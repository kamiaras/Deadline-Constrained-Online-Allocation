"""Copy one tracked PDF into a disposable website checkout and push normally."""

import argparse
import io
from pathlib import Path
import subprocess
import sys

from pypdf import PdfReader


SOURCE_REMOTES = {
    "https://github.com/kamiaras/Deadline-Constrained-Online-Allocation",
    "https://github.com/kamiaras/Deadline-Constrained-Online-Allocation.git",
    "git@github.com:kamiaras/Deadline-Constrained-Online-Allocation.git",
}
WEBSITE_REMOTES = {
    "https://github.com/kamiaras/kamiaras.github.io",
    "https://github.com/kamiaras/kamiaras.github.io.git",
    "git@github.com:kamiaras/kamiaras.github.io.git",
}
DESTINATION = "assets/pdf/Deadline-Constrained-Online-Allocation.pdf"
MAX_ATTEMPTS = 4


class SyncError(RuntimeError):
    pass


def git(root, *args, check=True):
    result = subprocess.run(
        ["git", "-C", str(root), *args],
        capture_output=True,
        text=True,
        timeout=120,
    )
    if check and result.returncode:
        # Do not echo Git output: it may contain authentication details.
        raise SyncError(f"Git {args[0]} failed.")
    return result


def check_checkout(root, remotes, branch):
    if git(root, "remote", "get-url", "origin").stdout.strip() not in remotes:
        raise SyncError("Unexpected repository origin.")
    if git(root, "branch", "--show-current").stdout.strip() != branch:
        raise SyncError(f"Expected the {branch} branch.")
    if git(root, "status", "--porcelain", "--untracked-files=all").stdout:
        raise SyncError("Use a clean, disposable checkout.")


def read_pdf(source):
    path = source / "main.pdf"
    if path.is_symlink() or not path.is_file():
        raise SyncError("The source main.pdf is missing or is not a regular file.")
    entry = git(source, "ls-tree", "HEAD", "--", "main.pdf").stdout
    if not entry.startswith("100644 blob "):
        raise SyncError("The source main.pdf must be a tracked regular file.")
    if git(source, "diff", "--quiet", "HEAD", "--", "main.pdf", check=False).returncode:
        raise SyncError("The source main.pdf differs from the tracked version.")
    data = path.read_bytes()
    if not data.startswith(b"%PDF-") or not data.rstrip().endswith(b"%%EOF"):
        raise SyncError("The source is not a complete PDF.")
    try:
        reader = PdfReader(io.BytesIO(data), strict=True)
        if reader.is_encrypted or not reader.pages:
            raise ValueError("Encrypted or empty PDF")
        for page in reader.pages:
            if page.mediabox.width <= 0 or page.mediabox.height <= 0:
                raise ValueError("Invalid page dimensions")
            contents = page.get_contents()
            if contents is not None:
                # Parse the content streams as well as the page tree.
                _ = contents.operations
    except Exception as error:
        raise SyncError("The source PDF could not be read safely.") from error
    return data


def destination_path(website):
    target = website / DESTINATION
    for component in (target, *target.parents):
        if component == website:
            break
        if component.is_symlink():
            raise SyncError("The website PDF path must not contain symlinks.")
    if target.exists() and not target.is_file():
        raise SyncError("The website PDF path is not a regular file.")
    return target


def check_source_current(source):
    local = git(source, "rev-parse", "HEAD").stdout.strip()
    remote = git(source, "ls-remote", "--exit-code", "origin", "refs/heads/main").stdout.split()
    if len(remote) != 2 or remote[0] != local:
        raise SyncError("Source main changed; a newer workflow run must publish its PDF.")


def publish(source, website):
    source, website = source.resolve(), website.resolve()
    if source == website or source in website.parents or website in source.parents:
        raise SyncError("Source and website must be separate checkouts.")
    check_checkout(source, SOURCE_REMOTES, "main")
    data = read_pdf(source)
    check_checkout(website, WEBSITE_REMOTES, "master")

    for attempt in range(1, MAX_ATTEMPTS + 1):
        check_source_current(source)
        git(website, "fetch", "--no-tags", "origin", "master")
        base = git(website, "rev-parse", "FETCH_HEAD").stdout.strip()
        # This clean checkout is disposable. Reapply only our PDF to the latest
        # remote tree after a race, retaining concurrent CV and website changes.
        git(website, "checkout", "-B", "master", base)
        target = destination_path(website)
        if target.exists() and target.read_bytes() == data:
            print("Website PDF is already current; no commit created.")
            return "unchanged"
        target.parent.mkdir(parents=True, exist_ok=True)
        target.write_bytes(data)
        git(website, "add", "--", DESTINATION)
        staged = git(website, "diff", "--cached", "--name-only", "-z").stdout
        if staged != DESTINATION + "\0":
            raise SyncError("Refusing to commit files outside the PDF destination.")
        git(
            website,
            "-c", "user.name=github-actions[bot]",
            "-c", "user.email=41898282+github-actions[bot]@users.noreply.github.com",
            "commit", "-m", "Update deadline allocation note PDF",
        )
        check_source_current(source)
        pushed = git(website, "push", "origin", "HEAD:refs/heads/master", check=False)
        if pushed.returncode == 0:
            print("Updated the website PDF.")
            return "updated"
        if attempt == MAX_ATTEMPTS:
            raise SyncError("Website push failed after four attempts.")
        git(website, "fetch", "--no-tags", "origin", "master")
        if git(website, "rev-parse", "FETCH_HEAD").stdout.strip() == base:
            raise SyncError("Website push failed without a concurrent branch update.")
        print("Website branch changed during sync; retrying on its latest commit.")


def main():
    parser = argparse.ArgumentParser(description=__doc__)
    parser.add_argument("--source", required=True, type=Path)
    parser.add_argument("--website", required=True, type=Path)
    args = parser.parse_args()
    try:
        publish(args.source, args.website)
    except (SyncError, OSError, subprocess.TimeoutExpired) as error:
        # Avoid dumping a parser traceback or credential-bearing subprocess data.
        message = str(error) if isinstance(error, SyncError) else "Local operation failed."
        print(f"PDF sync failed: {message}", file=sys.stderr)
        return 1
    return 0


if __name__ == "__main__":
    raise SystemExit(main())

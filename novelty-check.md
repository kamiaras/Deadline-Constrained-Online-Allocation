# Novelty assessment: Deadline-Constrained Online Allocation

Search date: 17 September 2026. Manuscript reviewed: `main.tex` in this project.

## Assessment

The search did **not identify a prior paper establishing the complete combination of this manuscript's model, comparator, progressive controller, and stated bounds**. The strongest defensible positioning is a specific construction and analysis for lossless scalar storage with mandatory per-arrival deadlines. Several central ingredients have close, established predecessors. The manuscript should not claim that scheduling filters, simplex storage policies, tree regret decomposition, delayed optimism, or deadlines combined with learning are individually new.

This is a literature-based assessment, not a proof of priority or an independent validation of every theorem. The search covered primary proceedings, publisher records, author manuscripts, and arXiv, including available 2026 work. Unindexed papers, inaccessible versions, and unpublished research may remain. The actual theorem assumptions matter more than a matching title or abstract.

## What was compared

The target result combines all of the following:

1. Lossless dynamics `x[t+1] = x[t] - u[t] + w[t]`, nonnegative adversarial arrivals, and no service beyond available resource.
2. Complete service of **every** arrival at ages 1 through H, including service after the cost horizon when necessary.
3. A current action chosen before the current arrival and jointly convex cost are revealed; full cost feedback afterward.
4. Hindsight comparison with every fixed probability distribution over service ages, each evaluated on its own state trajectory under the same realized environment.
5. Progressively chosen chronological tree splits, with local delays and prediction errors, and regret `O(Lu sqrt(H0 T) + Lx H0^(3/2) sqrt(T))`, where `H0 = min(H,T)`.
6. A matching storage-dependent lower bound for signed state marginals, and a positive-holding-cost reduction with a finite-horizon correction.

A paper matching only some of these conditions can be an important antecedent without subsuming the theorem.

## Closest overlaps and their implications

| Manuscript component | Closest prior work | Implication for positioning |
|---|---|---|
| Fixed age-distribution filters | [Khojastepour and Sabharwal, INFOCOM 2004](https://doi.org/10.1109/INFCOM.2004.1354603); [Xu et al., TPDS 2010](https://doi.org/10.1109/TPDS.2010.22) | The normalized finite-filter representation is established. Claim the learning guarantee for this class, rather than invention of the class. |
| Adversarial scalar storage with simplex policies | [Asgari and Neely, September 2026](https://arxiv.org/abs/2609.07690) | This is a particularly close model-level antecedent and warrants prominent discussion. The lossless deadline result needs its own argument. |
| Local-to-global tree identity | [Farina, Kroer, and Sandholm, AAAI 2019](https://doi.org/10.1609/aaai.v33i01.33011917); [Zinkevich et al., NIPS 2007](https://papers.nips.cc/paper_files/paper/2007/hash/08d98638c6fcd194a4b1e6992063e944-Abstract.html) | The comparator-mass-weighted identity is an elementary specialization of established counterfactual/laminar decomposition. The chronology and physical service interpretation require additional analysis. |
| Tree-local prediction and geometry | [Farina et al., ICML 2019](https://proceedings.mlr.press/v97/farina19a.html); [Farina et al., NeurIPS 2019](https://papers.neurips.cc/paper_files/paper/2019/hash/b030afbb3a8af8fb0759241c97466ee4-Abstract.html) | Neither prediction on trees nor local quadratic/entropy regularization is a separate novelty claim. |
| Delayed prediction-error learning | [Flaspohler et al., ICML 2021](https://proceedings.mlr.press/v139/flaspohler21a.html); [Abdullah et al., AAAI 2026](https://ojs.aaai.org/index.php/AAAI/article/view/39031) | The relevant specialization is the causal marginal-cost target and exact service feasibility, rather than delayed optimism itself. |
| Memory-length hardness | [Kumar, Dean, and Kleinberg, NeurIPS 2023, Appendix D](https://papers.nips.cc/paper_files/paper/2023/file/531230cfac80c65017ad0f85d3031edc-Paper-Conference.pdf) | The `H^(3/2) sqrt(T)` exponent has a general-memory antecedent. Establishing it inside this storage subclass remains a distinct issue. |
| Full service under uniform relative deadlines and predictions | [Bamas et al., NeurIPS 2020](https://proceedings.neurips.cc/paper_files/paper/2020/hash/af94ed0d6f5acc95f97170e3685f16c0-Abstract.html) | The consumption-only feasibility model is closely related. Their known energy law and workload-prediction competitive objective differ. |
| Regret in deadline scheduling | [Mlika, Driouch, and Ajib, GLOBECOM 2019](https://www.labunix.uqam.ca/~ajib_w/index_fichiers/Publi_Conf/Ajib_Globecom2019.pdf); [Cayci and Eryilmaz, 2019](https://arxiv.org/abs/1811.10829) | Deadlines with learning/regret are established; admission, unsuccessful transmission, and finite policy classes differ from mandatory service of all arrivals. |
| Exact safety and regret | [Li, Das, and Li, AAAI 2021](https://ojs.aaai.org/index.php/AAAI/article/view/17035); [Zhou and Tzoumas, 2023](https://arxiv.org/abs/2308.12395) | Exact constraint satisfaction is not new in general. The age-conservation construction, boundary feasibility, and comparator distinguish this result. |
| Recent deadline-related no-regret model | [Zhang and Mo, July 2026](https://arxiv.org/abs/2607.27626) | Modeled peak-AoI safety is different from complete per-arrival service. This preprint is included as adjacent work, not as an independently audited theorem. |
| Maximum-delay queue control | [Neely, Saber Tehrani, and Dimakis, 2010](https://arxiv.org/abs/1006.4649) | Do not contrast all queue-based methods with hard deadlines: virtual queues can produce worst-case delay guarantees. |
| Storage and flexible demand | [Lechowicz et al., SIGMETRICS 2026 full version](https://arxiv.org/abs/2511.18554v2) | Storage, deadlines, and learning also coexist in richer demand-management models, with a different competitive benchmark. |

### Why the closest storage paper does not directly subsume the result

The SDAC main theorem assumes retention strictly below one; its bounds rely on that contraction. Its stabilizing extension requires a positive consumption baseline. For H greater than one, such a baseline excludes a comparator that waits until age H. The present guarantee instead includes that comparator and requires exact exhaustion by a finite age. This is a comparison of the published assumptions, not a claim that no modification of SDAC could produce another solution.

### What remains potentially distinctive

- The physical chronology of the service-age tree: later subdecisions for a single arrival can use intervening observations while earlier allocations remain binding.
- The coupling of interval length to both local feedback delay and marginal-cost range, including cancellation of the common holding-cost prefix.
- The resulting separation of action and state contributions to regret against the entire age simplex, while preserving every arrival's deadline.
- Realizing matching signed-storage hardness in this constrained physical system, where an algorithm may react progressively.
- The positive-storage-marginal support reduction with the explicit finite-cost-horizon correction. No direct antecedent for that precise comparison lemma surfaced; virtual-deadline shortening itself is established elsewhere.

These are candidates supported by the examined literature, rather than unconditional claims of firstness. The most useful referee-facing comparison is the *combination* of these points.

### Claims that should stay qualified

- The storage lower bound allows negative state slopes. It does not establish the same rate for ordinary nonnegative holding costs.
- The action-only lower bound leaves a factor of `sqrt(H0)` between the stated bounds. Full minimax optimality is not established.
- The reported `sqrt(T)` rate holds for fixed deadline and marginal bounds. The deadline factors matter when H grows.
- Costs and arrivals may respond to the controller, but the comparison holds the realized environment fixed. It does not rerun an adaptive adversary under alternative policies; see [Arora, Dekel, and Tewari](https://icml.cc/2012/papers/749.pdf).
- Constant competitive ratios for a known energy objective neither directly give the stated additive regret nor make the restricted filter comparator stronger than an unrestricted offline schedule.

## Search coverage and evidence limits

Three independent literature passes covered (i) control, constraints, memory and inventory; (ii) scheduling, filters, energy and deadlines; and (iii) tree learning, delay, optimism and lower bounds. The main pass additionally searched exact manuscript-title and age-allocation phrases, deferrable loads, budgeted allocation, inventory learning, and recent deadline-aware scheduling. Representative searches included “deadline regret allocation convex storage,” “online deferrable regret deadlines,” “deadline laminar regret,” “simplex disturbance-action storage,” and the exact titles of the closest papers. Reference chains were followed from the most relevant primary papers.

Comparisons used the manuscript's formal information pattern, service equations, comparator, local feedback, master bound, and lower-bound statements. Full-text checks were prioritized for the main overlap risks. Publisher or author abstracts were used for broader context; those entries do not support claims of theorem equivalence. The complete Khojastepour–Sabharwal PDF could not be retrieved, but indexed original-paper theorem passages and the primary repository record confirmed the normalized-filter and i.i.d. long-run-power scope. That limitation does not justify claiming a broader absence of overlap.

Recent preprints are explicitly labeled. Kumar et al. was corrected to its NeurIPS 2023 publication, Fan et al. to NeurIPS 2024, and Farina et al.'s later regularization paper to its 2025 journal version. Some online-publication years differ from final issue years; the bibliography uses final publication information where verified and identifies the full arXiv version when that is the version examined.

## Changes made

- Expanded Related Work to eleven subsections (approximately 2,800 words) covering the comparisons above.
- Added 40 references, bringing the bibliography from 11 to 51, with every entry cited.
- Added attribution beside the contributions, tree identity, local optimistic estimate, and lower-bound introduction.
- Preserved theorem statements, algorithms, equations, and proofs.
- Rebuilt the manuscript and checked bibliography consistency and rendered pages.

Temporary build files and backup copies were removed during repository cleanup. Earlier tracked versions of the manuscript, bibliography, and PDF remain available in Git history.

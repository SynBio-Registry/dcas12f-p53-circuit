# Model Writeup: dCas12f/p53 Epigenetic Circuit

## Background

Transient attenuation of p53 activity may permit the accumulation of genomic lesions during reprogramming, including replication stress and DNA damage. While subsequent reactivation may eliminate severely compromised cells, mutational events arising during the suppressed phase may persist — representing a fundamental limitation of any p53-modulating strategy.

## System Architecture and Logic States

This study presents a theoretical and systems-level design rather than an experimentally validated platform. The proposed architecture is intended to illustrate how programmable epigenetic regulators could be integrated with endogenous stress-response pathways, and should therefore be interpreted as a hypothesis-generating framework.

Several optimized molecular components described throughout this framework are hypothetical engineering abstractions intended to represent future design targets rather than experimentally validated constructs.

The circuit operates across four environmental states, managed by a dual-input sensor detecting hypoxia and MYC overexpression:

| State | Environmental Trigger | p53 Epigenetic Status |
|---|---|---|
| 0 — Silenced | Basal homeostasis | Hypermethylated (silenced) |
| 1 — Reprogramming | OSKM induction + ligand absent | Translationally restricted cassette (aptazyme-locked) |
| 2 — Surveillance | Ligand present + hypoxia/MYC | Demethylation of core promoter (basal activation) |
| 3 — High-Activation | Malignant transformation threshold | Synergistic transactivation (high output) |

In practice, these state transitions would emerge from graded signal integration rather than discrete switching, and would likely exhibit substantial cell-to-cell variability due to stochastic gene expression and chromatin accessibility.

## Technical Specification of the High-Fidelity Chassis

The proposed framework incorporates a highly compact, engineered dCas12f-derived scaffold to achieve dynamic control over p53 transcriptional activity while preserving single-vector packaging compatibility. This miniature alternative scaffold contains catalytic-domain mutations that eliminate double-stranded DNA cleavage activity while fully preserving programmable, high-fidelity target sequence recognition.

To control the p53 epigenetic landscape without modifying the underlying sequence, the system relies on a bifurcated split-effector recruitment array using specialized, minimized fusion proteins:

- MCP-TDG-mCD (Targeted Demethylation Module) — recruited via MS2 coat protein interactions to target active DNA demethylation to the CpG islands of the p53 promoter during surveillance and reactivation states.
- PCP-p300∆-HAT/p65-Rta (Transcriptional Activation Module) — recruited via PP7 coat protein interactions to mediate locus-specific H3K27 acetylation and drive synergistic transcriptional output under severe oncogenic or cellular stress.

The localization array uses multiplexed tRNA-crRNA architectures combined with compact com and PP7 RNA aptamers to enable multi-site promoter targeting. Endogenous RNase P and RNase Z processing generates multiple guide RNAs from a single transcript, enabling coordinated promoter occupancy. The p300 histone acetyltransferase region is structurally minimized to preserve catalytic H3K27 acetylation activity within a reduced sequence footprint, while cooperatively recruiting RNA Polymerase II.

## The Stress-Tolerant p53 Variant Architecture

A critical component of this framework is the incorporation of a modeled p53 response profile inspired by comparative studies of chiropteran (bat) tumor suppression and longevity mechanisms. Certain bat species exhibit enhanced tolerance to DNA damage and altered apoptotic thresholds, suggesting that evolutionary variation in p53 pathway regulation may bias cellular outcomes toward repair-oriented responses under moderate stress.

Within this framework, "Allele B" represents a hypothetical engineered p53 variant incorporating functional characteristics associated with elevated DNA damage tolerance and altered repair-apoptosis thresholds, rather than a direct cross-species gene transfer construct.

By assigning:

- Allele A: canonical human TP53 response (rapid stress-induced apoptosis/senescence)
- Allele B: modified p53 response profile with elevated activation threshold and increased weighting toward DNA repair-associated intermediate states

the framework enables a modular stress-response architecture capable of transitioning between conservative tumor suppression and reprogramming-permissive cellular states depending on environmental input.

However, the feasibility of engineering p53 variants with predictable and tunable network behavior remains highly uncertain due to species-specific regulatory context dependence and extensive coupling within endogenous p53 signaling pathways.

## Mathematical Modeling of Circuit Activation

The transition between State 2 (Surveillance) and State 3 (High-Activation) is modeled using a Hill-coefficient-based activation function. The concentration of functional p53 ([P]) in response to oncogenic signaling intensity ([S]) is expressed as:

[P] = Vmax · [S]^n / (K^n + [S]^n)

Where Vmax represents the maximum transcriptional output of the modified p53 architecture, K represents the oncogenic activation threshold, and n denotes the cooperativity coefficient governing epigenetic scaffold recruitment dynamics.

By adjusting scaffold recruitment multiplicity, the system can theoretically achieve increasingly switch-like responses (n > 2), producing sharper activation thresholds in response to escalating oncogenic stress.

To model autoregulatory feedback dynamics, system expression over time is approximated using ordinary differential equations (ODEs). Let [M] denote active circuit mRNA concentration, [C] represent intracellular epigenetic scaffold concentration, and [P] indicate total intracellular p53 concentration:

d[M]/dt = alpha_m * 1/(1 + ([P]/K_beta)^m) * theta_L - gamma_m[M]
d[C]/dt = alpha_c[M] - gamma_c[C]
d[P]/dt = Vmax*[C]^n / (K^n + [C]^n) - gamma_p[P]

Where parameters alpha_x and gamma_x define molecular production and degradation rate constants. The parameter K_beta captures the operational threshold for negative feedback inhibition, while m represents the feedback cooperativity coefficient. The parameter theta_L acts as a normalized ligand-dependent activation parameter (0 <= theta_L <= 1) governed by aptazyme-mediated riboswitch activation. The clearance parameter gamma_c incorporates rapid proteasomal degradation kinetics mediated through a proteasome-targeting degron domain.

Note on parameter values: the numeric values used in model/ode_model.py are illustrative placeholders chosen to produce stable, interpretable dynamics — they are not yet fitted to literature-derived kinetic data. Sourcing real parameter estimates from published CRISPRi/CRISPRa and p53 pathway kinetics literature is a planned next step (see README roadmap).

## Vector Engineering and Payload Optimization

A major limitation in the therapeutic translation of CRISPR-based epigenetic systems is the packaging constraint of Adeno-Associated Virus (AAV) vectors, typically limited to approximately ~4.7 kb. Conventional dSpCas9 architectures frequently exceed this threshold, necessitating multi-vector delivery strategies that reduce transduction efficiency.

To preserve single-vector delivery compatibility, the framework implements a compact CRISPR epigenetic architecture. By substituting dSpCas9 with compact dCas12f variants and replacing bulky recruitment networks with miniature aptamer-based logic, the total payload size is substantially reduced while preserving modular functionality.

The optimized architecture incorporates a compact synthetic polyadenylation sequence (sAAV-pA) alongside a minimized JeT promoter to preserve adequate packaging headroom for stable encapsulation and high viral titers.

| Component | Standard (v1) | Optimized Architecture | Engineering Rationale |
|---|---|---|---|
| Cas Scaffold | dSpCas9 (~4.1 kb) | Engineered dCas12f variant (~1.4 kb) | Compact high-fidelity scaffold optimized for epigenetic recruitment |
| Targeting | scFv Array (~0.8 kb) | com/PP7 Aptamers (~0.25 kb) | Reduces steric complexity and improves compactness |
| Promoter | CMV (~0.8 kb) | Minimal JeT promoter (~0.16 kb) | Reduces total vector footprint while preserving expression |
| Effector | p300 Full Domain | p300∆-mini VPR (~0.9 kb) | Retains catalytic acetyltransferase activity in minimized form |
| Regulation | None | Aptazyme/Feedback (~0.15 kb) | Enables ligand-sensitive temporal regulation |
| Safety/Reporter | None | P2A-mNeonGreen-Degron (~0.75 kb) | Enables co-expression tracking and degradation control |
| Termination | SV40 polyA (~0.2 kb) | sAAV-pA (~0.05 kb) | Compact transcriptional termination sequence |
| Total Size | ~5.7 kb | ~3.95 kb | Preserves packaging headroom for stable AAV encapsulation |

## Implementation: The Linear Architecture

The optimized system is designed as a modular expression cassette. Through the incorporation of compact nuclear localization signals (NLS) and minimized regulatory elements, the framework maintains efficient nuclear import while preserving limited vector space.

This architecture also permits potential multiplexing, where multiple independent p53-targeting circuits may theoretically be packaged within a single AAV capsid depending on payload constraints.

To enforce stoichiometric expression ratios, a P2A self-cleaving peptide linker is positioned downstream of the epigenetic scaffold sequence. This coordinated translation process generates both the fluorescent mNeonGreen reporter and the upstream scaffold at approximately equivalent molar ratios, enabling live-cell monitoring of intracellular scaffold abundance.

Additionally, recombination-buffering flanking sequences are incorporated to reduce the probability of vector deletion or homologous recombination during large-scale vector amplification.

## Conclusion

This work presents a theoretical framework for dynamically regulating p53 activity through programmable epigenetic circuitry during cellular reprogramming. By integrating compact CRISPR-based recruitment systems, environmental sensing logic, and conditional feedback regulation, the proposed architecture attempts to reconcile the competing demands of cellular plasticity and tumor suppression.

Despite the conceptual advantages of such a system, major translational barriers remain unresolved, including stochastic chromatin dynamics, mutational accumulation during transient p53 suppression, delivery efficiency, off-target epigenetic remodeling, and long-term genomic stability. Consequently, this framework should be interpreted as a hypothesis-generating systems model rather than an immediately deployable therapeutic strategy.

Future work would require experimental validation of programmable epigenetic fidelity, multi-state control robustness, vector stability, and cellular safety thresholds before clinical implementation could be considered.

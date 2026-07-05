# dCas12f/p53 Epigenetic Circuit — Computational Model

![License](https://img.shields.io/badge/license-MIT-blue.svg)
![Status](https://img.shields.io/badge/status-in%20silico-orange.svg)
![Python](https://img.shields.io/badge/python-3.10+-blue.svg)

> A theoretical, systems-level model of a feedback-controlled dCas12f
> epigenetic circuit for programmable p53 regulation during cellular
> reprogramming and oncogenic stress states.

## Overview

This project models a synthetic epigenetic circuit that uses a compact,
catalytically-dead Cas12f (dCas12f) scaffold to dynamically regulate p53
transcriptional activity — without editing the underlying DNA sequence.

The circuit is designed to toggle p53 through four logic states depending on
environmental input (hypoxia, MYC overexpression, reprogramming factors):

| State | Trigger | p53 Status |
|---|---|---|
| 0 — Silenced | Basal homeostasis | Hypermethylated (silenced) |
| 1 — Reprogramming | OSKM induction, no ligand | Translationally restricted (aptazyme-locked) |
| 2 — Surveillance | Ligand + hypoxia/MYC | Core promoter demethylated (basal activation) |
| 3 — High-Activation | Malignant transformation threshold | Synergistic transactivation (high output) |

**This is a theoretical and systems-level design, not an experimentally
validated platform.** It is intended as a hypothesis-generating framework —
see [Status & Limitations](#status--limitations).

## The Circuit

![Circuit Diagram](figures/circuit_diagram.png)

Two split-effector modules are recruited to the p53 promoter via RNA aptamer
scaffolds (MS2/PP7):

- **MCP-TDG-mCD** — targeted demethylation of p53 promoter CpG islands
  during surveillance/reactivation states.
- **PCP-p300∆-HAT/p65-Rta** — locus-specific H3K27 acetylation driving
  transcriptional output under oncogenic stress.

A ligand-gated aptazyme riboswitch provides temporal control, and a
proteasome-targeting degron sets the clearance rate of the scaffold protein.

## Mathematical Model

Circuit activation (State 2 → 3) follows a Hill-type activation function:

[P] = Vmax · [S]^n / (K^n + [S]^n)

Autoregulatory dynamics are modeled as a 3-variable ODE system:

d[M]/dt = αm · 1/(1 + ([P]/Kβ)^m) · θL − γm[M]      # mRNA
d[C]/dt = αc[M] − γc[C]                              # scaffold protein
d[P]/dt = Vmax·[C]^n / (K^n + [C]^n) − γp[P]          # p53

| Symbol | Meaning |
|---|---|
| `[M]` | active circuit mRNA concentration |
| `[C]` | intracellular epigenetic scaffold concentration |
| `[P]` | total intracellular p53 concentration |
| `αx`, `γx` | production / degradation rate constants |
| `Kβ`, `m` | feedback threshold and cooperativity |
| `θL` | ligand-dependent activation input (0–1) |
| `n`, `K` | Hill cooperativity coefficient and activation threshold |

Full derivation and parameter rationale: [`docs/model_writeup.md`](docs/model_writeup.md)

## Quick Start

git clone https://github.com/SynBio-Registry/dcas12f-p53-circuit.git
cd dcas12f-p53-circuit
pip install -r requirements.txt
python model/ode_model.py

This runs the ODE system and produces a time-course plot of `[M]`, `[C]`,
and `[P]` under a chosen ligand/state input.

## Status & Limitations

This is a **computational, hypothesis-generating model**, not an
experimentally validated therapeutic system. Key open questions the model
does not resolve:

- Real state transitions would emerge from graded signal integration, not
  discrete switching, and would show substantial cell-to-cell variability.
- The "stress-tolerant p53 variant" (Allele B) is a modeled abstraction, not
  a validated engineered protein.
- Transient p53 suppression during reprogramming carries a theoretical risk
  of allowing genomic lesions to accumulate before reactivation.
- Feasibility of tunable p53 variant engineering is highly uncertain given
  species-specific regulatory context.

## Roadmap

- [ ] Parameter sensitivity analysis
- [ ] Stochastic (Gillespie) simulation to model cell-to-cell variability
- [ ] Comparison against any available published wet-lab kinetic data
- [ ] Formal review by outside computational/synbio researchers

## Citation

If you use this model, please cite:
[Your Name]. (2026). *dCas12f/p53 Epigenetic Circuit — Computational Model.*
SynBio Registry. https://osf.io/p95fc

## License

MIT — see [LICENSE](LICENSE)

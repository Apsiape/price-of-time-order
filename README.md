# The price of time order

Seth Douglas and Nidhal Mghirbi — October 2026.

[![DOI](https://zenodo.org/badge/DOI/10.5281/zenodo.23310622.svg)](https://doi.org/10.5281/zenodo.23310622)

[Read the manuscript](paper/main.pdf) · [TeX source](paper/main.tex) ·
[Machine checks](verification/README.md)

A physical device acts in time: inputs arrive, outputs are released and can no longer be touched, some systems
are kept, and some must come back. This paper shows that the optimal work rate of such a device, over many uses at vanishing error, is fixed by one quantity,
the least entropy that one implementation must add to its own record, plus the energy it hands over to the carriers, against the most demanding observer its schedule allows.

- **One law for every schedule** in which each borrowed system comes back with the Hamiltonian it arrived with:
  Landauer's bound, the thermodynamic capacity of time-covariant channels, the real-time cost of channels,
  interactive processes and the batch cost of a channel whose clock must be returned are special cases.
- **Order, not speed.** The cost survives arbitrarily slow operation; an operation can cost more merely because some of
  its outputs must leave sooner.
- **Which carriers to hold.** For linear tasks the price of a schedule is a rank, and deciding whether holding a given
  number of carriers lowers it at all is NP-complete.
- **A witness.** A two-qubit process that is free when held costs every early-release device at least 0.87 kT ln 2
  per episode at 1% error, when the energy and entropy budgets of its controller and battery total at most 0.025
  (energies in kT ln 2, entropies in bits); the error that enters is fixed by three Pauli measurements on one probe.
  A classical version needs no coherence.
- **Beyond thermodynamics.** Order has a price in entanglement and coherence theory too, with no single exchange rate
  between theories.
- **Holding is decidable, releasing is not.** In thermodynamics, whether a channel is free is decidable when outputs
  may be held and undecidable when they must be released; in the other theories examined, both are decidable.

All rates here are optimal asymptotic work rates at vanishing error over the complete interaction, with hardware
allowed to grow; where a controller comes back only approximately, its actual mean energy and entropy are also
refunded up to sublinear changes.

This repository contains the manuscript, its source, and the machine checks that accompany it. It is version 1.0.2 of the Zenodo record [doi:10.5281/zenodo.23310622](https://doi.org/10.5281/zenodo.23310622); that concept DOI always resolves to the latest version. Version 1.0.1 is [doi:10.5281/zenodo.23310735](https://doi.org/10.5281/zenodo.23310735) and version 1.0.0 is [doi:10.5281/zenodo.23310623](https://doi.org/10.5281/zenodo.23310623). The manuscript is the
authority for exact statements and hypotheses; [verification/README.md](verification/README.md) lists what is checked
by machine and what is proved only in the text.

## Reproduce

Requires Python 3.10+ with the packages in [verification/requirements.txt](verification/requirements.txt), a TeX
distribution with the packages listed in paper/main.tex, and, for the formal proofs, Lean 4 with Mathlib as described
in [verification/README.md](verification/README.md).

    python -m pip install -r verification/requirements.txt
    python paper/build.py
    python verification/run_all.py

The build refuses to finish on any undefined reference or citation, duplicate label or overfull line. Each check
prints what it verifies and exits with status 0 when it passes.
Until Mathlib is set up as described there, the Lean step reports that it was skipped and the run
fails; the Python checks do not need it.

## Companions

This paper is one of four on the thermodynamics of time order, each with its own repository:
- [Only quantum channels save work by waiting](https://github.com/Apsiape/save-work-by-waiting) · [doi:10.5281/zenodo.23310624](https://doi.org/10.5281/zenodo.23310624)
- [The work cost of answering in real time](https://github.com/Apsiape/answering-in-real-time) · [doi:10.5281/zenodo.23310628](https://doi.org/10.5281/zenodo.23310628)
- [The price of keeping time](https://github.com/Apsiape/price-of-keeping-time) · [doi:10.5281/zenodo.23310632](https://doi.org/10.5281/zenodo.23310632)

Earlier papers it builds on are listed, with the exact results used and where, in the appendix "Results from the
companion papers" of the manuscript.

## Reading guide

For the organizing principle, read the introduction, Figure 1 and Table 2 of *The price of time order*. For the device model,
the law for repeated channels and the free set, read *Only quantum channels save work by waiting*. For processes with
memory and the classical example of an order cost, read *The work cost of answering in real time*. For returned
clocks, the batch law and the time reverse, read *The price of keeping time*. Readers following proofs should note that
the finite-source module of *The work cost of answering in real time* (Appendix E, Lemma 12) is established
independently of the channel results it helps to prove.

## License and citation

The manuscript and repository content are available under **CC BY 4.0**. The software and machine-readable
verification artifacts are additionally available under the **MIT License**, at your option; see
[RIGHTS.md](RIGHTS.md) for the scope. [CITATION.cff](CITATION.cff) provides machine-readable citation metadata. Please cite the manuscript by its concept DOI, [10.5281/zenodo.23310622](https://doi.org/10.5281/zenodo.23310622).

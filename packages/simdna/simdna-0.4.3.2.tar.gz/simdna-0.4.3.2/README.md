# [simdna: simulated datasets of DNA](https://kundajelab.github.io/simdna/)
[![license](https://img.shields.io/github/license/mashape/apistatus.svg?maxAge=2592000)](https://github.com/kundajelab/simdna/blob/master/LICENSE)

## Installation
```
git clone https://github.com/kundajelab/simdna.git
cd simdna
python setup.py develop
```

## Examples
Please see the scripts folder for example scripts generating simulations and the scripts_test folder for example arguments.
- densityMotifSimulation.py generates a simulated dataset where multiple instances of motifs are present per sequence, as determined by a poisson distribution which could optionally be subject to zero-inflation.
- motifGrammarSimulation.py illustates how to set up a simulation where two motifs have a fixed-spacing or variable-spacing grammar (set `--generationSetting` to twoMotifsFixedSpacing or twoMotifsVariableSpacing as desired).
- emptyBackground.py just generates a background sequence with no motifs embedded.


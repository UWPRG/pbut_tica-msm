# "Analyzing the long time-scale dynamics of uremic toxins bound to Sudlow Site II in human serum albumin" 
James Ludwig, Josh Smith, and Jim Pfaendtner
---
For the purpose of making our scientific work both reproducible and transparent, this repository is home to supplemental files relating to the paper listed above. In this repo, you will find both analysis code and examples/files used to conduct or research. Futhremore, a brief outline of the methods/steps will be housed here. Along with the files present in this repo, all tools used to conduct this work are open source. We hope this repo supports those interested in the study of protein-ligand binding dynamics and the construction of MSM for biophysical challenges.

### Required Software

As described in the Methods section (2) of the paper, we use a combination of open source software. In order to recreate our results and conduct analysis, the following open source softward was used:

- [GROMACS](http://www.gromacs.org/) (2016.3)
- [PLUMED](https://www.plumed.org/) (2.4)
- [python](https://www.python.org/) (3.6)

Although it would be easiest to apply the following methods using the above software, if you are a seasoned MD professional - capable of calculating order parameters from an MD trajectory, you should be able to adapt our python scripts to read your results. The clustering and MSM analyses simply require that you can convert your data into pandas DataFrames and/or numpy arrays (see read_plumed_file() in util.py for an example). 

### Guide

- __Step 1__ - Use our methods section to generate a set (15) of simulations for the desired protein-ligand comlpex in aqueous solution.

- __Step 2__ - Follow procedure from previous work, using steps 2-4a from [Smith & Pfaendtner, 2020](https://github.com/UWPRG/pbut_analysis), in order to identify and monitor key residues of each system.

- __Step 3__ - Determine hyperparameters using fivefold cross validation analysis in python ('get-hyperparameters.ipynb').

- __Step 4__ - Tets, build, and analyze MSMs in python ('build-msm.ipynb').

- __Step 5__ -  Return to step 1 for any other ligands to be studied/compared.

### Attribution

When using the code above to conduct original research, please cite our upcoming paper and reference this code repository. Paper is currently in submission process, this will be updated. Thanks!

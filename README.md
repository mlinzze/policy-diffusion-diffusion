Overview
--------

The code in this replication package conducts the statistical analysis and produces the results presented in the manuscript. The package consists of several scripts written in Python 3 and Stata, as well as code in C++ for the Monte Carlo simulations.

Data Availability
----------------------------

All original data are publicly available at no cost.

See the section in the manuscript `Data availability` for more information.

Computational requirements
---------------------------

### Software Requirements

- Python 3.10.9
  - `numpy` 1.23.4
  - `pandas` 1.5.1
  - `scipy` 1.10.0
  - `statsmodels` 0.13.5
  - `geopandas` 0.12.0
  - `xarray` 2022.10.0
  - `matplotlib` 3.6.1
  - `seaborn` 0.12.0

The file `requirements.txt` lists these dependencies, please run `pip install -r requirements.txt` as the first step. See [https://pip.readthedocs.io/en/1.1/requirements.html](https://pip.readthedocs.io/en/1.1/requirements.html) for further instructions on using the `requirements.txt` file.

### Memory and Runtime Requirements

The analysis and visualisation of the processed data requires less than 1 hour on a standard (2024) desktop machine.

Instructions to Replicators
---------------------------

Replication of all figures:
- The file `parameters.py` includes some parameters that can be chosen by the user prior to executing the scripts. These include the path to the data (default: `./data/`).
- The replication is facilitated with a Makefile that runs the scripts in the correct order (`make clean; make all`).
- Note that the name of each script also indicates its relative position in the intended order of execution (i.e. `p01`, `p02`, `p03`, ...).
- Some of the scripts store intermediate data in the folder `data`. Results are stored in the folder `results`.
- The folder `simulations` includes the code for the Monte Carlo simulations. The folder has a separate Makefile that allows one to run the simulations, including the sensitivity analysis.
- Once all scripts have finished, all figures can be found in the folder `figures` and all tables will be in the folder `tables`.

For the replication of specific figures, see the following list:
- Figure 1: `p01_descriptive_statistics.py`
- Table 1: `p05_plot_modelfit.py`
- Figure 2a: `p04b_compare_coefficients.py`
- Figure 2b: `p04a_plot_coefficients.py`
- Figure 3a,b: `p06a_quantify_adoption.py`
- Figure 4a: `p07a_visualise_solar-expansion.py`
- Figure 4b: `p07b_visualise_emission-reductions.py`
- Figure A1: `p01_plot_timeline.py`
- Figure B1: `p03_variable_selection.py`
- Figure B2,C1,C2,C3: `p04a_plot_coefficients.py`

### License for Code and Data

The code in this repository is provided only for the purpose of replicating the results for peer-review. All other uses of the code or data are strictly prohibited.
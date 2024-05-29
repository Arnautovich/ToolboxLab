# ToolboxLab
[![alt text](https://img.shields.io/badge/Python-14354C?style=for-the-badge&logo=python&logoColor=white)](https://www.python.org)
[![alt text](https://camo.githubusercontent.com/d9715378ddbf6b262203f7c27f12eeb6a7caa3b85a56cc980dbb2648753d526c/68747470733a2f2f696d672e736869656c64732e696f2f62616467652f4a7570797465722d4633373632362e7376673f267374796c653d666f722d7468652d6261646765266c6f676f3d4a757079746572266c6f676f436f6c6f723d707572706c65)](https://jupyter.org)
[![license](https://img.shields.io/badge/License-MIT-ac8b11.svg?style=for-the-badge&labelColor=yellow)](https://github.com/Arnautovich/Toolbox/blob/main/LICENSE)
[![open an issue](https://custom-icon-badges.demolab.com/badge/-Open%20Issue-palegreen?style=for-the-badge&logoColor=black&logo=issue-opened)](https://github.com/Arnautovich/Toolbox/issues)

<!---<p align="center">
<img width="500" src="https://github.com/Nicolas-jnn/host/blob/main/Logo.png">
</p>--->

<p align="center">
<img width="500" src="https://github.com/Arnautovich/ToolboxLab/assets/132769698/ce5efe17-79a6-4fc1-b8b3-b1a405cd1c28">
</p>


## Overview

**ToolboxLab** is a Python package designed to assist chemical engineers and chemists with essential calculations and automation in various domains such as distillation, reaction stoichiometry, acid/base chemistry, liquid-liquid extraction (LLE), pH calculations, boiling point determination, molecular properties and safety concerns extraction, and a solvent ranking system. The package provides robust functions to simplify complex calculations and visualize key processes.

## Authors
Three authors contributed to this project:
- **Bruno Gonçalves Oliveira**, BSc in chemistry and chemical engineering at **[EPFL](https://www.epfl.ch)**   [![alt text](https://img.shields.io/badge/GitHub-100000?style=for-the-badge&logo=github&logoColor=white)](https://github.com/BrunoGonOli)

- **Arnau Casalprim Perez**, BSc in chemistry and chemical engineering at **[EPFL](https://www.epfl.ch)**   [![alt text](https://img.shields.io/badge/GitHub-100000?style=for-the-badge&logo=github&logoColor=white)](https://github.com/Arnautovich)
- **Nicolas Jenni**, BSc in chemistry and chemical engineering at **[EPFL](https://www.epfl.ch)**   [![alt text](https://img.shields.io/badge/GitHub-100000?style=for-the-badge&logo=github&logoColor=white)](https://github.com/Nicolas-jnn)
## Features

- **Distillation Calculations**: Calculate the needed number of stages and generate McCabe-Thiele diagrams for distillation processes.
- **Chemical Reaction**: Determine the stoichiometric coefficients based on a given reaction string and retrieve properties of the products and reactants.
- **Acid/Base Calculations**: Calculate the pH or concentration of acids and bases in solutions.
- **Liquid-Liquid Extraction (LLE)**: Calculate the number of stages for both counter-flow and cross-flow LLE processes.
- **pH Calculations**: Perform pH calculations
- **Boiling Point Determination**: Estimate the boiling points of compounds at different pressure
- **Molecular Properties and Safety Data Extraction**: Retrieve detailed molecular properties and safety data sheets (SDS) for chemicals.
- **Solvent Ranking System**: Rank solvents based on given specific properties (boiling point, polarity, viscosity) and the type of reaction that want to be performed

## Installation
The package **Toolbox** can be easily installed using pip, the package installer for Python. This package requires a Python version newer or equal to version **3.10.14**. Open your terminal or command prompt and run the following command:
```
pip install git+https://github.com/Arnautovich/ToolboxLab.git
```

It can also be installed locally.
```
cd /to_dir/
git clone https://github.com/Arnautovich/ToolboxLab.git
pip install .
```

## Requirements
To use the safety-datasheet function, poppler should be installed according to the documentation found on their [website](https://pdf2image.readthedocs.io/en/latest/installation.html). For macOS users, it is also necessary to download [Homebrew](https://brew.sh) to install Poppler.

When installing the Toolbox package, the necessary dependencies should be installed automatically. However, if the dependencies are not installed as expected, please ensure you manually install the following packages by executing the corresponding commands:
```
pip install matplotlib
pip install rdkit
pip install pubchempy
pip install pandas
pip install scipy
pip install typing
pip install chemicals
pip install pdf2image
pip install requests
```
## Usage
For an example of the utilization of each function, please refer to the [jupyter notebook](https://github.com/Arnautovich/Toolbox/blob/main/notebooks/project_report.ipynb)

### Interface
This project also has an interface-based UI to interact with the functions. To run the interface, make sure that **streamlit** package was installed when installing **ToolboxLab** or install it by
```
pip install streamlit
```
Then go to the directory where you cloned the repository and launch the **run.py** file that is in the [scripts](https://github.com/Arnautovich/ToolboxLab/tree/main/scripts) folder. Upon execution, you should arrive at the homepage shown below, where you can select the application you wish to use.

<img width="1511" alt="Home_Page" src="https://github.com/Arnautovich/ToolboxLab/assets/132769698/44e5f00b-fc39-46e6-bf09-31fed85496ba">


## License

This project is licensed under the **MIT License** - see the [LICENSE file](https://github.com/Arnautovich/ToolboxLab/blob/main/LICENSE) for details.

## Contact
For any questions or issues, please open an issue on GitHub[![open an issue](https://custom-icon-badges.demolab.com/badge/-Open%20Issue-palegreen?style=for-the-badge&logoColor=black&logo=issue-opened)](https://github.com/Arnautovich/Toolbox/issues)

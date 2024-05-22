# ToolboxLab

[![alt text](https://img.shields.io/badge/Python-14354C?style=for-the-badge&logo=python&logoColor=white)](https://www.python.org)
[![alt text](https://camo.githubusercontent.com/d9715378ddbf6b262203f7c27f12eeb6a7caa3b85a56cc980dbb2648753d526c/68747470733a2f2f696d672e736869656c64732e696f2f62616467652f4a7570797465722d4633373632362e7376673f267374796c653d666f722d7468652d6261646765266c6f676f3d4a757079746572266c6f676f436f6c6f723d707572706c65)](https://jupyter.org)
[![open an issue](https://custom-icon-badges.demolab.com/badge/-Open%20Issue-palegreen?style=for-the-badge&logoColor=black&logo=issue-opened)](https://github.com/Arnautovich/Toolbox/issues)
[![license](https://custom-icon-badges.demolab.com/github/license/denvercoder1/custom-icon-badges?logo=law&logoColor=white)](https://github.com/Arnautovich/Toolbox/blob/main/LICENSE)



## Overview

Toolbox is a Python package designed to assist chemical engineers and chemists with essential calculations in various domains such as distillation, reaction stoichiometry, acid/base chemistry, and liquid-liquid extraction (LLE). The package provides robust functions to simplify complex calculations and visualize key processes.

## Authors
Three authors contributed to this project:
- **Bruno Gonçalves Oliveira**, BSc in chemistry and chemical engineering at **[EPFL](https://www.epfl.ch)**   [![alt text](https://img.shields.io/badge/GitHub-100000?style=for-the-badge&logo=github&logoColor=white)](https://github.com/BrunoGonOli)

- **Arnau Casalprim Perez**, BSc in chemistry and chemical engineering at **[EPFL](https://www.epfl.ch)**   [![alt text](https://img.shields.io/badge/GitHub-100000?style=for-the-badge&logo=github&logoColor=white)](https://github.com/Arnautovich)
- **Nicolas Jenni**, BSc in chemistry and chemical engineering at **[EPFL](https://www.epfl.ch)**   [![alt text](https://img.shields.io/badge/GitHub-100000?style=for-the-badge&logo=github&logoColor=white)](https://github.com/Nicolas-jnn)
## Features

- **Distillation Calculations**: Calculate the needed number of stages and generate McCabe-Thiele diagrams for distillation processes.
- **Stoichiometric Coefficients**: Determine the stoichiometric coefficients based on a given reaction string and retrieve properties of the products and reactants.
- **Acid/Base Calculations**: Calculate the pH or concentration of acids and bases in solutions.
- **Liquid-Liquid Extraction (LLE)**: Calculate the number of stages for both counter-flow and cross-flow LLE processes.

## Installation
The package **Toolbox** can be easily installed using pip, the package installer for Python. Open your terminal or command prompt and run the following command:
```
pip install git+https://github.com/Arnautovich/Toolbox.git
```

It can also be installed locally.
```
cd /to_dir/
git clone https://github.com/Arnautovich/Toolbox.git
pip install .
```

## Usage
For an example of the utilisation of each function please refer to the jupyter notebook here [Examples](https://github.com/Arnautovich/Toolbox/blob/main/notebooks/project_report.ipynb)

### Interface
This project also have an interface based UI to interact with the functions. To lunch the interface make sure you installed **streamlit** package or install it by
```
pip install streamlit
```
Then go to the directory where you cloned the repository and lunch the **run.py** file.


## License

This project is licensed under the **MIT License** - see the LICENSE file for details.

## Contact
For any questions or issues, please open an issue on GitHub[![open an issue](https://custom-icon-badges.demolab.com/badge/-Open%20Issue-palegreen?style=for-the-badge&logoColor=black&logo=issue-opened)](https://github.com/Arnautovich/Toolbox/issues)

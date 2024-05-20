# Toolbox [![alt text](https://img.shields.io/badge/Python-14354C?style=for-the-badge&logo=python&logoColor=white)](https://www.python.org)

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
### Distillation
This function is used to determine the number of stages required for the give separtion properties. Example of use:

3 stages

This function calculates the number of stages required for a distillation process based on given separation properties. It also generates a McCabe-Thiele diagram to visually represent the stages.

Parameters:
- F (float): Feed flow rate (mol/hr)
- R (float): Reflux ratio
- z (float): Feed composition (mole fraction)
- q (float): Feed quality (ratio of liquid to total feed)
- alpha (float): Relative volatility
- xD (float): Distillate composition (mole fraction)
- D (float): Distillate flow rate (mol/hr)

Returns:
- nb_stages (int): Number of stages required
- fig (matplotlib.figure.Figure): McCabe-Thiele diagram
Example of Use:
```
from Toolbox.Distillation as distillation

nb_stages, fig = distillation(F=100, R=0.5, z=0.5, q=1, alpha=10, xD=0.9, D=50)

print(f'Number of stages required: {nb_stages}')
```
This example calculates that 3 stages are required for the given distillation process. The following McCabe-Thiele diagram is also generated to help visualize the separation process.



# Optionally, display the McCabe-Thiele diagram
import matplotlib.pyplot as plt
plt.show(fig)
This example calculates that 3 stages are required for the given distillation process. The McCabe-Thiele diagram is also generated to help visualize the separation process.

# Access properties of reactants and products
reactants = stoichiometric_data['reactants']
products = stoichiometric_data['products']
Acid/Base Calculations
To calculate the pH or concentration of acids and bases:

python
Copier le code
from toolbox import acid_base

# Calculate pH of a solution
ph = acid_base.calculate_ph(concentration, acid_constant)

# Calculate concentration of an acid or base
concentration = acid_base.calculate_concentration(ph, acid_constant)
Liquid-Liquid Extraction (LLE)
To calculate the number of stages for LLE processes:

python
Copier le code
from toolbox import lle

# Calculate number of stages for counter-flow LLE
counter_flow_stages = lle.calculate_counter_flow_stages(feed_composition, extract_composition, solvent_composition)

# Calculate number of stages for cross-flow LLE
cross_flow_stages = lle.calculate_cross_flow_stages(feed_composition, extract_composition, solvent_composition)
Documentation

Comprehensive documentation is available here, including detailed descriptions of each function, input parameters, and examples.

Contributing

Contributions are welcome! Please read the contributing guidelines to get started.

License

This project is licensed under the MIT License - see the LICENSE file for details.

Contact

For any questions or issues, please open an issue on GitHub or contact us at support@example.com.

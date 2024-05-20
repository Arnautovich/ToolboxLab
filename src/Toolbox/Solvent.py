def select_solvent(reaction_type, desired_properties, criteria):
    solvents = [
       {"name": "Water", "polarity": 10.2, "boiling_point": 100, "viscosity": 1.0},
        {"name": "Ethanol", "polarity": 4.3, "boiling_point": 78.37, "viscosity": 1.1},
        {"name": "Diethyl ether", "polarity": 2.8, "boiling_point": 34.6, "viscosity":0.224},
        {"name": "Pentane", "polarity": 0.0, "boiling_point": 36.07, "viscosity": 0.23},
        {"name": "1,1,2-Trichlorotrifluoroethane", "polarity": 0.0, "boiling_point": 47.57, "viscosity":0.71},
        {"name": "Cyclopentane", "polarity": 0.1, "boiling_point": 49.26, "viscosity":0.44},
        {"name": "Heptane", "polarity": 0.1, "boiling_point": 98.43, "viscosity": 0.42},
        {"name": "Hexane", "polarity": 0.1, "boiling_point": 68.7, "viscosity": 0.31},
        {"name": "Iso-Octane", "polarity": 0.1, "boiling_point": 99.24, "viscosity": 0.50},
        {"name": "Petroleum Ether", "polarity": 0.1, "boiling_point": 50, "viscosity": 0.46},
        {"name": "Cyclohexane", "polarity": 0.2, "boiling_point": 80.72, "viscosity": 1.0},
        {"name": "n-Butyl Chloride", "polarity": 1.0, "boiling_point": 78.44, "viscosity": 0.45},
        {"name": "Toluene", "polarity": 2.4, "boiling_point": 110.62, "viscosity": 0.59},
        {"name": "Methyl t-Butyl Ether	", "polarity": 2.5, "boiling_point": 55.2, "viscosity": 0.27},
        {"name": "o-Xylene", "polarity": 2.5, "boiling_point": 144.41, "viscosity": 0.81},
        {"name": "Chlorobenzene", "polarity": 2.7, "boiling_point": 131.69, "viscosity": 0.80},
        {"name": "o-Dichlorobenzene", "polarity": 2.7, "boiling_point": 180.48, "viscosity": 1.32},
        {"name": "Ethyl Ether", "polarity": 2.8, "boiling_point": 34.55, "viscosity": 0.24},
        {"name": "Dichloromethane", "polarity": 3.1, "boiling_point": 39.75, "viscosity": 0.44},
        {"name": "Ethylene Dichloride", "polarity": 3.5, "boiling_point": 83.48, "viscosity": 0.79},
        {"name": "n-Butyl Alcohol", "polarity": 3.9, "boiling_point": 117.5, "viscosity": 2.98},
        {"name": "Isopropyl Alcohol", "polarity": 3.9, "boiling_point": 82.26, "viscosity": 2.4},
        {"name": "n-Butyl Acetate", "polarity": 4.0, "boiling_point": 126.11, "viscosity": 0.74},
        {"name": "Isobutyl Alcohol", "polarity": 4.0, "boiling_point": 108, "viscosity": 3.95},
        {"name": "Methyl Isoamyl Ketone", "polarity": 4.0, "boiling_point": 144.9, "viscosity": 0.8},
        {"name": "n-Propyl Alcohol", "polarity": 4.0, "boiling_point": 97.20, "viscosity": 2.3},
        {"name": "Tetrahydrofuran", "polarity": 4.0, "boiling_point": 66, "viscosity": 0.55},
        {"name": "Chloroform", "polarity": 4.1, "boiling_point": 61.15, "viscosity": 0.57},
        {"name": "Methyl Isobutyl Ketone", "polarity": 4.2, "boiling_point": 117.4, "viscosity": 0.58},
        {"name": "Ethyl Acetate", "polarity": 4.4, "boiling_point": 77.11, "viscosity": 0.45},
        {"name": "Methyl n-Propyl Ketone", "polarity": 4.5, "boiling_point": 102.4, "viscosity": 0.51},
        {"name": "Methyl Ethyl Ketone", "polarity": 4.7, "boiling_point": 79.64, "viscosity": 0.43},
        {"name": "1,4-Dioxane", "polarity": 4.8, "boiling_point": 101.32, "viscosity": 1.37},
        {"name": "Methanol", "polarity": 5.1, "boiling_point": 64.7, "viscosity": 0.59},
        {"name": "Acetone", "polarity": 5.1, "boiling_point": 	56.29, "viscosity": 0.36},
        {"name": "Pyridine", "polarity": 5.3, "boiling_point": 115.25, "viscosity": 0.95},
        {"name": "2-Methoxyethanol", "polarity": 5.5, "boiling_point": 124, "viscosity": 1.72},
        {"name": "Acetonitrile", "polarity": 5.8, "boiling_point": 81.60, "viscosity": 0.38},
        {"name": "Propylene Carbonate", "polarity": 6.1, "boiling_point": 241.7, "viscosity": 2.76},
        {"name": "N,N-Dimethylformamide", "polarity": 6.4, "boiling_point": 153.0, "viscosity": 0.92},
        {"name": "Dimethyl Acetamide", "polarity": 6.5, "boiling_point": 166.1, "viscosity": 2.14},
        {"name": "N-Methylpyrrolidone", "polarity": 6.7, "boiling_point": 202, "viscosity": 1.67 },
        {"name": "Dimethyl Sulfoxide", "polarity": 7.2, "boiling_point": 189.0, "viscosity":2.24},
    ]

    # Define weights and thresholds in dictionaries
    weights = {
        "polarity": {0.5: 35, 1: 30, 2: 25, 3: 15, 5: 10, 7: 6, 8: 0},
        "boiling_point": {3: 55, 5: 45, 7: 40, 10: 35, 15: 25, 20: 15, 35: 10, 50: 5, 75: 0},
        "viscosity": {0.2: 25, 0.5: 20, 1: 15, 1.5: 10, 2.5: 5, 3.5: 3, 4: 0}
    }

    scores = []

    for solvent in solvents:
        score = 0

        # Calculate score for each criterion based on the desired combination
        if criteria == "boiling_point_and_polarity":
            for prop, value in desired_properties.items():
                diff = abs(solvent[prop] - value)
                for threshold, weight in weights[prop].items():
                    if diff <= threshold and (prop == "boiling_point" or prop == "polarity"):
                        score += weight
                        break
        elif criteria == "boiling_point_and_viscosity":
            # Adjust this section based on the solubility criterion
            # Example: if solubility is represented by "solubility" property
            for prop, value in desired_properties.items():
                diff = abs(solvent[prop] - value)
                for threshold, weight in weights[prop].items():
                    if diff <= threshold and (prop == "boiling_point" or prop == "viscosity"):
                        score += weight
                        break
        else:
            return "Invalid criteria"

        scores.append((solvent["name"], score))  # Store both solvent name and score as a tuple

    sorted_solvents = sorted(scores, key=lambda x: x[1], reverse=True)
    return sorted_solvents
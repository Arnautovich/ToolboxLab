def select_solvent(reaction_type, boiling_point, polarity, viscosity):
    solvents = [
        {"name": "Water", "polarity": 10.2, "boiling_point": 100, "viscosity": 1.0},
        {"name": "Ethanol", "polarity": 4.3, "boiling_point": 78.37, "viscosity": 1.1},
        {"name": "Diethyl ether", "polarity": 2.8, "boiling_point": 34.6, "viscosity": 0.224},
        {"name": "Pentane", "polarity": 0.0, "boiling_point": 36.07, "viscosity": 0.23},
        {"name": "1,1,2-Trichlorotrifluoroethane", "polarity": 0.0, "boiling_point": 47.57, "viscosity": 0.71},
        {"name": "Cyclopentane", "polarity": 0.1, "boiling_point": 49.26, "viscosity": 0.44},
        {"name": "Heptane", "polarity": 0.1, "boiling_point": 98.43, "viscosity": 0.42},
        {"name": "Hexane", "polarity": 0.1, "boiling_point": 68.7, "viscosity": 0.31},
        {"name": "Iso-Octane", "polarity": 0.1, "boiling_point": 99.24, "viscosity": 0.50},
        {"name": "Petroleum Ether", "polarity": 0.1, "boiling_point": 50, "viscosity": 0.46},
        {"name": "Cyclohexane", "polarity": 0.2, "boiling_point": 80.72, "viscosity": 1.0},
        {"name": "n-Butyl Chloride", "polarity": 1.0, "boiling_point": 78.44, "viscosity": 0.45},
        {"name": "Toluene", "polarity": 2.4, "boiling_point": 110.62, "viscosity": 0.59},
        {"name": "Methyl t-Butyl Ether", "polarity": 2.5, "boiling_point": 55.2, "viscosity": 0.27},
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
        {"name": "Acetone", "polarity": 5.1, "boiling_point": 56.29, "viscosity": 0.36},
        {"name": "Pyridine", "polarity": 5.3, "boiling_point": 115.25, "viscosity": 0.95},
        {"name": "2-Methoxyethanol", "polarity": 5.5, "boiling_point": 124, "viscosity": 1.72},
        {"name": "Acetonitrile", "polarity": 5.8, "boiling_point": 81.60, "viscosity": 0.38},
        {"name": "Propylene Carbonate", "polarity": 6.1, "boiling_point": 241.7, "viscosity": 2.76},
        {"name": "N,N-Dimethylformamide", "polarity": 6.4, "boiling_point": 153.0, "viscosity": 0.92},
        {"name": "Dimethyl Acetamide", "polarity": 6.5, "boiling_point": 166.1, "viscosity": 2.14},
        {"name": "N-Methylpyrrolidone", "polarity": 6.7, "boiling_point": 202, "viscosity": 1.67},
        {"name": "Dimethyl Sulfoxide", "polarity": 7.2, "boiling_point": 189.0, "viscosity": 2.24}
    ]

    desired_properties = {
        "polarity": float(polarity),
        "boiling_point": float(boiling_point),
        "viscosity": float(viscosity)
    }

    weights = {
        "polarity": {0.3: 40, 0.7: 35, 1.2: 30, 2: 25, 3.5: 20, 5: 10, 7: 5},
        "boiling_point": {3: 40, 5: 35, 7: 30, 10: 25, 15: 20, 20: 15, 35: 10, 50: 5, 75: 1},
        "viscosity": {0.2: 35, 0.5: 30, 1: 25, 1.5: 20, 2: 15, 3: 10, 3.5: 5}
    }

    reaction_adjustments = {
        "SN1": {"polarity": 1.6, "boiling_point": 1.3, "viscosity": 1.1},
        "SN2": {"polarity": 1.4, "boiling_point": 1.5, "viscosity": 1.1},
        "Grignard": {"polarity": 1.4, "boiling_point": 1.5, "viscosity": 1.1},
        "Esterification": {"polarity": 1.6, "boiling_point": 1.3, "viscosity": 1.1},
        "Aldol": {"polarity": 1.5, "boiling_point": 1.2, "viscosity": 1.3},
        "Friedel-Crafts": {"polarity": 1.6, "boiling_point": 1.3, "viscosity": 1.1},
        "Hydrogenation": {"polarity": 1.1, "boiling_point": 1.3, "viscosity": 1.6},
        "Oxidation": {"polarity": 1.6, "boiling_point": 1.3, "viscosity": 1.1},
        "Reduction": {"polarity": 1.6, "boiling_point": 1.3, "viscosity": 1.1},
        "Heck": {"polarity": 1.6, "boiling_point": 1.3, "viscosity": 1.1},
        "Suzuki Coupling": {"polarity": 1.6, "boiling_point": 1.3, "viscosity": 1.1},
        "Sonogashira Coupling": {"polarity": 1.6, "boiling_point": 1.3, "viscosity": 1.1},
        "Nitration": {"polarity": 1.6, "boiling_point": 1.3, "viscosity": 1.1},
        "Sulfonation": {"polarity": 1.6, "boiling_point": 1.3, "viscosity": 1.1},
        "Amination": {"polarity": 1.3, "boiling_point": 1.2, "viscosity": 1.5},
        "Michael Addition": {"polarity": 1.5, "boiling_point": 1.2, "viscosity": 1.3},
        "Fischer Esterification": {"polarity": 1.6, "boiling_point": 1.3, "viscosity": 1.1},
        "Buchwald-Hartwig Amination:": {"polarity": 1.6, "boiling_point": 1.3, "viscosity": 1.1},
        "Grignard addition": {"polarity": 1.4, "boiling_point": 1.5, "viscosity": 1.1},
        "Wittig Reaction": {"polarity": 1.6, "boiling_point": 1.3, "viscosity": 1.1},
        "Claisen Condensation": {"polarity": 1.5, "boiling_point": 1.3, "viscosity": 1.2},
        "Cannizzaro Reaction": {"polarity": 1.6, "boiling_point": 1.3, "viscosity": 1.1},
        "Baeyer-Villiger Oxidation": {"polarity": 1.6, "boiling_point": 1.3, "viscosity": 1.1},
        "Polymerization": {"polarity": 1.2, "boiling_point": 1.3, "viscosity": 1.5},
        "Crystallization Reactions": {"polarity": 1.2, "boiling_point": 1.3, "viscosity": 1.5},
        "Enzymatic Reactions:": {"polarity": 1.6, "boiling_point": 1.3, "viscosity": 1.6},
        "Phase Transfer Catalysis:": {"polarity": 1.3, "boiling_point": 1.2, "viscosity": 1.5},
        "Reflux Reactions:": {"polarity": 1.2, "boiling_point": 1.7, "viscosity": 1.1},
        "Distillation": {"polarity": 1.1, "boiling_point": 1.8, "viscosity": 1.1},
        "Knoevenagel Condensation:": {"polarity": 1.2, "boiling_point": 1.6, "viscosity": 1.2},
        "Recrystallization::": {"polarity": 1.3, "boiling_point": 1.6, "viscosity": 1.1},
        "Steam Distillation:": {"polarity": 1.2, "boiling_point": 1.7, "viscosity": 1.1}
       
    }
    
    if reaction_type in reaction_adjustments:
            adjustments = reaction_adjustments[reaction_type]
            for key in weights:
                for threshold in weights[key]:
                    weights[key][threshold] *= adjustments[key]

    scores = []

    for solvent in solvents:
        score = 0

        

        for prop, value in desired_properties.items():
            diff = abs(solvent[prop] - value)
            for threshold, weight in weights[prop].items():
                if diff <= threshold:
                    score += weight
                    break

        scores.append((solvent["name"], score))

    # Sort solvents based on scores
    sorted_solvents = sorted(scores, key=lambda x: x[1], reverse=True)

    return sorted_solvents[:5]

reaction_type = "Recrystallization"
boiling_point = 150
polarity = 6
viscosity = 2.5


top_solvents = select_solvent(reaction_type, boiling_point, polarity, viscosity)
print(f"The top 5 more accurate Solvents for the {reaction_type} reaction with the chosen values for Boiling point, polarity and viscosity are:")
for solvent, score in top_solvents:
    print(f"{solvent}: {score} points")
import unittest
from Toolbox.Solvent import select_solvent
print(select_solvent("Recrystallization", 150, 6, 2.5))
class TestSelectSolvent(unittest.TestCase):

    def test_select_solvent_recrystallization(self):
        # Test for the "Recrystallization" reaction
        reaction_type = "Recrystallization"
        boiling_point = 150
        polarity = 6
        viscosity = 2.5

        top_solvents = select_solvent(reaction_type, boiling_point, polarity, viscosity)

        expected_top_solvents = [
            ("N,N-Dimethylformamide", 90),
            ("Dimethyl Acetamide", 80),
            ("Methyl Isoamyl Ketone", 70),
            ("2-Methoxyethanol", 70),
            ("Propylene Carbonate", 70),
        ]

        self.assertEqual(top_solvents, expected_top_solvents)

    def test_select_solvent_hydrogenation(self):
        # Test for the "Hydrogenation" reaction
        reaction_type = "Hydrogenation"
        boiling_point = 80
        polarity = 1.5
        viscosity = 1.6

        top_solvents = select_solvent(reaction_type, boiling_point, polarity, viscosity)

        expected_top_solvents = [
            ("n-Butyl Chloride", 122.5),
            ("Ethanol", 122.0),
            ("Cyclohexane", 119.5),
            ("Isopropyl Alcohol", 114.0),
            ("Ethylene Dichloride", 113.0)
        ]

        self.assertEqual(top_solvents, expected_top_solvents)

    def test_select_solvent_polymerization(self):
        # Test for the "Polymerization" reaction
        reaction_type = "Polymerization"
        boiling_point = 230
        polarity = 5
        viscosity = 3.1

        top_solvents = select_solvent(reaction_type, boiling_point, polarity, viscosity)

        expected_top_solvents = [
            ("Propylene Carbonate", 107.0),
            ("n-Butyl Alcohol", 88.5),
            ("Isopropyl Alcohol", 73.5),
            ("Isobutyl Alcohol", 73.5),
            ("n-Propyl Alcohol", 73.5)
        ]

        self.assertEqual(top_solvents, expected_top_solvents)

if __name__ == '__main__':
    unittest.main()

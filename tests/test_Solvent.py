import unittest
from Toolbox.Solvent import select_solvent

class TestSelectSolvent(unittest.TestCase):
        
    def test_select_solvent_hydrogenation(self):
        # Test for the "Hydrogenation" reaction
        reaction_type = "Hydrogenation"
        boiling_point = 80
        polarity = 1.5
        viscosity = 1.6

        top_solvents = select_solvent(reaction_type, boiling_point, polarity, viscosity)

        expected_top_solvents = [
            ("n-Butyl Chloride"),
            ("Ethanol"),
            ("Cyclohexane"),
            ("Isopropyl Alcohol"),
            ("Ethylene Dichloride")
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
            ("Propylene Carbonate"),
            ("n-Butyl Alcohol"),
            ("Isopropyl Alcohol"),
            ("Isobutyl Alcohol"),
            ("n-Propyl Alcohol")
        ]

        self.assertEqual(top_solvents, expected_top_solvents)

if __name__ == '__main__':
    unittest.main()

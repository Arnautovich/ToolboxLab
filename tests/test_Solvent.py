import unittest
from Toolbox.Solvent import select_solvent

class TestSelectSolvent(unittest.TestCase):

    def test_select_solvent_recrystallization(self):
        # Test for the "Recrystallization" reaction
        reaction_type = "Recrystallization"
        boiling_point = 150
        polarity = 6
        viscosity = 2.5

        top_solvents = select_solvent(reaction_type, boiling_point, polarity, viscosity)

        expected_top_solvents = [
            ("1,4-Dioxane", 5.6),
            ("N,N-Dimethylformamide", 5.4),
            ("N-Methylpyrrolidone", 5.4),
            ("Dimethyl Sulfoxide", 5.4),
            ("Propylene Carbonate", 5.4)
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
            ("Dimethyl Sulfoxide", 5.4),
            ("Pyridine", 5.2),
            ("Acetonitrile", 5.1),
            ("Tetrahydrofuran", 5.0),
            ("Dimethyl Acetamide", 4.9)
        ]

        self.assertEqual(top_solvents, expected_top_solvents)

    def test_select_solvent_polymerization(self):
        # Test for the "Polymerization" reaction
        reaction_type = "Polymerization"
        boiling_point = 150
        polarity = 1.2
        viscosity = 1.5

        top_solvents = select_solvent(reaction_type, boiling_point, polarity, viscosity)

        expected_top_solvents = [
            ("1,4-Dioxane", 5.6),
            ("N,N-Dimethylformamide", 5.4),
            ("N-Methylpyrrolidone", 5.4),
            ("Dimethyl Sulfoxide", 5.4),
            ("Propylene Carbonate", 5.4)
        ]

        self.assertEqual(top_solvents, expected_top_solvents)

if __name__ == '__main__':
    unittest.main()

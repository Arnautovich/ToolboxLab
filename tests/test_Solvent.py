import unittest
from Toolbox.Solvent import select_solvent

#version chatgpt

class TestSelectSolvent(unittest.TestCase):
    
    def test_sn1_reaction(self):
        result = select_solvent("SN1", 80, 5, 1)
        expected_solvents = ['Methyl Ethyl Ketone', 'Ethanol', 'Ethyl Acetate', 'Acetonitrile', 'Isopropyl Alcohol']
        self.assertEqual(len(result), 5)
        self.assertListEqual([i[0] for i in result], expected_solvents)
        
    def test_grignard_reaction(self):
        result = select_solvent("Grignard", 60, 3, 0.5)
        expected_solvents = ['Chloroform', 'Methyl t-Butyl Ether', 'Tetrahydrofuran', 'Methanol', 'Acetone']
        self.assertEqual(len(result), 5)
        self.assertListEqual([i[0] for i in result], expected_solvents)

    def test_oxidation_reaction(self):
        result = select_solvent("Oxidation", 100, 6, 2)
        expected_solvents = ['n-Propyl Alcohol','1,4-Dioxane',  'Methyl n-Propyl Ketone',  '2-Methoxyethanol',  'Acetonitrile']
        self.assertEqual(len(result), 5)
        self.assertListEqual([i[0] for i in result], expected_solvents)

    def test_invalid_reaction_type(self):
        result = select_solvent("InvalidReaction", 70, 4, 1)
        self.assertEqual(len(result), 5)
        # Check if function returns any valid solvents despite invalid reaction type

    def test_edge_case_boiling_point(self):
        result = select_solvent("SN1", 0, 5, 1)
        expected_solvents =['Pyridine', 'Methanol', '1,4-Dioxane', 'Acetone', 'Methyl Ethyl Ketone']
        self.assertEqual(len(result), 5)
        self.assertListEqual([i[0] for i in result], expected_solvents)
        
    def test_edge_case_polarity(self):
        result = select_solvent("SN1", 80, 0, 1)
        expected_solvents = ['Cyclohexane', 'n-Butyl Chloride', 'Hexane', 'Iso-Octane', 'Heptane']
        self.assertEqual(len(result), 5)
        self.assertListEqual([i[0] for i in result], expected_solvents)
        
    def test_edge_case_viscosity(self):
        result = select_solvent("SN1", 80, 5, 0)
        expected_solvents = ['Methyl Ethyl Ketone', 'Ethyl Acetate', 'Acetonitrile', 'Ethanol', 'Ethylene Dichloride']
        self.assertEqual(len(result), 5)
        self.assertListEqual([i[0] for i in result], expected_solvents)

if __name__ == '__main__':
    unittest.main()
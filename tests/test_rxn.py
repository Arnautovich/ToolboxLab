from Toolbox.chemical_rxn import equation, elements, tokenize, gauss_elimination, permute
import unittest
import numpy as np

class TestStringMethods(unittest.TestCase):
   
    def test_elements(self):
        el = elements('H2O')
        self.assertEqual(el.smile, "O")
        self.assertEqual(float(el.properties["MolecularWeight"]), 18.015)
        self.assertEqual(el.atoms_nb, {'H': 2, 'O': 1})

        with self.assertRaises(TypeError):
            elements(1)

    def test_equation(self):
        eq = equation("NaOH + HCl -> NaCl + H2O")
        self.assertTrue(np.array_equal(eq.stoich_coeff, np.array([1,1,1,1])))

    def test_tokenize(self):
        self.assertEqual(tokenize("NaOH + HCl -> NaCl + H2O"), ['NaOH', '+', 'HCl', '->', 'NaCl', '+', 'H2O'])
        self.assertEqual(tokenize("A + B -> C + D"), ['A', '+', 'B', '->', 'C', '+', 'D'])
        self.assertEqual(tokenize("A + B      ->        C     +     D"), ['A', '+', 'B', '->', 'C', '+', 'D'])

    def test_gauss_elimination(self):
        A = np.array([[1, 2, 3], [10, 5, 6], [2,4,6]])
        B = np.array([0, 0, 0])

        resp = gauss_elimination(A, B)
        true_sol = np.array([0.2, -1.6, 1.])

        close = True

        for i in range(len(resp)):
            if not np.isclose(resp[i], true_sol[i]):
                i = False
                break

        self.assertTrue(close)

    def test_permute(self):
        self.assertTrue(np.array_equal(permute(np.array([[1, 2, 3], [2,4,6], [7,8,9]])), np.array([[7,8,9], [2,4,6], [1, 2, 3]])))


if __name__ == '__main__':
    unittest.main()
    


from Toolbox.chemical_rxn import equation, elements, tokenize, gauss_elimination, permute
from Toolbox.Distillation import distillation, enriching_operating_line, feed_line, stripping_operating_line
from Toolbox.LLE import equilibrium_line, operating_line, lle, LLE_cross_flow
import unittest
import numpy as np

class TestStringMethods(unittest.TestCase):
    def test_lle_cross(self):
        self.assertEqual(LLE_cross_flow(R=100, E=100, x0= 0.018, xN=0.002, y_in=0, kD=1.6)[1], 3)
        self.assertEqual(LLE_cross_flow(R=100, E=10, x0= 0.018, xN=0.002, y_in=0, kD=1.6)[1], 15)
        
        with self.assertRaises(ValueError):
            LLE_cross_flow(R=100, E=100, x0= 1.1, xN=0.002, y_in=0, kD=1.6)
            LLE_cross_flow(R=100, E=100, x0= 0.018, xN=1.1, y_in=0, kD=1.6)
            LLE_cross_flow(R=100, E=100, x0= 0.018, xN=0.002, y_in=1.1, kD=1.6)

        with self.assertRaises(TypeError):
            LLE_cross_flow(R='100', E=100, x0= 0.018, xN=0.002, y_in=0, kD=1.6)
            LLE_cross_flow(R=100, E='100', x0= 0.018, xN=0.002, y_in=0, kD=1.6)
            LLE_cross_flow(R=100, E=100, x0= '0.018', xN=0.002, y_in=0, kD=1.6)
            LLE_cross_flow(R=100, E=100, x0= 0.018, xN='0.002', y_in=0, kD=1.6)
            LLE_cross_flow(R=100, E=100, x0= 0.018, xN=0.002, y_in='0', kD=1.6)
            LLE_cross_flow(R=100, E=100, x0= 0.018, xN=0.002, y_in=0, kD='1.6')


    def test_lle_counter(self):
        self.assertEqual(lle(R=100, E=80, x0= 0.018, xN=0.002, yN_1=0, kD=1.6)[1], 5)
        self.assertEqual(lle(R=100, E=80, x0= 0.02, xN=0.005, yN_1=0.001, kD=1.1)[1], 6)

        with self.assertRaises(ValueError):
            lle(R=100, E=80, x0= 1.1, xN=0.002, yN_1=0, kD=1.6)
            lle(R=100, E=80, x0= 0.018, xN=1.1, yN_1=0, kD=1.6)
            lle(R=100, E=80, x0= 0.018, xN=0.002, yN_1=1.1, kD=1.6)

        with self.assertRaises(TypeError):
            lle(R='100', E=80, x0= 0.018, xN=0.002, yN_1=0, kD=1.6)
            lle(R=100, E='80', x0= 0.018, xN=0.002, yN_1=0, kD=1.6)
            lle(R=100, E=80, x0= '0.018', xN=0.002, yN_1=0, kD=1.6)
            lle(R=100, E=80, x0= 0.018, xN='0.002', yN_1=0, kD=1.6)
            lle(R=100, E=80, x0= 0.018, xN=0.002, yN_1='0', kD=1.6)
            lle(R=100, E=80, x0= 0.018, xN=0.002, yN_1=0, kD='1.6')

    def test_operating_line(self):
        self.assertEqual(operating_line(R=1.5, x=0.5, yN_1=0, E=1, xN=0), 0.75)
        self.assertEqual(operating_line(R=5, x=np.linspace(0,100,1), yN_1=0.1, E=1, xN=0.1), 5*np.linspace(0,100,1)+(0.1-5*0.1))

    def test_equilibrium_line(self):
        self.assertEqual(equilibrium_line(kD=1.5, x=0.5), 0.75)
        self.assertEqual(equilibrium_line(kD=1.5, x=np.linspace(0,100,1)), 1.5*np.linspace(0,100,1))
    

    def test_distillation(self):
        self.assertEqual(distillation(F=100, D=38.89, z=0.5, xD=0.95, xB=0.05, q=0.5, alpha=5, R=1.515)[0], 6)
        self.assertEqual(distillation(z=0.4, xD=0.9, xB=0.1, q=0.5, alpha=5, R=2.5)[0], 4)

        with self.assertRaises(ValueError):
            distillation(F=100, D=38.89, z=0.5, xD=1.1, xB=0.05, q=0.5, alpha=5, R=1.515)
            distillation(F=100, D=38.89, z=1.1, xD=0.9, xB=0.05, q=0.5, alpha=5, R=1.515)
            distillation(F=100, D=38.89, z=0.5, xD=0.9, xB=1.1, q=0.5, alpha=5, R=1.515)
            distillation(F=100, D=38.89, z=0.5, xD=0.9, xB=0.6, q=0.5, alpha=5, R=1.515)
            distillation(F=100, D=38.89, z=0.5, xD=0.9, xB=0.95, q=0.5, alpha=5, R=1.515)
            distillation(F=100, D=38.89, z=0.5, xD=0.2, xB=0.05, q=0.5, alpha=5, R=1.515)
        
        with self.assertRaises(TypeError):
            distillation(F='100', D=38.89, z=0.5, xD=0.95, xB=0.05, q=0.5, alpha=5, R=1.515)
            distillation(F=100, D='38.89', z=0.5, xD=0.95, xB=0.05, q=0.5, alpha=5, R=1.515)
            distillation(F=100, D=38.89, z='0.5', xD=0.95, xB=0.05, q=0.5, alpha=5, R=1.515)
            distillation(F=100, D=38.89, z=0.5, xD='0.95', xB=0.05, q=0.5, alpha=5, R=1.515)
            distillation(F=100, D=38.89, z=0.5, xD=0.95, xB='0.05', q=0.5, alpha=5, R=1.515)
            distillation(F=100, D=38.89, z=0.5, xD=0.95, xB=0.05, q='0.5', alpha=5, R=1.515)
            distillation(F=100, D=38.89, z=0.5, xD=0.95, xB=0.05, q=0.5, alpha='5', R=1.515)
            distillation(F=100, D=38.89, z=0.5, xD=0.95, xB=0.05, q=0.5, alpha=5, R='1.515')
    
    def test_feed_line(self):
        self.assertEqual(feed_line(q=0.5, z=0.5, x=0.5), 0.5)
        self.assertEqual(feed_line(q=0.5, z=0.5, x=np.linspace(0,100,1)), -np.linspace(0,100,1)+1)
    
    def test_stripping_operating_line(self):
        self.assertEqual(stripping_operating_line(R=1.5, xB=0.6, xD=0.5, x_inter=0.5, x=0.5), 0.5)
        self.assertEqual(stripping_operating_line(R=1.5, xB=0.6, xD=0.5, x_inter=0.5, x=np.linspace(0,100,1)), np.linspace(0,100,1))

    def test_enriching_operating_line(self):
        self.assertEqual(enriching_operating_line(R=1.5, x=0.5, xD=0.5), 0.5)
        self.assertEqual(enriching_operating_line(R=1.5, x=np.linspace(0,100,1), xD=0.5), 0.6*np.linspace(0,100,1)+0.2)

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
    


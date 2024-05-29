
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
    


   
if __name__ == '__main__':
    unittest.main()
    


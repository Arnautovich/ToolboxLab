import unittest
from unittest.mock import patch, MagicMock
from Toolbox.Pressure_TB import resolve_name_to_cas, clausius_clapeyron_enthalpy
import chemicals
import numpy as np

class TestResolveNameToCAS(unittest.TestCase):

    @patch('requests.get')
    def test_resolve_name_to_cas(self, mock_get):
        mock_response = MagicMock()
        mock_response.text = 'Result: 64-17-5,'
        mock_get.return_value = mock_response
        
        cas_number = resolve_name_to_cas('Ethanol')

        self.assertEqual(cas_number, '64-17-5')

class TestClausiusClapeyronEnthalpy(unittest.TestCase):

    def test_clausius_clapeyron_enthalpy(self):
        chemicals.reaction.Hfl = MagicMock(return_value=100)  
        chemicals.reaction.Hfg = MagicMock(return_value=200) 
        chemicals.phase_change.Tb = MagicMock(return_value=300)

        result = clausius_clapeyron_enthalpy(0.5, 'Ethanol')

        expected_result = 1 / ((1/300) - (np.log(0.5/1.01325)*8.314/(200-100)))

        self.assertAlmostEqual(result, expected_result)

if __name__ == '__main__':
    unittest.main()

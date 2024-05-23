import unittest
from unittest.mock import patch, MagicMock
from Toolbox.Pressure_TB import resolve_name_to_cas, clausius_clapeyron_enthalpy
import chemicals
import numpy as np

class TestResolveNameToCAS(unittest.TestCase):

    @patch('requests.get')
    def test_resolve_name_to_cas(self, mock_get):
        # Mock the response
        mock_response = MagicMock()
        mock_response.text = 'Result: 64-17-5,'
        mock_get.return_value = mock_response
        
        # Call the function
        cas_number = resolve_name_to_cas('Ethanol')

        # Check if the function returns the correct CAS number
        self.assertEqual(cas_number, '64-17-5')

class TestClausiusClapeyronEnthalpy(unittest.TestCase):

    def test_clausius_clapeyron_enthalpy(self):
        # Provide mock values for the chemical library functions
        chemicals.reaction.Hfl = MagicMock(return_value=100)  # Mock Liquid_heat_compound
        chemicals.reaction.Hfg = MagicMock(return_value=200)  # Mock Gas_heat_compound
        chemicals.phase_change.Tb = MagicMock(return_value=300)  # Mock T

        # Call the function
        result = clausius_clapeyron_enthalpy(0.5, 'Ethanol')

        # Compute the expected result based on the provided mock values
        expected_result = 1 / ((1/300) - (np.log(0.5/1.01325)*8.314/(200-100)))

        # Check if the function returns the correct result
        self.assertAlmostEqual(result, expected_result)

if __name__ == '__main__':
    unittest.main()

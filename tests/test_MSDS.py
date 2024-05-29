import unittest
import requests
from pdf2image import convert_from_bytes
from PIL import Image
from Toolbox.MSDS_2 import resolve_name_to_cas, merge_images_vertically, display_pdf_images

class TestChemistryUtils(unittest.TestCase):

    def test_resolve_name_to_cas(self):
        cas_number = resolve_name_to_cas("water")
        self.assertEqual(cas_number, "7732-18-5")  # Known CAS number for water

    def test_merge_images_vertically(self):
        # Create some sample images
        image1 = Image.new('RGB', (100, 200), color = 'red')
        image2 = Image.new('RGB', (100, 300), color = 'blue')
        
        merged_image = merge_images_vertically([image1, image2])
        
        self.assertEqual(merged_image.size, (100, 500))

    #def test_list_of_succesful_companies(self):
       # companies = list_of_succesful_companies("water")
        # Test for a known company that sells water
       #self.assertIn("Sigma-Aldrich", companies)

    def test_display_pdf_images(self):
    # Fetch and convert the PDF images
        merged_image = display_pdf_images("Benzene", "Sigma-Aldrich")
    
    # Ensure the merged image is not None and is a valid Image object
        self.assertIsNotNone(merged_image)
        self.assertTrue(isinstance(merged_image, Image.Image))
    
    # Check the dimensions and properties of the merged image
    # Since we can't predict the exact size, we check for reasonable dimensions
        width, height = merged_image.size
    
    # Ensure the merged image has a reasonable width and height
    # These values can be adjusted based on expected content, here we assume non-zero dimensions
        self.assertGreater(width, 0)
        self.assertGreater(height, 0)
    
    # Optionally, save the merged image to a file to visually inspect it (useful for debugging)
    # merged_image.save("merged_image_test_output.png")

if __name__ == '__main__':
    unittest.main()

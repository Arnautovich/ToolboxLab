import unittest
import requests
from pdf2image import convert_from_bytes
from PIL import Image
from Toolbox.MSDS_2 import resolve_name_to_cas, merge_images_vertically, display_pdf_images

class TestChemistryUtils(unittest.TestCase):

    def test_resolve_name_to_cas(self):
        cas_number = resolve_name_to_cas("water")
        self.assertEqual(cas_number, "7732-18-5")

    def test_merge_images_vertically(self):
        image1 = Image.new('RGB', (100, 200), color = 'red')
        image2 = Image.new('RGB', (100, 300), color = 'blue')
        
        merged_image = merge_images_vertically([image1, image2])
        
        self.assertEqual(merged_image.size, (100, 500))


    def test_display_pdf_images(self):
        merged_image = display_pdf_images("Benzene", "Sigma-Aldrich")
    
        self.assertIsNotNone(merged_image)
        self.assertTrue(isinstance(merged_image, Image.Image))
    
        width, height = merged_image.size
    
        self.assertGreater(width, 0)
        self.assertGreater(height, 0)
    

if __name__ == '__main__':
    unittest.main()

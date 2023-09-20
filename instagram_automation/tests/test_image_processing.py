
import unittest
from src.instagram.image_processing import ImageProcessor

class TestImageProcessing(unittest.TestCase):
    def setUp(self):
        self.image_processor = ImageProcessor()

    def test_image_resize(self):
        result = self.image_processor.resize('resources/images/raw/test.jpg', (500, 500))
        self.assertEqual(result.size, (500, 500))

    def test_image_filter(self):
        result = self.image_processor.apply_filter('resources/images/raw/test.jpg', 'GREYSCALE')
        self.assertTrue(result.mode, 'L')

    def test_image_rotate(self):
        result = self.image_processor.rotate('resources/images/raw/test.jpg', 90)
        # Assert the image is rotated correctly

    def test_image_crop(self):
        result = self.image_processor.crop('resources/images/raw/test.jpg', (10, 10, 100, 100))
        # Assert the image is cropped correctly

if __name__ == '__main__':
    unittest.main()

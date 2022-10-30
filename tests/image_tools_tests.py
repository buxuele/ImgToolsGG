# -*- coding: UTF-8 -*-
import unittest
from ImgTools import ImageUtils

class ImageTestCase(unittest.TestCase):

    def setUp(self):
        self.tools = ImageUtils("a.jpg")

    def test_name(self):
        """Test 1"""
        result = self.tools.get_image_name()
        self.assertEqual(result, "a.jpg")

if __name__ == '__main__':
    unittest.main()

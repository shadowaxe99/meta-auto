
import unittest
from src.instagram.error_handling import ErrorHandler

class TestErrorHandler(unittest.TestCase):

    def setUp(self):
        self.error_handler = ErrorHandler()

    def test_handle_error(self):
        try:
            raise Exception("Test Exception")
        except Exception as e:
            self.error_handler.handle_error(e)
            self.assertTrue(self.error_handler.error_occurred)
            self.assertEqual(self.error_handler.error_message, "Test Exception")

    def test_reset_error(self):
        self.error_handler.reset_error()
        self.assertFalse(self.error_handler.error_occurred)
        self.assertEqual(self.error_handler.error_message, "")

if __name__ == '__main__':
    unittest.main()


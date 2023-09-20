
import unittest
from src.instagram.logging import Logger

class TestLogging(unittest.TestCase):
    def setUp(self):
        self.logger = Logger()

    def test_log_info(self):
        message = "Test info message"
        self.logger.log_info(message)
        with open('logs/application.log', 'r') as f:
            last_line = f.readlines()[-1]
        self.assertIn(message, last_line)

    def test_log_error(self):
        message = "Test error message"
        self.logger.log_error(message)
        with open('logs/application.log', 'r') as f:
            last_line = f.readlines()[-1]
        self.assertIn(message, last_line)

if __name__ == '__main__':
    unittest.main()

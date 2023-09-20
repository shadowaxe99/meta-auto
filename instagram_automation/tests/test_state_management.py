
import unittest
from src.instagram.state_management import StateManagement

class TestStateManagement(unittest.TestCase):

    def setUp(self):
        self.state_management = StateManagement()

    def test_save_state(self):
        self.state_management.save_state()
        self.assertTrue(self.state_management.state_saved)

    def test_load_state(self):
        self.state_management.save_state()
        self.state_management.load_state()
        self.assertTrue(self.state_management.state_loaded)

    def test_reset_state(self):
        self.state_management.save_state()
        self.state_management.reset_state()
        self.assertTrue(self.state_management.state_reset)

if __name__ == '__main__':
    unittest.main()

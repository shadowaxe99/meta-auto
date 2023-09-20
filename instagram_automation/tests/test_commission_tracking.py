
import unittest
from src.instagram.commission_tracking import CommissionTracking

class TestCommissionTracking(unittest.TestCase):

    def setUp(self):
        self.commission_tracking = CommissionTracking()

    def test_calculate_commission(self):
        result = self.commission_tracking.calculate_commission(1000, 10)
        self.assertEqual(result, 100)

    def test_update_commission(self):
        self.commission_tracking.update_commission(100)
        self.assertEqual(self.commission_tracking.total_commission, 100)

    def test_reset_commission(self):
        self.commission_tracking.reset_commission()
        self.assertEqual(self.commission_tracking.total_commission, 0)

if __name__ == '__main__':
    unittest.main()


import unittest
from src.instagram.direct_messaging_automation import DirectMessagingAutomation

class TestDirectMessagingAutomation(unittest.TestCase):

    def setUp(self):
        self.dma = DirectMessagingAutomation()

    def test_send_message(self):
        self.assertEqual(self.dma.send_message("test_user", "Hello, this is a test message."), "Message sent successfully")

    def test_bulk_send_message(self):
        users = ["test_user1", "test_user2", "test_user3"]
        self.assertEqual(self.dma.bulk_send_message(users, "Hello, this is a test message."), "Messages sent successfully")

    def test_schedule_message(self):
        self.assertEqual(self.dma.schedule_message("test_user", "Hello, this is a test message.", "2022-12-31 23:59"), "Message scheduled successfully")

if __name__ == '__main__':
    unittest.main()


import unittest
from src.instagram.account_management import AccountManagement

class TestAccountManagement(unittest.TestCase):

    def setUp(self):
        self.account_management = AccountManagement()

    def test_login(self):
        self.assertTrue(self.account_management.login('test_username', 'test_password'))

    def test_logout(self):
        self.assertTrue(self.account_management.logout())

    def test_follow_user(self):
        self.assertTrue(self.account_management.follow_user('test_user'))

    def test_unfollow_user(self):
        self.assertTrue(self.account_management.unfollow_user('test_user'))

    def test_post_image(self):
        self.assertTrue(self.account_management.post_image('test_image_path', 'test_caption'))

    def test_delete_post(self):
        self.assertTrue(self.account_management.delete_post('test_post_id'))

    def test_send_direct_message(self):
        self.assertTrue(self.account_management.send_direct_message('test_user', 'test_message'))

    def test_delete_direct_message(self):
        self.assertTrue(self.account_management.delete_direct_message('test_message_id'))

if __name__ == '__main__':
    unittest.main()

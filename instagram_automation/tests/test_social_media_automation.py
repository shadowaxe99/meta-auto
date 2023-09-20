
import unittest
from src.instagram.social_media_automation import SocialMediaAutomation

class TestSocialMediaAutomation(unittest.TestCase):

    def setUp(self):
        self.sma = SocialMediaAutomation()

    def test_post_image(self):
        result = self.sma.post_image('resources/images/processed/test.jpg')
        self.assertTrue(result)

    def test_follow_user(self):
        result = self.sma.follow_user('test_user')
        self.assertTrue(result)

    def test_unfollow_user(self):
        result = self.sma.unfollow_user('test_user')
        self.assertTrue(result)

    def test_like_post(self):
        result = self.sma.like_post('test_post_id')
        self.assertTrue(result)

    def test_unlike_post(self):
        result = self.sma.unlike_post('test_post_id')
        self.assertTrue(result)

    def test_comment_post(self):
        result = self.sma.comment_post('test_post_id', 'Great post!')
        self.assertTrue(result)

if __name__ == '__main__':
    unittest.main()

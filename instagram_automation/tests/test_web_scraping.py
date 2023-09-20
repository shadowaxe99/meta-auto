
import unittest
from src.instagram.web_scraping import WebScraping

class TestWebScraping(unittest.TestCase):

    def setUp(self):
        self.web_scraping = WebScraping()

    def test_scrape_user_profile(self):
        result = self.web_scraping.scrape_user_profile('test_user')
        self.assertIsNotNone(result)

    def test_scrape_post_data(self):
        result = self.web_scraping.scrape_post_data('test_post_id')
        self.assertIsNotNone(result)

    def test_scrape_comments(self):
        result = self.web_scraping.scrape_comments('test_post_id')
        self.assertIsNotNone(result)

    def test_scrape_likes(self):
        result = self.web_scraping.scrape_likes('test_post_id')
        self.assertIsNotNone(result)

if __name__ == '__main__':
    unittest.main()

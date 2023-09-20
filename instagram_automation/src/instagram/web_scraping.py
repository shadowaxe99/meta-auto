
import scrapy
from scrapy.crawler import CrawlerProcess
from instagram_private_api import Client, ClientCompatPatch

class InstagramSpider(scrapy.Spider):
    name = 'instagram'
    start_urls = ['https://www.instagram.com/']

    def __init__(self, username=None, password=None, *args, **kwargs):
        super(InstagramSpider, self).__init__(*args, **kwargs)
        self.api = Client(username, password)

    def parse(self, response):
        for post in response.css('article div div div div a'):
            yield response.follow(post, self.parse_post)

    def parse_post(self, response):
        item = {}
        item['id'] = response.css('::attr(data-shortcode)').get()
        item['likes'] = response.css('section span span::text').get()
        item['comments'] = response.css('ul li span::text').get()
        item['caption'] = response.css('div.C4VMK span::text').get()
        item['image_url'] = response.css('div.KL4Bh img::attr(src)').get()
        yield item

if __name__ == "__main__":
    process = CrawlerProcess()
    process.crawl(InstagramSpider, username='your_username', password='your_password')
    process.start()

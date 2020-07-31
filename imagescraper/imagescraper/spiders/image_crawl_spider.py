import scrapy
import re
from scrapy.linkextractors import LinkExtractor
from scrapy.spiders import CrawlSpider, Rule
from ..items import ImagescraperItem


class ImageCrawlSpiderSpider(CrawlSpider):
    name = "image_crawl_spider"
    allowed_domains = ["books.toscrape.com"]

    def start_requests(self):
        url = "http://books.toscrape.com/"
        yield scrapy.Request(url=url)

    rules = (Rule(LinkExtractor(allow=r"catalogue/"), callback="parse_image", follow=True),)

    def parse_image(self, response):
        if response.xpath('//div[@class="item active"]/img').get() is not None:
            img = response.xpath('//div[@class="item active"]/img/@src').get()
            """
            Computing the Absolute path of the image file.
            "image_urls" require absolute path, not relative path
            """
            m = re.match(r"^(?:../../)(.*)$", img).group(1)
            url = "http://books.toscrape.com/"
            img_url = "".join([url, m])
            image = ImagescraperItem()
            image["image_urls"] = [img_url]  # "image_urls" must be a list
            yield image

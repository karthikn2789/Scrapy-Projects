import scrapy
from scrapy.linkextractors import LinkExtractor
from scrapy.spiders import CrawlSpider, Rule
from ..items import BookstoscrapeItem


class CrawlSpiderSpider(CrawlSpider):
    name = "crawl_spider"
    allowed_domains = ["books.toscrape.com"]
    # start_urls = ["http://books.toscrape.com/"] # when trying to use this, comment start_requests()
    rules = (Rule(LinkExtractor(allow=r"catalogue/"), callback="parse_books", follow=True),)

    def start_requests(self):
        url = "http://books.toscrape.com/"
        yield scrapy.Request(url)

    def parse_books(self, response):
        """ Filtering out pages other than books' pages to avoid getting "NotFound" error.
        Because, other pages would not have any 'div' tag with attribute 'class="col-sm-6 product_main"'
        """
        if response.xpath('//div[@class="col-sm-6 product_main"]').get() is not None:
            title = response.xpath('//div[@class="col-sm-6 product_main"]/h1/text()').get()
            price = response.xpath('//div[@class="col-sm-6 product_main"]/p[@class="price_color"]/text()').get()
            stock = (
                response.xpath('//div[@class="col-sm-6 product_main"]/p[@class="instock availability"]/text()')
                .getall()[-1]
                .strip()
            )
            rating = response.xpath('//div[@class="col-sm-6 product_main"]/p[3]/@class').get()
            # Yielding the extracted data as Item object.
            item = BookstoscrapeItem()
            item["title"] = title
            item["price"] = price
            item["rating"] = rating
            item["availability"] = stock
            yield item

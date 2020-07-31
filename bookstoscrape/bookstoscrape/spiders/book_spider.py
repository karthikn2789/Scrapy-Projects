import scrapy
from ..items import BookstoscrapeItem


class BookSpiderSpider(scrapy.Spider):
    name = "book_spider"
    allowed_domains = ["books.toscrape.com"]

    def start_requests(self):
        urls = ["http://books.toscrape.com/"]
        for url in urls:
            yield scrapy.Request(url=url, callback=self.parse_pages)

    def parse_pages(self, response):
        """
        The purpose of this method is to look for books listing and the link for next page.
        - When it sees books listing, it generates requests with individual book's URL with parse_books()
        as its callback function.
        - When it sees a next page URL, it generates a request for the next page by calling itself
        as the callback function.
        """
        books = response.xpath("//h3")

        """ Using response.urljoin() to get individual book page """
        """
        for book in books:
            book_url = response.urljoin(book.xpath(".//a/@href").get())
            yield scrapy.Request(url=book_url, callback=self.parse_books)
        """

        """ Using response.follow() to get individual book page """
        for book in books:
            yield response.follow(url=book.xpath(".//a/@href").get(), callback=self.parse_books)

        """ Using response. urljoin() to get next page """
        """
        next_page_url = response.xpath('//li[@class="next"]/a/@href').get()
        if next_page_url is not None:
            next_page = response.urljoin(next_page_url)
            yield scrapy.Request(url=next_page, callback=self.parse_pages)
        """

        """ Using response.follow() to get next page """
        next_page_url = response.xpath('//li[@class="next"]/a/@href').get()
        if next_page_url is not None:
            yield response.follow(url=next_page_url, callback=self.parse_pages)

    def parse_books(self, response):
        """
        Method to extract book details and yield it as Item object
        """
        title = response.xpath('//div[@class="col-sm-6 product_main"]/h1/text()').get()
        price = response.xpath('//div[@class="col-sm-6 product_main"]/p[@class="price_color"]/text()').get()
        stock = (
            response.xpath('//div[@class="col-sm-6 product_main"]/p[@class="instock availability"]/text()')
            .getall()[-1]
            .strip()
        )
        rating = response.xpath('//div[@class="col-sm-6 product_main"]/p[3]/@class').get()
        item = BookstoscrapeItem()
        item["title"] = title
        item["price"] = price
        item["rating"] = rating
        item["availability"] = stock
        yield item

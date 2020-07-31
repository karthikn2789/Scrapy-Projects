## Bookstoscrape Scraper

This project demonstrates how Scrapy handles multiple requests and responses by extracting books' details from a dummy online book store books.toscrape.com that is purpose built to practice web scraping. The following book's details would be extracted when this project is executed.  

* Book title
* Price
* Rating
* Availability

This project contains two spiders: [a crawling spider](https://github.com/karthikn2789/Scrapy-Projects/blob/master/bookstoscrape/bookstoscrape/spiders/crawl_spider.py) and [a basic spider](https://github.com/karthikn2789/Scrapy-Projects/blob/master/bookstoscrape/bookstoscrape/spiders/book_spider.py). The end product of these two spiders will be identical. But they differ in how they navigate the website. The crawling spider has built-in methods to navigate webpages, whereas the basic spider needs manual programming to navigate webpages. 

To run the project type the following command from the project's root directory i.e. 'bookstoscrape' directory that contains scrapy.cfg file.

`scrapy crawl crawl_spider -o crawl_spider_output.json` runs the crawling spider and stores the extracted books' details in `crawl_spider_output.json`.

`scrapy crawl book_spider -o book_spider_output.json` runs the basic spider and stores the extracted books' details in `book_spider_output.json`.

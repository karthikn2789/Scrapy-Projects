## Image Scraper

This project demonstrates how Scrapy can be used to scrape images from websites by scraping the cover images of all the books listed in a dummy online book store books.toscrape.com. Image scraping in scrapy is similar to data scraping with just a few lines of code added to `settings.py` file. 

To run the project type the following command from the project's root directory i.e. 'imagescraper' directory that contains scrapy.cfg file.

`scrapy crawl image_crawl_spider -o output.json`

Executing the above command invokes a crawling spider that crawls across the webpages of books.toscrape.com and downloads all the cover pages to images/full folder under the root directory. `output.json` file contains details of each image downloaded from the website.

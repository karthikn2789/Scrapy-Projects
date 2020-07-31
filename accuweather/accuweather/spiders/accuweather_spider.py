import scrapy
import re
from ..items import AccuweatherItem


class AccuweatherSpiderSpider(scrapy.Spider):
    name = "accuweather_spider"
    allowed_domains = ["accuweather.com"]

    def start_requests(self):
        # Accuweather URL for Chennai's weather
        urls = ["https://www.accuweather.com/en/in/chennai/206671/weather-forecast/206671"]
        for url in urls:
            yield scrapy.Request(url=url, callback=self.parse_url)

    def parse_url(self, response):
        # Extracting city, temperature, air quality and condition from the response using XPath
        city = response.xpath('//h1[@class="header-loc"]/text()').get()
        temp = response.xpath('//div[@class="temp"]/text()').get()
        air_quality = response.xpath(
            '//div[@class="spaced-content detail"]/span[text()="Air Quality"]/following-sibling::span[1]/text()'
        ).get()
        cond = response.xpath('//span[@class="phrase"]/text()').get()
        temp = re.match(r"(\d+)", temp).group(1) + " C"  # Removing the degree symbol and adding C
        # Yielding the extracted data as Item object. You may also extract as Dictionary
        item = AccuweatherItem()
        item["city"] = city
        item["temp"] = temp
        item["air_quality"] = air_quality
        item["cond"] = cond
        yield item

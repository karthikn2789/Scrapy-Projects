# Define here the models for your scraped items
#
# See documentation in:
# https://docs.scrapy.org/en/latest/topics/items.html

import scrapy


class WeatherItem(scrapy.Item):
    city = scrapy.Field()
    temp = scrapy.Field()
    air_quality = scrapy.Field()
    cond = scrapy.Field()

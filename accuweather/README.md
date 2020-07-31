## Accuweather Scraper

This project demonstrates how Scrapy handles a single request and response by extracting 'Chennai' city's weather report from [accuweather.com](https://www.accuweather.com/en/in/chennai/206671/weather-forecast/206671).

To run the project type the following command from the project's root directory i.e. 'accuweather' directory that contains scrapy.cfg file.

`scrapy crawl accuweather_spider -o output.json`

This command invokes the spider named `accuweather_spider` in this project, crawls the webpage containing Chennai's weather, extracts city name, temperature, air quality, condition and exports it to `output.json` file.
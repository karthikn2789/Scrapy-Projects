## Weather.com Scraper

This project demonstrates how Scrapy handles a single request and response by extracting 'Chennai' city's weather report from [weather.com](https://weather.com/en-IN/weather/today/l/bf01d09009561812f3f95abece23d16e123d8c08fd0b8ec7ffc9215c0154913c).

To run the project type the following command from the project's root directory i.e. 'weather' directory that contains scrapy.cfg file.

`scrapy crawl weather_spider -o output.json`

This command invokes the spider named `weather_spider` in this project, crawls the webpage containing Chennai's weather, extracts city name, temperature, air quality, condition and exports it to `output.json` file.
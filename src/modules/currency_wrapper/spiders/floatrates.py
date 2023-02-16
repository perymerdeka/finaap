import scrapy
import json

# from scrapy.http.response import Response

class FloatratesSpider(scrapy.Spider):
    name = "floatrates"
    allowed_domains = ["floatrates.com"]
    start_urls = ["http://www.floatrates.com/daily/usd.json"]

    def parse(self, response):
        json_res = response.json()

        for key, val in json_res:
            print(key)

        # print(json_res)
        return json_res

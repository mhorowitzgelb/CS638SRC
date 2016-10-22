from scrapy.contrib.spiders import CrawlSpider, Rule
from scrapy.contrib.linkextractors.sgml import SgmlLinkExtractor
from scrapy.selector import HtmlXPathSelector
from scrapy.http import Request
from tutorial.items import UsedCar

from selenium import selenium

class CarmaxSpider(CrawlSpider):
    name = "carmax"
    start_urls = ["http://madison.craigslist.org/search/ctd"]



    def parse(self, response):
        for price in response.xpath("//span[@class='price']/text()").extract():
            item = UsedCar()
            item['name'] = 'car'
            item['cost'] = price
            yield item
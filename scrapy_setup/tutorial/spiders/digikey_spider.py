import scrapy
from tutorial.items import Digikey

class DigikeySpider(scrapy.Spider):
    name = 'digikey'
    start_urls = ['http://www.digikey.com/product-search/en',]

    def parse(self,response):
        for subgroup in response.xpath("//ul[@class='catfiltersub']"):
            for subsubgroup in subgroup.xpath('li'):
                next_page = subsubgroup.xpath('a/@href').extract_first()
                if next_page:
                    next_page = response.urljoin(next_page)
                    yield scrapy.Request(next_page, callback=self.parseSubPage)

    def parseSubPage(self, response):
        for row in response.xpath(
                "//table[@id='productTable']/tbody/tr/td[@class='tr-description']/text()").extract():
            item = Digikey()
            item['desc'] = row
            yield item
        next_page = response.xpath("//a[@class='Next']/@href").extract_first()
        if next_page:
            next_page = response.urljoin(next_page)
            yield scrapy.Request(next_page, callback=self.parseSubPage)


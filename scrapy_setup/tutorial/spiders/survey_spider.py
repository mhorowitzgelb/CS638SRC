import scrapy
from tutorial.items import QuoteItem

class SurveySpider(scrapy.Spider):
    name = 'survey'
    start_urls = [
        'http://factfinder.census.gov/faces/tableservices/jsf/pages/productview.xhtml?src=bkmk',
    ]

    def parse(self,response):
        for total in response.xpath("//table[@id='data']"):
            print "found"

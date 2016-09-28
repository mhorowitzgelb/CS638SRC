import scrapy
from tutorial.items import QuoteItem

class QuotesSpider(scrapy.Spider):
    name = 'quotes'
    start_urls = [
        'http://quotes.toscrape.com/page/1/',
    ]

    def parse(self,response):
        for quote in response.xpath("//div[@class='quote']"):
            item = QuoteItem()
            item['text'] = quote.xpath("span[@class='text']/text()").extract_first()
            item['author'] = quote.xpath("span/small/text()").extract_first()
            yield item
        next_page = response.xpath("//li[@class='next']/a/@href").extract_first()
        if next_page:
            next_page = response.urljoin(next_page)
            yield scrapy.Request(next_page, callback=self.parse)

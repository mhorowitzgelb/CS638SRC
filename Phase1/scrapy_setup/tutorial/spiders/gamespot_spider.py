import scrapy
from tutorial.items import GamespotReview

class DigikeySpider(scrapy.Spider):
    name = 'gamespot'
    start_urls = ['http://www.ign.com/games/reviews?platformSlug=xbox-one&startIndex=150',]

    def parse(self,response):
        for article in response.xpath("//div[@id='item-list']/div[@class='itemList']/div"):
            item  = GamespotReview()
            item["title"] =  article.xpath("div[@class='up-com grid_7']/div[@class='item-title']/h3/a/text()").extract_first()
            item["score"] = article.xpath("div[@class='releaseDate grid_3 omega']/div/a/span[@class='scoreBox-score']/text()").extract_first()

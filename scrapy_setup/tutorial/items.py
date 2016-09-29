import scrapy

class QuoteItem(scrapy.Item):
	text = scrapy.Field()
	author = scrapy.Field()

class Digikey(scrapy.Item):
	desc = scrapy.Field()

class GamespotReview(scrapy.Item):
	title = scrapy.Field();
	score = scrapy.Field();

class UsedCar(scrapy.Item):
	name = scrapy.Field()
	cost = scrapy.Field()

class ComputerPart(scrapy.Item):
	name = scrapy.Field()
	model = scrapy.Field()
	brand = scrapy.Field()
	price = scrapy.Field()
	rating = scrapy.Field()
	energy_rating = scrapy.Field()
	max_power = scrapy.Field()
	weight = scrapy.Field()
	modular = scrapy.Field()

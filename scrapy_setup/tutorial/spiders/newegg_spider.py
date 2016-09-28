import scrapy
from tutorial.items import ComputerPart
class NewEggSpider(scrapy.Spider):
    name = 'newegg'
    start_urls =['http://www.newegg.com/Product/Product.aspx?Item=N82E16817139142']

    def parse(selfs, response):
        item = ComputerPart()

        name = response.xpath("//div[@class='grpArticle']/div/div[2]/h1/span/text()").extract_first()
        name = ' '.join(name.split())

        brand = response.xpath("//div[@id='Specs']/fieldset/dl/dd[../dt/text()='Brand']/text()").extract_first()
        brand = ' '.join(brand.split())

        model = response.xpath("//div[@id='Specs']/fieldset/dl/dd[../dt/text()='Model']/text()").extract_first()
        model = ' '.join(model.split())

        rating = response.xpath("//div[@class='grpArticle']/div/div[@class='grpRating']/a/span[@itemprop='ratingValue']/@content").extract_first()

        price = response.xpath("//div[@itemprop='offers']/meta[@itemprop='price']/@content").extract_first()

        max_watts = response.xpath("//div[@id='Specs']/fieldset/dl/dd[../dt/a/text()='Maximum Power']/text()").extract_first()
        max_watts = ' '.join(max_watts.split())

        modular = response.xpath("//div[@id='Specs']/fieldset/dl/dd[../dt/a/text()='Modular']/text()").extract_first()
        modular = ' '.join(modular.split())

        energy_rating = response.xpath("//div[@id='Specs']/fieldset/dl/dd[../dt/text()='Energy-Efficient']/text()").extract_first()
        energy_rating = ' '.join(energy_rating.split())

        weight = response.xpath("//div[@id='Specs']/fieldset/dl/dd[../dt/text()='Weight']/text()").extract_first()

        item['name'] = name
        item['brand'] = brand
        item['model'] = model
        item['rating'] = rating
        item['price'] = price
        item['weight'] = weight
        item['modular'] = modular
        item['energy_rating'] = energy_rating
        item['max_power'] = max_watts

        print item

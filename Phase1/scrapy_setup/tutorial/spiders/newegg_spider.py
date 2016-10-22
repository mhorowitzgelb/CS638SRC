import scrapy
import random
from tutorial.items import ComputerPart
class NewEggSpider(scrapy.Spider):
    name = 'newegg'
    start_urls =["http://www.newegg.com/Desktop-Graphics-Cards/SubCategory/ID-48/Page-1?PageSize=36&order=BESTMATCH"
,"http://www.newegg.com/Desktop-Graphics-Cards/SubCategory/ID-48/Page-2?PageSize=36&order=BESTMATCH"
,"http://www.newegg.com/Desktop-Graphics-Cards/SubCategory/ID-48/Page-3?PageSize=36&order=BESTMATCH"
,"http://www.newegg.com/Desktop-Graphics-Cards/SubCategory/ID-48/Page-4?PageSize=36&order=BESTMATCH"
,"http://www.newegg.com/Desktop-Graphics-Cards/SubCategory/ID-48/Page-5?PageSize=36&order=BESTMATCH"
,"http://www.newegg.com/Desktop-Graphics-Cards/SubCategory/ID-48/Page-6?PageSize=36&order=BESTMATCH"
,"http://www.newegg.com/Desktop-Graphics-Cards/SubCategory/ID-48/Page-7?PageSize=36&order=BESTMATCH"
,"http://www.newegg.com/Desktop-Graphics-Cards/SubCategory/ID-48/Page-8?PageSize=36&order=BESTMATCH"
,"http://www.newegg.com/Desktop-Graphics-Cards/SubCategory/ID-48/Page-9?PageSize=36&order=BESTMATCH"
,"http://www.newegg.com/Desktop-Graphics-Cards/SubCategory/ID-48/Page-10?PageSize=36&order=BESTMATCH"
,"http://www.newegg.com/Desktop-Graphics-Cards/SubCategory/ID-48/Page-11?PageSize=36&order=BESTMATCH"
,"http://www.newegg.com/Desktop-Graphics-Cards/SubCategory/ID-48/Page-12?PageSize=36&order=BESTMATCH"
,"http://www.newegg.com/Desktop-Graphics-Cards/SubCategory/ID-48/Page-13?PageSize=36&order=BESTMATCH"
,"http://www.newegg.com/Desktop-Graphics-Cards/SubCategory/ID-48/Page-14?PageSize=36&order=BESTMATCH"
,"http://www.newegg.com/Desktop-Graphics-Cards/SubCategory/ID-48/Page-15?PageSize=36&order=BESTMATCH"
,"http://www.newegg.com/Desktop-Graphics-Cards/SubCategory/ID-48/Page-16?PageSize=36&order=BESTMATCH"
,"http://www.newegg.com/Desktop-Graphics-Cards/SubCategory/ID-48/Page-17?PageSize=36&order=BESTMATCH"
,"http://www.newegg.com/Desktop-Graphics-Cards/SubCategory/ID-48/Page-18?PageSize=36&order=BESTMATCH"
,"http://www.newegg.com/Desktop-Graphics-Cards/SubCategory/ID-48/Page-19?PageSize=36&order=BESTMATCH"
,"http://www.newegg.com/Desktop-Graphics-Cards/SubCategory/ID-48/Page-20?PageSize=36&order=BESTMATCH"
,"http://www.newegg.com/Desktop-Graphics-Cards/SubCategory/ID-48/Page-21?PageSize=36&order=BESTMATCH"
,"http://www.newegg.com/Desktop-Graphics-Cards/SubCategory/ID-48/Page-22?PageSize=36&order=BESTMATCH"
,"http://www.newegg.com/Desktop-Graphics-Cards/SubCategory/ID-48/Page-23?PageSize=36&order=BESTMATCH"
,"http://www.newegg.com/Desktop-Graphics-Cards/SubCategory/ID-48/Page-24?PageSize=36&order=BESTMATCH"
,"http://www.newegg.com/Desktop-Graphics-Cards/SubCategory/ID-48/Page-25?PageSize=36&order=BESTMATCH"
,"http://www.newegg.com/Desktop-Graphics-Cards/SubCategory/ID-48/Page-26?PageSize=36&order=BESTMATCH"
,"http://www.newegg.com/Desktop-Graphics-Cards/SubCategory/ID-48/Page-27?PageSize=36&order=BESTMATCH"
,"http://www.newegg.com/Desktop-Graphics-Cards/SubCategory/ID-48/Page-28?PageSize=36&order=BESTMATCH"
,"http://www.newegg.com/Desktop-Graphics-Cards/SubCategory/ID-48/Page-29?PageSize=36&order=BESTMATCH"
,"http://www.newegg.com/Desktop-Graphics-Cards/SubCategory/ID-48/Page-30?PageSize=36&order=BESTMATCH"
,"http://www.newegg.com/Desktop-Graphics-Cards/SubCategory/ID-48/Page-31?PageSize=36&order=BESTMATCH"
,"http://www.newegg.com/Desktop-Graphics-Cards/SubCategory/ID-48/Page-32?PageSize=36&order=BESTMATCH"
,"http://www.newegg.com/Desktop-Graphics-Cards/SubCategory/ID-48/Page-33?PageSize=36&order=BESTMATCH"
,"http://www.newegg.com/Desktop-Graphics-Cards/SubCategory/ID-48/Page-34?PageSize=36&order=BESTMATCH"
,"http://www.newegg.com/Desktop-Graphics-Cards/SubCategory/ID-48/Page-35?PageSize=36&order=BESTMATCH"
,"http://www.newegg.com/Desktop-Graphics-Cards/SubCategory/ID-48/Page-36?PageSize=36&order=BESTMATCH"
,"http://www.newegg.com/Desktop-Graphics-Cards/SubCategory/ID-48/Page-37?PageSize=36&order=BESTMATCH"
,"http://www.newegg.com/Desktop-Graphics-Cards/SubCategory/ID-48/Page-38?PageSize=36&order=BESTMATCH"
,"http://www.newegg.com/Desktop-Graphics-Cards/SubCategory/ID-48/Page-39?PageSize=36&order=BESTMATCH"
,"http://www.newegg.com/Desktop-Graphics-Cards/SubCategory/ID-48/Page-40?PageSize=36&order=BESTMATCH"
,"http://www.newegg.com/Desktop-Graphics-Cards/SubCategory/ID-48/Page-41?PageSize=36&order=BESTMATCH"
,"http://www.newegg.com/Desktop-Graphics-Cards/SubCategory/ID-48/Page-42?PageSize=36&order=BESTMATCH"
,"http://www.newegg.com/Desktop-Graphics-Cards/SubCategory/ID-48/Page-43?PageSize=36&order=BESTMATCH"
,"http://www.newegg.com/Desktop-Graphics-Cards/SubCategory/ID-48/Page-44?PageSize=36&order=BESTMATCH"]

    def parse(self, response):
        for itemDom in response.xpath("//div[@class='items-view is-grid']/div[@class='item-container ']"):

            rating = itemDom.xpath("div/div[@class='item-branding']/a[@class='item-rating']/@title").extract_first()

            next_page = itemDom.xpath("a/@href").extract_first()

            item = ComputerPart()
            item['rating'] = rating

            if(next_page):
                next_page = response.urljoin(next_page)
                request = scrapy.Request(next_page, callback=self.parse_product_page)
                request.meta['item'] = item
                yield request
        '''
        if "page" in response.meta:
            page_num = response.meta['page']
        else:
            page_num = 1
        page_num = page_num + 1

        if page_num <= 2:
            next_page = "http://www.newegg.com/Power-Supplies/SubCategory/ID-58/Page-{0}?PageSize=36&order=BESTMATCH".format(page_num)
            next_page = response.urljoin(next_page)
            request = scrapy.Request(next_page, callback=self.parse)
            request.meta['page'] = page_num
            yield request
        '''

    def parse_product_page(self,response):
        item = response.meta['item']

        name = response.xpath("//div[@class='grpArticle']/div/div[2]/h1/span/text()").extract_first()
        if name:
            name = ' '.join(name.split())

        brand = response.xpath("//div[@id='Specs']/fieldset/dl/dd[../dt/text()='Brand']/text()").extract_first()
        if brand:
            brand = ' '.join(brand.split())

        model = response.xpath("//div[@id='Specs']/fieldset/dl/dd[../dt/text()='Model']/text()").extract_first()
        if model:
            model = ' '.join(model.split())


        price = response.xpath("//div[@itemprop='offers']/meta[@itemprop='price']/@content").extract_first()

        max_watts = response.xpath("//div[@id='Specs']/fieldset/dl/dd[../dt/a/text()='Maximum Power']/text()").extract_first()
        if max_watts:
            max_watts = ' '.join(max_watts.split())

        modular = response.xpath("//div[@id='Specs']/fieldset/dl/dd[../dt/a/text()='Modular']/text()").extract_first()
        if modular:
            modular = ' '.join(modular.split())

        energy_rating = response.xpath("//div[@id='Specs']/fieldset/dl/dd[../dt/text()='Energy-Efficient']/text()").extract_first()
        if energy_rating:
            energy_rating = ' '.join(energy_rating.split())

        weight = response.xpath("//div[@id='Specs']/fieldset/dl/dd[../dt/text()='Weight']/text()").extract_first()

        item['name'] = name
        item['brand'] = brand
        item['model'] = model
        item['price'] = price
        item['weight'] = weight
        item['modular'] = modular
        item['energy_rating'] = energy_rating
        item['max_power'] = max_watts
        if model:
            fname = model
        else:
            return item

        f = open("/home/max/CS638SRC/data/{0}{1}.html".format(fname,random.randint(0,9)),'w')
        f.write(response.body)
        f.close()
        return item


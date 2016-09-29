import scrapy
from tutorial.items import ComputerPart
class NewEggSpider(scrapy.Spider):
    name = 'newegg'
    start_urls =["http://www.newegg.com/Power-Supplies/SubCategory/ID-58/Page-1?PageSize=36&order=BESTMATCH"
,"http://www.newegg.com/Power-Supplies/SubCategory/ID-58/Page-2?PageSize=36&order=BESTMATCH"
,"http://www.newegg.com/Power-Supplies/SubCategory/ID-58/Page-3?PageSize=36&order=BESTMATCH"
,"http://www.newegg.com/Power-Supplies/SubCategory/ID-58/Page-4?PageSize=36&order=BESTMATCH"
,"http://www.newegg.com/Power-Supplies/SubCategory/ID-58/Page-5?PageSize=36&order=BESTMATCH"
,"http://www.newegg.com/Power-Supplies/SubCategory/ID-58/Page-6?PageSize=36&order=BESTMATCH"
,"http://www.newegg.com/Power-Supplies/SubCategory/ID-58/Page-7?PageSize=36&order=BESTMATCH"
,"http://www.newegg.com/Power-Supplies/SubCategory/ID-58/Page-8?PageSize=36&order=BESTMATCH"
,"http://www.newegg.com/Power-Supplies/SubCategory/ID-58/Page-9?PageSize=36&order=BESTMATCH"
,"http://www.newegg.com/Power-Supplies/SubCategory/ID-58/Page-10?PageSize=36&order=BESTMATCH"
,"http://www.newegg.com/Power-Supplies/SubCategory/ID-58/Page-11?PageSize=36&order=BESTMATCH"
,"http://www.newegg.com/Power-Supplies/SubCategory/ID-58/Page-12?PageSize=36&order=BESTMATCH"
,"http://www.newegg.com/Power-Supplies/SubCategory/ID-58/Page-13?PageSize=36&order=BESTMATCH"
,"http://www.newegg.com/Power-Supplies/SubCategory/ID-58/Page-14?PageSize=36&order=BESTMATCH"
,"http://www.newegg.com/Power-Supplies/SubCategory/ID-58/Page-15?PageSize=36&order=BESTMATCH"
,"http://www.newegg.com/Power-Supplies/SubCategory/ID-58/Page-16?PageSize=36&order=BESTMATCH"
,"http://www.newegg.com/Power-Supplies/SubCategory/ID-58/Page-17?PageSize=36&order=BESTMATCH"
,"http://www.newegg.com/Power-Supplies/SubCategory/ID-58/Page-18?PageSize=36&order=BESTMATCH"
,"http://www.newegg.com/Power-Supplies/SubCategory/ID-58/Page-19?PageSize=36&order=BESTMATCH"
,"http://www.newegg.com/Power-Supplies/SubCategory/ID-58/Page-20?PageSize=36&order=BESTMATCH"
,"http://www.newegg.com/Power-Supplies/SubCategory/ID-58/Page-21?PageSize=36&order=BESTMATCH"
,"http://www.newegg.com/Power-Supplies/SubCategory/ID-58/Page-22?PageSize=36&order=BESTMATCH"
,"http://www.newegg.com/Power-Supplies/SubCategory/ID-58/Page-23?PageSize=36&order=BESTMATCH"
,"http://www.newegg.com/Power-Supplies/SubCategory/ID-58/Page-24?PageSize=36&order=BESTMATCH"
,"http://www.newegg.com/Power-Supplies/SubCategory/ID-58/Page-25?PageSize=36&order=BESTMATCH"
,"http://www.newegg.com/Power-Supplies/SubCategory/ID-58/Page-26?PageSize=36&order=BESTMATCH"
,"http://www.newegg.com/Power-Supplies/SubCategory/ID-58/Page-27?PageSize=36&order=BESTMATCH"
,"http://www.newegg.com/Power-Supplies/SubCategory/ID-58/Page-28?PageSize=36&order=BESTMATCH"
,"http://www.newegg.com/Power-Supplies/SubCategory/ID-58/Page-29?PageSize=36&order=BESTMATCH"
,"http://www.newegg.com/Power-Supplies/SubCategory/ID-58/Page-30?PageSize=36&order=BESTMATCH"
,"http://www.newegg.com/Power-Supplies/SubCategory/ID-58/Page-31?PageSize=36&order=BESTMATCH"
,"http://www.newegg.com/Power-Supplies/SubCategory/ID-58/Page-32?PageSize=36&order=BESTMATCH"
,"http://www.newegg.com/Power-Supplies/SubCategory/ID-58/Page-33?PageSize=36&order=BESTMATCH"
,"http://www.newegg.com/Power-Supplies/SubCategory/ID-58/Page-34?PageSize=36&order=BESTMATCH"
,"http://www.newegg.com/Power-Supplies/SubCategory/ID-58/Page-35?PageSize=36&order=BESTMATCH"
,"http://www.newegg.com/Power-Supplies/SubCategory/ID-58/Page-36?PageSize=36&order=BESTMATCH"
,"http://www.newegg.com/Power-Supplies/SubCategory/ID-58/Page-37?PageSize=36&order=BESTMATCH"
,"http://www.newegg.com/Power-Supplies/SubCategory/ID-58/Page-38?PageSize=36&order=BESTMATCH"
,"http://www.newegg.com/Power-Supplies/SubCategory/ID-58/Page-39?PageSize=36&order=BESTMATCH"
,"http://www.newegg.com/Power-Supplies/SubCategory/ID-58/Page-40?PageSize=36&order=BESTMATCH"
,"http://www.newegg.com/Power-Supplies/SubCategory/ID-58/Page-41?PageSize=36&order=BESTMATCH"
,"http://www.newegg.com/Power-Supplies/SubCategory/ID-58/Page-42?PageSize=36&order=BESTMATCH"
,"http://www.newegg.com/Power-Supplies/SubCategory/ID-58/Page-43?PageSize=36&order=BESTMATCH"
,"http://www.newegg.com/Power-Supplies/SubCategory/ID-58/Page-44?PageSize=36&order=BESTMATCH"
,"http://www.newegg.com/Power-Supplies/SubCategory/ID-58/Page-45?PageSize=36&order=BESTMATCH"
,"http://www.newegg.com/Power-Supplies/SubCategory/ID-58/Page-46?PageSize=36&order=BESTMATCH"
,"http://www.newegg.com/Power-Supplies/SubCategory/ID-58/Page-47?PageSize=36&order=BESTMATCH"
,"http://www.newegg.com/Power-Supplies/SubCategory/ID-58/Page-48?PageSize=36&order=BESTMATCH"
,"http://www.newegg.com/Power-Supplies/SubCategory/ID-58/Page-49?PageSize=36&order=BESTMATCH"
,"http://www.newegg.com/Power-Supplies/SubCategory/ID-58/Page-50?PageSize=36&order=BESTMATCH"
,"http://www.newegg.com/Power-Supplies/SubCategory/ID-58/Page-51?PageSize=36&order=BESTMATCH"
,"http://www.newegg.com/Power-Supplies/SubCategory/ID-58/Page-52?PageSize=36&order=BESTMATCH"
,"http://www.newegg.com/Power-Supplies/SubCategory/ID-58/Page-53?PageSize=36&order=BESTMATCH"
,"http://www.newegg.com/Power-Supplies/SubCategory/ID-58/Page-54?PageSize=36&order=BESTMATCH"
,"http://www.newegg.com/Power-Supplies/SubCategory/ID-58/Page-55?PageSize=36&order=BESTMATCH"
,"http://www.newegg.com/Power-Supplies/SubCategory/ID-58/Page-56?PageSize=36&order=BESTMATCH"
,"http://www.newegg.com/Power-Supplies/SubCategory/ID-58/Page-57?PageSize=36&order=BESTMATCH"
,"http://www.newegg.com/Power-Supplies/SubCategory/ID-58/Page-58?PageSize=36&order=BESTMATCH"
,"http://www.newegg.com/Power-Supplies/SubCategory/ID-58/Page-59?PageSize=36&order=BESTMATCH"
,"http://www.newegg.com/Power-Supplies/SubCategory/ID-58/Page-60?PageSize=36&order=BESTMATCH"
,"http://www.newegg.com/Power-Supplies/SubCategory/ID-58/Page-61?PageSize=36&order=BESTMATCH"
,"http://www.newegg.com/Power-Supplies/SubCategory/ID-58/Page-62?PageSize=36&order=BESTMATCH"
,"http://www.newegg.com/Power-Supplies/SubCategory/ID-58/Page-63?PageSize=36&order=BESTMATCH"
,"http://www.newegg.com/Power-Supplies/SubCategory/ID-58/Page-64?PageSize=36&order=BESTMATCH"
,"http://www.newegg.com/Power-Supplies/SubCategory/ID-58/Page-65?PageSize=36&order=BESTMATCH"
,"http://www.newegg.com/Power-Supplies/SubCategory/ID-58/Page-66?PageSize=36&order=BESTMATCH"
,"http://www.newegg.com/Power-Supplies/SubCategory/ID-58/Page-67?PageSize=36&order=BESTMATCH"
,"http://www.newegg.com/Power-Supplies/SubCategory/ID-58/Page-68?PageSize=36&order=BESTMATCH"
,"http://www.newegg.com/Power-Supplies/SubCategory/ID-58/Page-69?PageSize=36&order=BESTMATCH"
,"http://www.newegg.com/Power-Supplies/SubCategory/ID-58/Page-70?PageSize=36&order=BESTMATCH"
,"http://www.newegg.com/Power-Supplies/SubCategory/ID-58/Page-71?PageSize=36&order=BESTMATCH"
,"http://www.newegg.com/Power-Supplies/SubCategory/ID-58/Page-72?PageSize=36&order=BESTMATCH"
,"http://www.newegg.com/Power-Supplies/SubCategory/ID-58/Page-73?PageSize=36&order=BESTMATCH"
,"http://www.newegg.com/Power-Supplies/SubCategory/ID-58/Page-74?PageSize=36&order=BESTMATCH"
,"http://www.newegg.com/Power-Supplies/SubCategory/ID-58/Page-75?PageSize=36&order=BESTMATCH"
,"http://www.newegg.com/Power-Supplies/SubCategory/ID-58/Page-76?PageSize=36&order=BESTMATCH"
,"http://www.newegg.com/Power-Supplies/SubCategory/ID-58/Page-77?PageSize=36&order=BESTMATCH"
,"http://www.newegg.com/Power-Supplies/SubCategory/ID-58/Page-78?PageSize=36&order=BESTMATCH"
,"http://www.newegg.com/Power-Supplies/SubCategory/ID-58/Page-79?PageSize=36&order=BESTMATCH"
,"http://www.newegg.com/Power-Supplies/SubCategory/ID-58/Page-80?PageSize=36&order=BESTMATCH"
,"http://www.newegg.com/Power-Supplies/SubCategory/ID-58/Page-81?PageSize=36&order=BESTMATCH"
,"http://www.newegg.com/Power-Supplies/SubCategory/ID-58/Page-82?PageSize=36&order=BESTMATCH"
,"http://www.newegg.com/Power-Supplies/SubCategory/ID-58/Page-83?PageSize=36&order=BESTMATCH"
,"http://www.newegg.com/Power-Supplies/SubCategory/ID-58/Page-84?PageSize=36&order=BESTMATCH"
,"http://www.newegg.com/Power-Supplies/SubCategory/ID-58/Page-85?PageSize=36&order=BESTMATCH"
,"http://www.newegg.com/Power-Supplies/SubCategory/ID-58/Page-86?PageSize=36&order=BESTMATCH"
,"http://www.newegg.com/Power-Supplies/SubCategory/ID-58/Page-87?PageSize=36&order=BESTMATCH"
,"http://www.newegg.com/Power-Supplies/SubCategory/ID-58/Page-88?PageSize=36&order=BESTMATCH"
,"http://www.newegg.com/Power-Supplies/SubCategory/ID-58/Page-89?PageSize=36&order=BESTMATCH"
,"http://www.newegg.com/Power-Supplies/SubCategory/ID-58/Page-90?PageSize=36&order=BESTMATCH"
,"http://www.newegg.com/Power-Supplies/SubCategory/ID-58/Page-91?PageSize=36&order=BESTMATCH"
,"http://www.newegg.com/Power-Supplies/SubCategory/ID-58/Page-92?PageSize=36&order=BESTMATCH"
,"http://www.newegg.com/Power-Supplies/SubCategory/ID-58/Page-93?PageSize=36&order=BESTMATCH"
,"http://www.newegg.com/Power-Supplies/SubCategory/ID-58/Page-94?PageSize=36&order=BESTMATCH"
,"http://www.newegg.com/Power-Supplies/SubCategory/ID-58/Page-95?PageSize=36&order=BESTMATCH"
,"http://www.newegg.com/Power-Supplies/SubCategory/ID-58/Page-96?PageSize=36&order=BESTMATCH"
,"http://www.newegg.com/Power-Supplies/SubCategory/ID-58/Page-97?PageSize=36&order=BESTMATCH"
,"http://www.newegg.com/Power-Supplies/SubCategory/ID-58/Page-98?PageSize=36&order=BESTMATCH"
,"http://www.newegg.com/Power-Supplies/SubCategory/ID-58/Page-99?PageSize=36&order=BESTMATCH"
,"http://www.newegg.com/Power-Supplies/SubCategory/ID-58/Page-100?PageSize=36&order=BESTMATCH"]

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
        return item


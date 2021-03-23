import scrapy
from ..items import HouseofindiaScraperItem

class HouseofindiaSpiderSpider(scrapy.Spider):
    name = 'houseOfIndia_spider'                                           # Spider name 
    start_urls = [
        'https://www.houseofindya.com/zyra/necklace-sets/cat'
        ]
                                            
    #custom_settings = {'FEED_FORMAT': 'json','FEED_URI': 'trial.json'}    # Uncomment to save output 
                                                                            # File format supported json, csv, xml

    def parse(self, response):
        items = HouseofindiaScraperItem()
        all_products = response.xpath('//*[(@id = "JsonProductList")]//li')
        
        for product in all_products:
            product_description = product.css("div.catgName p::text")[0].extract()
            product_new_price = product.css("div.catgName span::text")[0].extract()
            product_old_price = product.css("div.catgName span::text")[1].extract()
            product_image_url = product.css("div.catgItem img::attr(data-original)").extract_first()
            product_image_mouseover_url = product.css("div.catgItem img::attr(onmouseover)").extract_first().replace("this.src=","").replace('"',"")
            
            items['product_description'] = product_description
            items['product_new_price'] = product_new_price
            items['product_old_price'] = product_old_price
            items['product_image_url'] = product_image_url
            items['product_image_mouseover_url'] = product_image_mouseover_url
            
            yield items


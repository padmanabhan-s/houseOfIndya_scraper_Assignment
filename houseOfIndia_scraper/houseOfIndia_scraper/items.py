# Define here the models for your scraped items
#
# See documentation in:
# https://docs.scrapy.org/en/latest/topics/items.html

import scrapy


class HouseofindiaScraperItem(scrapy.Item):
    # define the fields for your item here like:
    # name = scrapy.Field()
    
    product_description = scrapy.Field()
    product_old_price = scrapy.Field()
    product_new_price = scrapy.Field()
    product_image_url = scrapy.Field()
    product_image_mouseover_url = scrapy.Field()
    pass

# Define here the models for your scraped items
#
# See documentation in:
# https://docs.scrapy.org/en/latest/topics/items.html

import scrapy
from scrapy.loader.processors import MapCompose


class ComfyItem(scrapy.Item):
    scanned_time = scrapy.Field()
    product_url = scrapy.Field()
    product_title = scrapy.Field(input_processor=MapCompose(str.strip))
    product_sku = scrapy.Field(input_processor=MapCompose(str.strip))
    product_category = scrapy.Field()
    product_availability = scrapy.Field()
    product_price = scrapy.Field(input_processor=MapCompose(str.strip))
    product_price_regular = scrapy.Field(input_processor=MapCompose(str.strip))
    # special_offers = scrapy.Field()

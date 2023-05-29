# Define here the models for your scraped items
#
# See documentation in:
# https://docs.scrapy.org/en/latest/topics/items.html

import scrapy
import re
from scrapy.loader.processors import MapCompose


def clean_price(value):
    cleaned_value = re.sub(r'\s', '', value)
    return int(cleaned_value)


class ComfyItem(scrapy.Item):
    scanned_time = scrapy.Field()
    product_url = scrapy.Field()
    product_title = scrapy.Field(input_processor=MapCompose(str.strip))
    product_sku = scrapy.Field(input_processor=MapCompose(str.strip))
    product_category = scrapy.Field()
    product_availability = scrapy.Field()
    product_price = scrapy.Field(input_processor=MapCompose(str.strip, clean_price))
    product_price_regular = scrapy.Field(input_processor=MapCompose(str.strip, clean_price))
    special_offers = scrapy.Field()

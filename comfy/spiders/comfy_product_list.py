import logging
from datetime import datetime

import scrapy
from itemloaders.processors import TakeFirst
from scrapy.loader import ItemLoader
from scrapy.utils.response import open_in_browser
from scrapy_selenium import SeleniumRequest

from comfy.items import ComfyItem

logger = logging.getLogger('__main__')


class ComfyProductsListSpider(scrapy.Spider):
    name = "comfy_products_list"
    allowed_domains = ["comfy.ua"]

    def start_requests(self):
        url = "https://comfy.ua/ua/"
        yield SeleniumRequest(url=url, callback=self.parse, wait_time=10)

    def parse(self, response, **kwargs):
        # Get 18 main categories and go to them
        for link in response.xpath("//div[@class='menu-desktop__items__item row items-center']/a/@href").getall():
            yield SeleniumRequest(url=link, callback=self.parse_category)

    def parse_category(self, response):
        # Get all categories from main сategory
        subcategories = response.css('.portal-tile__item a::attr(href)').getall()
        products = response.xpath('.//a[@class="products-list-item__name"]/@href').getall()
        next_page = response.xpath(
            './/div[@class="pagination__container"]//*[contains(text(),"Вперед")]/@href'
        ).get()
        if subcategories:
            for category_link in subcategories:
                category_link = category_link.replace('../', '')
                yield SeleniumRequest(url=f"https://comfy.ua/ua/{category_link}", callback=self.parse_category)
        elif products:
            for product_link in products:
                yield SeleniumRequest(url=product_link, callback=self.parse_product)
            if next_page:
                yield SeleniumRequest(url=next_page, callback=self.parse_category)
        else:
            logger.info('Empty subcategories and products')

    def parse_product(self, response):
        loader = ItemLoader(item=ComfyItem(), response=response)
        loader.default_output_processor = TakeFirst()
        loader.add_value('scanned_time', datetime.now().isoformat())
        loader.add_value('product_url', response.url)
        loader.add_css('product_title', "h1.gen-tab__name::text")
        loader.add_css('product_sku', 'span.i-main__sku::text', re=r'Код: (.+)')
        product_category_list = response.css('a.icon-comfy.breadcrumbs__item::text').getall()
        clear_category = []
        for item in product_category_list:
            clear_category.append(item.strip())
        loader.add_value('product_category', {'product_category': clear_category})
        link_available = response.css('span.base-button__text::text')
        if link_available:
            is_available = response.css('span.base-button__text::text').get().strip() == 'Купити'
            if not is_available:
                open_in_browser(response)
            loader.add_value('product_availability', is_available)
        else:
            open_in_browser(response)
            loader.add_value('product_availability', False)
        loader.add_css('product_price', 'div.price__current::text', re=r'\d+.?\d+')
        loader.add_css('product_price_regular', 'div.price__old::text', re=r'\d+.?\d+')
        cashback_link = response.css('span.bonus-label-value::text')
        if cashback_link:
            cashback = response.css('span.bonus-label-value::text').get().strip()
            loader.add_value('special_offers', {"cashback": f"{cashback} на бонусний рахунок"})
        yield loader.load_item()

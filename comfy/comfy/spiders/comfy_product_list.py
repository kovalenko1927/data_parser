import scrapy
from itemloaders.processors import TakeFirst
from scrapy.loader import ItemLoader

# from comfy.items import ComfyItem
from datetime import datetime

from scrapy.loader.processors import Join


class ComfyProductsListSpider(scrapy.Spider):
    name = "comfy_products_list"
    allowed_domains = ["comfy.ua"]
    start_urls = ["https://comfy.ua/ua/"]

    def parse(self, response, **kwargs):
        # Get 18 main categories and go to them
        for link in response.xpath("//div[@class='menu-desktop__items__item row items-center']/a/@href").getall()[0:1]:
            yield response.follow(link, self.parse_category)

    def parse_category(self, response):
        # Get all categories from main сategory
        for link in response.css('a.portal-tile__link::attr(href)').getall()[0:3]:
            yield response.follow("https://comfy.ua/ua/" + link[3:], self.parse_sub_category)

    def parse_sub_category(self, response):
        # Get subcategory from category
        links_sub_category = response.css('a.portal-tile__link::attr(href)').getall()
        if len(links_sub_category) > 0:
            for link in links_sub_category[0:3]:
                yield response.follow("https://comfy.ua/ua/" + link[6:], self.parse_product_link)
        else:
            yield from self.parse_product_link(response)

    def parse_product_link(self, response):
        # Get product links from page
        for link in response.css('a.products-list-item__code.dsk::attr(href)').getall():
            # yield response.follow(link, self.parse_product)
            print(link)
        # Go through each page
        # next_page = response.css('a.pagination-item.p-i.p-i--meta::attr(href)')
        # if next_page:
        #     yield response.follow(next_page, self.parse_product_link)

    # def parse_product(self, response):
    #     # Добавить проверку на наличие product_sku
    #     loader = ItemLoader(item=ComfyItem(), response=response)
    #     loader.default_output_processor = TakeFirst()
    #     loader.add_value('scanned_time', datetime.now().isoformat())
    #     loader.add_value('product_url', response.url)
    #     loader.add_css('product_title', "h1.gen-tab__name::text")
    #     loader.add_css('product_sku', 'span.i-main__sku::text', re='\d+')
    #     product_category_list = response.css('a.icon-comfy.breadcrumbs__item::text').getall()
    #     loader.add_value('product_category', product_category_list, Join())
    #     if response.css('span.base-button__text::text').get().strip() == 'Купити':
    #         loader.add_value('product_availability', True)
    #     else:
    #         loader.add_value('product_availability', False)
    #     loader.add_css('product_price', 'div.price__current::text')
    #     loader.add_css('product_price_regular', 'div.price__old::text')
    #     # loader.add_xpath("special_offers", )
    #     yield loader.load_item()
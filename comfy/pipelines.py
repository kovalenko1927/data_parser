# Define your item pipelines here
#
# Don't forget to add your pipeline to the ITEM_PIPELINES setting
# See: https://docs.scrapy.org/en/latest/topics/item-pipeline.html


import pandas as pd
# useful for handling different item types with a single interface
from itemadapter import ItemAdapter


class CSVPipeline:
    def __init__(self):
        self.data = pd.DataFrame()

    def process_item(self, item, spider):
        main_data = ItemAdapter(item).asdict()
        data_frame = pd.DataFrame.from_records([main_data])
        self.data = pd.concat([self.data, data_frame], ignore_index=True)

        return item

    def close_spider(self, spider):
        self.data.to_csv(f'{spider.name}.csv', index=False)

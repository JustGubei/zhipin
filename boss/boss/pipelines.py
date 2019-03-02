# -*- coding: utf-8 -*-

# Define your item pipelines here
#
# Don't forget to add your pipeline to the ITEM_PIPELINES setting
# See: https://doc.scrapy.org/en/latest/topics/item-pipeline.html
import pymysql
import pymongo
from scrapy import Request
from scrapy.exceptions import DropItem
from scrapy.pipelines.images import ImagesPipeline


class BossPipeline(object):
    def process_item(self, item, spider):
        return item


class BossMongoPipeline(object):
    def __init__(self, uri , database):
        self.uri = uri
        self.database = database


    @classmethod
    def from_crawler(cls, crawler):
        return cls(
            uri =crawler.settings.get('MONGO_URI'),
            database =crawler.settings.get('MONGO_DB'),

            )

    def open_spider(self, spider):

        self.client = pymongo.MongoClient(self.uri)
        self.db  = self.client[self.database]


    def close_spider(self, spider):
        self.client.close()

    def process_item(self, item, spider):

        self.db[item.collection_name].insert(dict(item))

        return item
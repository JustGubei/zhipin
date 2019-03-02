# -*- coding: utf-8 -*-

# Define here the models for your scraped items
#
# See documentation in:
# https://doc.scrapy.org/en/latest/topics/items.html

import scrapy


class BossItem(scrapy.Item):
    collection_name = 'boss'
    job_title = scrapy.Field()
    job_price = scrapy.Field()
    comp_name = scrapy.Field()
    comp_line = scrapy.Field()
    per_num = scrapy.Field()
    publis_name = scrapy.Field()
    publis_time = scrapy.Field()
    src = scrapy.Field()
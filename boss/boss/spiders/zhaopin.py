# -*- coding: utf-8 -*-
import json
from urllib.parse import urlencode

import scrapy

from boss.items import BossItem
from boss.spiders.agent_helper import get_random_agent
from boss.spiders.zhaopin_helper import *


class ZhaopinSpider(scrapy.Spider):
    name = 'zhaopin'
    allowed_domains = ['www.zhipin.com']
    start_urls = 'https://www.zhipin.com/job_detail/?'

    def get_headers(self):
        headers = {
            'User-Agent': 'Mozilla/4.0 (compatible; MSIE 7.0; Windows NT 5.1; 360SE)',
            'Host': 'www.zhipin.com',
            'Accept': 'text/html,application/xhtml+xml,application/xml;q=0.9,image/webp,image/apng,*/*;q=0.8',
            'Accept-Encoding': 'gzip, deflate, br',
            'Accept-Language': 'zh-CN,zh;q=0.9',
            'Content-Type': 'text/html;charset=UTF-8',
        }
        return headers



    def start_requests(self):
        for keyword in self.settings.get('KEYWORDS'):


            #https://www.zhipin.com/c101270100/?query=python&page=1&ka=page-1

            for page in range(1, 7):
                data = {'query': keyword, 'page': page,'scity':101270100,'ka': 'page-%s' % page}
                params = urlencode(data)
                boss_url = self.start_urls + params


                yield scrapy.Request(url=boss_url,
                                     headers=self.get_headers(),
                                     dont_filter=True,
                                     meta={'page': page},
                                     callback=self.parse,
                                    )

    def parse(self, response):
        gl_item = response.selector.xpath('//div[@class="job-primary"]')

        for i in gl_item:
            boss = BossItem()
            job_title = ''.join(i.xpath('.//div[@class="job-title"]/text()').extract())
            job_price = ''.join(i.xpath('.//h3[@class="name"]/a/span/text()').extract())
            comp_name = ''.join(i.xpath('.//div[@class="company-text"]/h3/a/text()').extract())
            comp_line = ''.join(i.xpath('.//div[@class="company-text"]/p/text()').extract()[0])


            comp_info = i.xpath('.//div[@class="company-text"]/p/text()').extract()
            # print(per_num)
            if len(comp_info)==3:
                per_num = comp_info[2]
            else:
                per_num = comp_info[1]

            publis_name = ''.join(i.xpath('.//div[@class="info-publis"]/h3/text()').extract()[0])
            publis_time = ''.join(i.xpath('.//div[@class="info-publis"]/p/text()').extract())
            src = ''.join(i.xpath('.//a[@class="btn btn-startchat"]/@redirect-url').extract())

            #https://www.zhipin.com/geek/new/index/chat?id=1ff819389ed8632e0nVz29S8FFM~


            # job_jianjie = ''.join(i.xpath('.//div[@class="info-primary"]/p/text()'))

            # comp_info = ''.join(i.xpath('.//div[@class="company-text"]/p/text()'))

            boss['job_title'] = job_title
            boss['job_price'] = job_price
            boss['comp_name'] = comp_name
            boss['comp_line'] = comp_line
            boss['per_num'] = per_num
            boss['publis_name'] = publis_name
            boss['publis_time'] = publis_time
            boss['src'] = src

            yield boss

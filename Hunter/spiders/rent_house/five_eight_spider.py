#!/usr/bin/python
# -*- coding: utf-8 -*-
# shq


from scrapy import Spider, Request
from Hunter.items import items
import os
import re
from urlparse import urljoin

'''
class FiveEight(Spider):
    name = "five_eight_spider"
    start_urls = [
        'http://bj.58.com/hezu/34003942117813x.shtml?psid=155238304200302092046667229&ClickID=2&cookie=||https://www.baidu.com/link?url=iD_ze-MxP5arCspP9GYHO9SzJROX9osIveH9c3B9jVm&wd=&eqid=b27ddc1d000cf9cc000000025b163b53|c5/njVsWO1czf2r3BQxDAg==&PGTID=0d3090a7-0000-161c-eaaf-462744864302&apptype=0&entinfo=34003942117813_0&fzbref=0&iuType=gz_2&key=&pubid=32582326&from=2-list-0&params=busitime^desc&local=1&trackkey=34003942117813_04374e00-b8f1-4c8d-a068-a344ad86d679_20180605152821_1528183701304&fcinfotype=gz'
    ]

    def parse(self, response):
        try:
            item = items.RentHouseItem()
            title=response.xpath('//div[@class="house-title"]/h1/text()').extract_first()
            item['title']=title
            print item.get('title')
            print response.body
            yield item



        except Exception:
            import traceback
            traceback.print_exc()
            '''
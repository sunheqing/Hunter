#!/usr/bin/python
# -*- coding: utf-8 -*-
# shq


from scrapy import Spider, Request
from Hunter.items import items
import os
import re
from urlparse import urljoin


class DouBanRentA(Spider):
    name = "douban_rent_1"
    #  url  小组名称
    start_urls = [
        'https://www.douban.com/group/279962/discussion?start='
        ]
    start_urls_1 = [
        'https://www.douban.com/group/65239/discussion?start=',   # 北京海淀短期租房  (over)
        'https://www.douban.com/group/279962/discussion?start=',  # 北京租房（非中介）
        'https://www.douban.com/group/sweethome/discussion?start=',  # 北京租房（密探）
        'https://www.douban.com/group/beijingzufang/discussion?start=',  # 北京租房
        'https://www.douban.com/group/26926/discussion?start=',   #  北京租房豆瓣
        'https://www.douban.com/group/zhufang/discussion?start=',   #  北京无中介租房（寻天使投资）
        'https://www.douban.com/group/276176/discussion?start=', # 北京出租房（请自觉统一标题格式）
        'https://www.douban.com/group/haidianzufang/discussion?start=', # 北京海淀租房
        'https://www.douban.com/group/502225/discussion?start=',  #  北京合租、整租、公寓房
        'https://www.douban.com/group/589927/discussion?start=',  #  北京中关村租房（限女神一位）
        'https://www.douban.com/group/605457/discussion?start=',   #  上地西二旗合租群
        'https://www.douban.com/group/450859/discussion?start=',   #  北京昌平回龙观周边租房小组
        'https://www.douban.com/group/257523/discussion?start=',    #   北京租房房东联盟(中介勿扰)
        'https://www.douban.com/group/opking/discussion?start=',   #   北京个人租房 （真房源|无中介）
        'https://www.douban.com/group/625354/discussion?start=',   #  北京租房（真的没有中介）小组
        'https://www.douban.com/group/259273/discussion?start='   #  北京租房生活
    ]
    def start_requests(self):
        # 构造每个小组的每一页的url，每个小组抓取1150条数据
        for url in self.start_urls:
            for i in xrange(0,1150,25):
                new_url = url+str(i)
                yield Request(new_url, self.parse)
    def parse(self, response):
        try:
            all_tr = response.xpath('//tr[@class=""]')
            for tr in all_tr:
                title = tr.xpath('./td[1]/a/@title').extract_first()
                hot = tr.xpath('./td[3]/text()').extract_first()
                time = tr.xpath('./td[4]/text()').extract_first()
                every_url = tr.xpath('./td[1]/a/@href').extract_first()
                yield response.follow(every_url, callback=self.parse_every, meta={'title': title, 'time': time,'hot':hot})

        except Exception:
            import traceback
            traceback.print_exc()

    def parse_every(self, response):

        try:
            img_url_sum = ''
            all_url = response.xpath('//div[@class="topic-content"]//img/@src').extract()
            if all_url:
                for i in all_url:
                    i = i + '|||'
                    img_url_sum = img_url_sum + i
            texts = response.xpath('string(//div[@class="topic-content"])').extract_first()
            text = texts.replace('\n', '').replace('\r', '').replace('\t', '').replace(' ', '').replace(u'\xa0',
                                                                                                       '').replace(
                u'\u3000', '')
            item = items.DouBanRentHouseItem()
            item['publish_time'] = response.xpath('//span[@class="color-green"]/text()').extract_first()
            item['title'] = response.meta.get('title')
            item['last_time'] = response.meta.get('time')
            item['source'] = response.url
            item['hot'] = response.meta.get('hot')
            item['image_url'] = img_url_sum
            item['content'] = text
            print item
            yield item



        except Exception:
            import traceback
            traceback.print_exc()

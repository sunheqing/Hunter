#!/usr/bin/python
# -*- coding: utf-8 -*-
# shq


from scrapy import Spider, Request
from Hunter.items import items
import os
import re
from urlparse import urljoin


class GongTongReconstruction(Spider):
    name = "gong_tong_reconstruction_spider"
    start_urls = [
        'https://china.kyodonews.net/news/cat85'
    ]

    def parse(self, response):
        try:
            every_li = response.xpath('//ul[@id="js-postListItems"]/li')

            for li in every_li:
                every_url = urljoin(response.url, li.xpath('.//a/@href').extract_first())
                title = li.xpath('.//a/h3/text()').extract_first()
                time = li.xpath('.//p[@class="time"]/text()').extract_first()
                yield response.follow(every_url, callback=self.parse_every, meta={'title': title, 'time': time})


        except Exception:
            import traceback
            traceback.print_exc()

    def parse_every(self, response):

        try:
            texts = ''.join(response.xpath('//div[@class="article-body"]/p/text()').extract()) #这个网站结构性非常好
            get_url = response.xpath('//div[@class="mainpic"]/img/@src').extract_first()
            item = items.NewsItem()
            item['title'] = response.meta.get('title')
            item['time'] = response.meta.get('time').replace(' ','').replace('\n','').replace('\r','').replace('\t','').replace(u'\u3000','').replace(u'\xa0','').replace('|','')
            item['source'] = response.url
            item['origin'] = u"日本共同社"
            item['news_type'] = u"灾难"
            item['lable'] = u"日本 灾难 建设"
            item['content'] = texts
            if get_url:
                photo_url = urljoin(response.url, get_url)
                item['image_src'] = photo_url
            else:
                item['image_src'] = ''
            print item
            yield item



        except Exception:
            import traceback
            traceback.print_exc()

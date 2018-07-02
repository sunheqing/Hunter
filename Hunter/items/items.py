# -*- coding: utf-8 -*-

# Define here the models for your scraped items
#
# See documentation in:
# https://doc.scrapy.org/en/latest/topics/items.html

import scrapy

class NewsItem(scrapy.Item):

    title = scrapy.Field()  #新闻标题
    source = scrapy.Field()  #网址
    origin = scrapy.Field()   #转载自
    time = scrapy.Field()  #发布时间
    image_src = scrapy.Field()  #主图
    news_type = scrapy.Field()  #新闻类型
    lable = scrapy.Field()   #新闻标签
    content = scrapy.Field()   #正文

class RentHouseItem(scrapy.Item):
    # define the fields for your item here like:
    # name = scrapy.Field()
    title = scrapy.Field()  # 标题
    rent_method = scrapy.Field()  # 租赁方式
    rent_money = scrapy.Field()  # 租金
    give_money_method = scrapy.Field()  # 付款方式
    source = scrapy.Field()  # 网址
    img_url = scrapy.Field()  # 房源主图
    house_type = scrapy.Field()  # 房屋类型
    face_to = scrapy.Field()  # 房屋朝向
    community = scrapy.Field()  # 所在小区
    area = scrapy.Field()  # 所在区域
    detailed_path = scrapy.Field()  # 详细地址
    phone = scrapy.Field()  # 联系方式
    important_point = scrapy.Field()  # 房屋亮点
    http_method = scrapy.Field()  # 请求方式
    content = scrapy.Field()
    # table = scrapy.Field()  #存入的数据库表单




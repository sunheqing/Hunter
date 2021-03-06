# -*- coding: utf-8 -*-

# Define your item pipelines here
#
# Don't forget to add your pipeline to the ITEM_PIPELINES setting
# See: https://doc.scrapy.org/en/latest/topics/item-pipeline.html

import arrow
from Hunter.mysql_operating import sql
from Hunter.utils_box.get_other_field import douban_rent_house_get_other_field
import sys
reload(sys)
sys.setdefaultencoding('utf8')


class HunterPipeline(object):
    def __init__(self):
        print u"数据库管道正在初始化......"
    def process_item(self, item, spider):
        try:
            item.update(douban_rent_house_get_other_field(item))
            TIME_AREA = 'Asia/Shanghai'
            spider_get_time = arrow.now(TIME_AREA).format('YYYY-MM-DD HH:mm:ss')
            print u"开始执行数据库操作！"
            #sql_talk_insert="insert into website.news(title,source,origin,time,image_src,news_type,lable,content,spider_get_time) VALUE('{0}','{1}','{2}','{3}','{4}','{5}','{6}','{7}','{8}')".format(item['title'],item['source'],item['origin'],item['time'],item['image_src'],item['news_type'],item['lable'],item['content'],spider_get_time)
            sql_talk_insert = "insert into website.renthouse(title,source,publish_time,last_time,image_url,hot,content,get_time,rent_money,phone,area,area_lable,house_lable,rent_method,give_money_method) VALUE('{0}','{1}','{2}','{3}','{4}','{5}','{6}','{7}','{8}','{9}','{10}','{11}','{12}','{13}','{14}')".format(
                item['title'], item['source'], item['publish_time'], item['last_time'], item['image_url'], item['hot'],
                item['content'], spider_get_time,item["rent_money"],item["phone"],item["area"],item["area_lable"],item["house_lable"],item["rent_method"],item["give_money_method"])

            sql(sql_talk_insert)
            print item
        except Exception:
            import traceback
            traceback.print_exc()
        return item



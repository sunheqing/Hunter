# -*- coding: utf-8 -*-

# Define your item pipelines here
#
# Don't forget to add your pipeline to the ITEM_PIPELINES setting
# See: https://doc.scrapy.org/en/latest/topics/item-pipeline.html

import arrow
from Hunter.mysql_operating import sql
import sys
reload(sys)
sys.setdefaultencoding('utf8')


class HunterPipeline(object):
    def __init__(self):
        print u"数据库管道正在初始化......"
    def process_item(self, item, spider):
        try:
            TIME_AREA = 'Asia/Shanghai'
            spider_get_time = arrow.now(TIME_AREA).format('YYYY-MM-DD HH:mm:ss')
            print u"开始执行数据库操作！"
            sql_talk_insert="insert into website.news(title,source,origin,time,image_src,news_type,lable,content,spider_get_time) VALUE('{0}','{1}','{2}','{3}','{4}','{5}','{6}','{7}','{8}')".format(item['title'],item['source'],item['origin'],item['time'],item['image_src'],item['news_type'],item['lable'],item['content'],spider_get_time)

            sql(sql_talk_insert)
        except Exception:
            import traceback
            traceback.print_exc()
        return item



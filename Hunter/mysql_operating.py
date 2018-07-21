# -*- coding: utf-8 -*-
import pymysql
import time
import re
from utils_box.special_name import lable_name
import sys
reload(sys)
sys.setdefaultencoding('utf8')

db = pymysql.connect(host="localhost", user="root", password="123456", db="website", port=3306, charset='utf8')
cursor = db.cursor()


def sql(sql_talk):
    try:
        row = cursor.execute(sql_talk)
        db.commit()
        print u"受影响的行数：" + str(row) + u" 行  （来源:豆瓣租房数据库执行函数）"
    except:
        db.rollback()
        print u"执行错误，已经回滚，请检查数据库！"
def no_num_change(strings):
    for s in strings:
        if u'\u0030' <= s and s <= u'\u0039':
            pass
        else:
            strings = strings.replace(s, '-')
    return strings
#创建数据库语句
'''
sql_talk_create = """CREATE TABLE website.news (
    id INT PRIMARY KEY AUTO_INCREMENT,
    title VARCHAR(100) NOT NULL,
    source VARCHAR(100),
    origin VARCHAR(50),
    time VARCHAR(100),
    image_src VARCHAR(100),
    news_type VARCHAR(50),
    lable VARCHAR(50),
    content VARCHAR(5000),
    no VARCHAR(100),
    spider_get_time VARCHAR(50),
    INDEX (id)
) AUTO_INCREMENT=0;"""

sql_talk_create = """CREATE TABLE website.RentHouse (
    id INT PRIMARY KEY AUTO_INCREMENT,
    title VARCHAR(100) NOT NULL,
    source VARCHAR(100),
    give_money_method VARCHAR(50),
    get_time VARCHAR(100),
    image_url VARCHAR(100),
    rent_method VARCHAR(50),
    rent_money VARCHAR(50),
    content VARCHAR(5000),
    area_lable VARCHAR(150),
    area VARCHAR(80),
    phone VARCHAR(50),
    house_lable VARCHAR(150),
    hot VARCHAR(20),
    last_time VARCHAR(50),
    publish_time VARCHAR(150),
    INDEX (id)
) AUTO_INCREMENT=0;"""
'''
def clean_content(code_list):
    for code in code_list:
        sql_talk_0 = "select %s,id from website.news" % code
        print 'sql_talk: ', sql_talk_0
        try:
            row = cursor.execute(sql_talk_0)
            for c in cursor.fetchall():
                cleaned = c[0].replace(' ','').replace('\n','').replace('\r','').replace('\t','').replace(u'\u3000','').replace(u'\xa0','').replace('|','')
                sql_talk_1 = "UPDATE website.news set {0} ='{1}' where id = '{2}'".format(code, cleaned, c[1])
                print 'sql_talk: ', sql_talk_1
                sql(sql_talk_1)
            db.commit()
            print row
        except:
            db.rollback()
def rent_house_clean_not_use_field():   #清理无效的（发布时间非2018年6、7月份的）
    sql_talk_get_publish_time="select id,publish_time from website.renthouse"
    try:
        row = cursor.execute(sql_talk_get_publish_time)
        for c in cursor.fetchall():
            if '2018-06' in c[1] or '2018-07' in c[1]:
                pass
            else:
                sql("delete from website.renthouse where id ={0}".format(c[0]))
        db.commit()
        print row
    except:
        db.rollback()

def rent_house_get_other_field():   #提取租房数据库的其他未获得字段
    sql_talk_get_content_title="select id,title,content from website.renthouse"
    ze_phone_formula = r"[1-9]\d{10}(?!\d)"   #提取联系方式
    ze_phone = re.compile(ze_phone_formula)
    try:
        row = cursor.execute(sql_talk_get_content_title)
        for c in cursor.fetchall():
            text=c[1]+c[2]
            l=[]
            for i in no_num_change(text.decode('utf8')).split('-'):
                if len(i)==4:
                    l.append(i)
            sql("UPDATE website.renthouse set rent_money ='{0}' where id = '{1}'".format('|'.join(l), c[0]))
            get_phone = re.search(ze_phone, c[1]+c[2])
            if get_phone:
                if ('微信' in c[1]+c[2] or 'vx' in c[1]+c[2]) or ('VX' in c[1]+c[2] or 'Vx' in c[1]+c[2]):
                    phone = '电话、微信:'+get_phone.group(0)
                else:
                    phone = '电话:' + get_phone.group(0)
                sql("UPDATE website.renthouse set phone ='{0}' where id = '{1}'".format(phone, c[0]))

            for key in lable_name.keys():
                value_list=[]
                for value in lable_name.get(key):
                    if value in c[1]+c[2]:
                        value_list.append(value)
                value_str = '|'.join(value_list)
                if '线' in key:
                    sql("UPDATE website.renthouse set area ='{0}' where id = '{1}'".format(value_str, c[0]))
                elif '外部标签' in key:
                    sql("UPDATE website.renthouse set area_lable ='{0}' where id = '{1}'".format(value_str, c[0]))
                elif '内部标签' in key:
                    sql("UPDATE website.renthouse set house_lable ='{0}' where id = '{1}'".format(value_str, c[0]))
                elif '出租方式' in key:
                    sql("UPDATE website.renthouse set rent_method ='{0}' where id = '{1}'".format(value_str, c[0]))
                else:
                    sql("UPDATE website.renthouse set give_money_method ='{0}' where id = '{1}'".format(value_str, c[0]))


        db.commit()
        print row
    except:
        db.rollback()


if __name__ == '__main__':
    time_start = time.time()
    # 执行数据库操作语句
    # clean_content(["content"])
    # clean_content(["time"])
    # rent_house_clean_not_use_field()
    # rent_house_get_other_field()
    time_end=time.time()
    print u"程序运行时间：" + str(time_end - time_start) + u'秒'




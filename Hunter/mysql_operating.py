# -*- coding: utf-8 -*-
import pymysql
import time
import sys
reload(sys)
sys.setdefaultencoding('utf8')

db = pymysql.connect(host="localhost", user="root", password="123456", db="website", port=3306, charset='utf8')
cursor = db.cursor()


def sql(sql_talk):
    try:
        row = cursor.execute(sql_talk)
        db.commit()
        print u"受影响的行数：" + str(row) + u" 行  （来源:新闻数据库执行函数）"
    except:
        db.rollback()
        print u"执行错误，已经回滚，请检查数据库！"

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
time_start = time.time()
#执行数据库操作语句
#clean_content(["content"])
#clean_content(["time"])

time_end=time.time()
print u"程序运行时间："+str(time_end-time_start)+u'秒'
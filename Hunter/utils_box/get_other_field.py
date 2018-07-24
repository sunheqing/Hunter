# -*- coding: utf-8 -*-
import re
from special_name import lable_name
# 为管道调用创建
def no_num_change(strings):
    for s in strings:
        if u'\u0030' <= s and s <= u'\u0039':
            pass
        else:
            strings = strings.replace(s, '-')
    return strings
def douban_rent_house_get_other_field(item):   #提取租房数据库的其他未获得字段

    ze_phone_formula = r"[1-9]\d{10}(?!\d)"   #提取联系方式
    ze_phone = re.compile(ze_phone_formula)

    text=item["title"]+item["content"]
    l=[]
    for i in no_num_change(text.decode('utf8')).split('-'):
        if len(i)==4:
            l.append(i)
    item["rent_money"] ='|'.join(l)
    get_phone = re.search(ze_phone, text)
    if get_phone:
        if ('微信' in text or 'vx' in text) or ('VX' in text or 'Vx' in text):
            phone = '电话、微信:'+get_phone.group(0)
        else:
            phone = '电话:' + get_phone.group(0)
        item["phone"] =phone

    for key in lable_name.keys():
        value_list=[]
        for value in lable_name.get(key):
            if value in text:
                value_list.append(value)
        value_str = '|'.join(value_list)
        if '线' in key:
            item["area"] =value_str
        elif '外部标签' in key:
            item["area_lable"] = value_str
        elif '内部标签' in key:
            item["house_lable"] = value_str
        elif '出租方式' in key:
            item["rent_method"] = value_str
        else:
            item["give_money_method"] = value_str
    print "数据库管道插件，获取其他豆瓣租房其他字段"
    return item



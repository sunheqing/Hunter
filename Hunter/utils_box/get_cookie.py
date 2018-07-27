#!/usr/bin/python
# -*- coding: utf-8 -*-
import re
'''
    获取response里的cookie
'''

def get_cookie(response):
    data = dict(response.headers)
    set_cookie = data.get('Set-Cookie')
    if type(set_cookie) is list:
        cookie_items = set_cookie
    elif type(set_cookie) in (str, unicode):
        cookie_items = set_cookie.split(';')
    else:
        cookie_items = ''
    if len(cookie_items) > 1:
        cookies = {}
        for item in cookie_items:
            key_value = item.split('=')
            if len(key_value) == 2:
                pattern = re.compile(r'(expires|path|domain|Secure|HttpOnly)', re.I)
                if not re.search(pattern, key_value[0]):
                    cookies[key_value[0]] = key_value[1]
        if cookies:
            return cookies
    return ''

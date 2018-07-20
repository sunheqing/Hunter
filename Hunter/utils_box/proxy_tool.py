#!/usr/bin/python
# -*- coding: utf-8 -*-
# AUTHor:shq

import time
import hashlib

# ******************************使用了公司的代理，仅个人使用，不得外漏！***************************
# 订单号
orderno = "*************"     #拒绝外泄！
secret = "****************"   #拒绝外泄！

# -*- 代理接口 -*-
ip = "forward.xdaili.cn"
port = "80"

ip_port = ip + ":" + port

# -*- 签名算法 -*-

# 计算时间戳
timestamp = str(int(time.time()))
text = "orderno=" + orderno + "," + "secret=" + secret + "," + "timestamp=" + timestamp
# 计算sign
md5_string = hashlib.md5(text).hexdigest()
# 转换成大写
sign = md5_string.upper()

# -*- 签名 -*-
AUTH = "sign=" + sign + "&" + "orderno=" + orderno + "&" + "timestamp=" + timestamp

# IP = 'https://' + ip_port
headers = {"Proxy-Authorization": AUTH}
proxy_http = "http://" + ip_port
proxy_https = "https://" + ip_port
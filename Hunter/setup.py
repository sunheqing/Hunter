# encoding: utf-8

#这是关于批量执行多个spider的配置文件，官方文档有这个,这个没有也可以，目前删掉还没发现问题
#应该和打包有关
from setuptools import setup, find_packages

setup(name='scrapy-Hunter',
  entry_points={
    'scrapy.commands': [
      'crawlall=Hunter.commands:crawlall',  #定义了crawlall命令，要写出这个新命令的文件位置
    ],
  },
 )

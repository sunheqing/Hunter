# coding=utf-8
from scrapy import cmdline
import redis
#spider = "gong_tong_global_spider"
#spider = "gong_tong_CHN_JPN_spider"
#spider = "gong_tong_economy_science_spider"
#spider = "gong_tong_JPN_political_spider"
#spider = "gong_tong_environmental_spider"
#spider = "gong_tong_society_spider"
#spider = "gong_tong_reconstruction_spider"
#spider = "gong_tong_Fukushima_spider"

spider = ''

#批量全部执行！
#cmdline.execute(["scrapy", "crawlall"])  #和操作数据库的游标对象用法很类似

#逐个执行
#cmdline.execute(["scrapy", "crawl", spider])
class Task(object):
    def __init__(self):
        self.rcon = redis.StrictRedis(host='localhost', db=5)
        self.queue = 'task:wechat:queue'

    def listen_task(self):
        while True:
            task = self.rcon.blpop(self.queue, 0)[1]
            task = eval(task)
            message = task.get('text')
            user = task.get('user_id')

            if message == 'Hunter' and user == 'oHfuz0hYUIrqM6b410E7nK8TnlGE':
                cmdline.execute(["scrapy", "crawlall"])



if __name__ == '__main__':
    print 'listen task queue'
    Task().listen_task()

from .crawler import Crawler
from .db import RedisClient


POOL_UPPER_THRESHOLD = 10000


class Getter(object):
    def __init__(self):
        self.redis = RedisClient()
        self.cralwer = Crawler()

    def is_over_threshold(self):
        """
        判断是否达到了代理池限制
        :return: 是否
        """
        if self.redis.count() >= POOL_UPPER_THRESHOLD:
            return True
        else:
            return False

    def run(self):
        print('获取器开始运行...')
        if not self.is_over_threshold():
            for callback_label in range(self.cralwer.__CrawlFuncCount__):
                callback = self.cralwer.__CrawlFunc__[callback_label]
                proxies = self.cralwer.get_proxies(callback)
                for proxy in proxies:
                    self.redis.add(proxy)


if __name__ == '__main__':
    get = Getter()
    get.run()

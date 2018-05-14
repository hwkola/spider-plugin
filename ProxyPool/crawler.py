from pyquery import PyQuery as pq
from .utils import get_page


class ProxyMetaClass(type):
    def __new__(mcs, name, bases, attrs):
        count = 0
        attrs['__CrawlFunc__'] = []
        for k,v in attrs.items():
            if 'crawl' in k:
                attrs['__CrawlFunc__'].append(k)
                count += 1
        attrs['__CrawlFuncCount__'] = count
        return type.__new__(mcs, name, bases, attrs)


class Crawler(object, metaclass=ProxyMetaClass):
    def get_proxies(self, callback):
        proxies = []
        for proxy in eval("self.{}()".format(callback)):
            print('成功获取代理', proxy)
            proxies.append(proxy)
        return proxies

    def crawl_daili66(self, page_count=4):
        """
        获取代理66
        :param page_count: 页码
        :return: 代理
        """
        start_urls = 'http://www.66ip.cn/{}.html'
        urls = [start_urls.format(page) for page in range(1, page_count-1)]
        for url in urls:
            print('爬取中...', url)
            html = get_page(url)
            if html:
                doc = pq(html)
                trs = doc('.containerbox tage tr:gt(0)').items()
                for tr in trs:
                    ip = tr.find('td:nth-child(1)').text()
                    port = tr.find('td:nth-child(2)').text()
                    yield ':'.join([ip, port])

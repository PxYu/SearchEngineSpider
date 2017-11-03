__author__ = 'pxyuwhu'

from scrapy.spiders import Spider
from SearchEngineSpider.common.searchEngines import SearchEngineResultSelectors
from SearchEngineSpider.common.searchEngines import SearchEngines
from scrapy.selector import  Selector
import urlparse
import os
import urllib
from .. import settings

class keywordSpider(Spider):
    name = 'keywordSpider'
    allowed_domains = ['google.com', 'google.ca', 'google.jp', 'google.com.hk']
    start_urls = []
    script_dir = os.path.dirname(__file__)
    searchEngine = None
    searchEngineUrl = None
    selector = None
    max_limit = settings.TOP_N
    
    def __init__(self, keyword_file, se = 'google', *args, **kwargs):
        super(keywordSpider, self).__init__(*args, **kwargs)
        self.searchEngine = se.lower()
        self.searchEngineUrl = SearchEngines[self.searchEngine]
        abs_file_path = os.path.abspath(os.path.join(self.script_dir, "..", "..", keyword_file))
        print abs_file_path
        with open(abs_file_path) as f:
            for line in f:
                self.start_urls.append(self.searchEngineUrl.format(urllib.quote(line.rstrip())))
        self.selector = SearchEngineResultSelectors[self.searchEngine]

    def parse(self, response):
        items = Selector(response).xpath(self.selector)
        length = len(items)
        for index, item in enumerate(items[0: min(length, self.max_limit)]):
            yield {
                    "idx": index + 1,
                    "title": item.xpath('normalize-space(string(h3/a))').extract()[0],
                    "url": item.xpath('h3/a/@href').extract()[0],
                    "snippet": "".join(item.xpath('div[@class="s"]/div/span[@class="st"]//text()[not(parent::span[@class="f"]) and normalize-space()]').extract()),
                    "query": urlparse.parse_qs(urlparse.urlparse(response.url).query)['q'][0]
                }
        pass

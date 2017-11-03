__author__ = 'tixie'

SearchEngines = {
    # 'google': 'http://www.google.ca/search?q={0}&start={1}',
    'google': 'http://www.google.ca/search?q={0}&gws_rd=ssl',
    'bing': 'http://www.bing.com/search?q={0}&first={1}',
    'baidu': 'http://www.baidu.com/s?wd={0}&pn={1}'
}


SearchEngineResultSelectors= {
    'google': '//div[@class="rc"]',
    'bing':'//h2/a/@href',
    'baidu':'//h3/a/@href',
}
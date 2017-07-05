import urlparse

import scrapy

def get(response, selector):
    return response.css(selector).extract_first()

def get_element(response, selector):
    return response.css(selector)

def get_url(response, selector):
    url = response.css(selector).extract_first()
    if url is None:
        return None
    return urlparse.urljoin(response.url, url)

class Spider(scrapy.Spider):

    def __init__(self, start=None, end=None):
        if start is None:
            raise Exception('start is required')
        if end is None:
            raise Exception('end is required')
        self.start = int(start)
        self.end = int(end)

    def start_requests(self):
        for i in range(self.start, self.end):
            url = self.url_format.format(i)
            yield scrapy.Request(url)

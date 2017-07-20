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

    def __init__(self, n=None):
        if n is None:
            raise Exception('n is required')
        self.n = int(n)

    def start_requests(self):
        start = self.n * 1000
        end = start + 1000
        for i in range(start, end):
            url = self.url_format.format(i)
            yield scrapy.Request(url)

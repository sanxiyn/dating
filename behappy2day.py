import urlparse

import scrapy

def get(response, selector):
    return response.css(selector).extract_first()

def get_url(response, selector):
    url = response.css(selector).extract_first()
    return urlparse.urljoin(response.url, url)

class BeHappy2daySpider(scrapy.Spider):
    name = 'behappy2day'

    def __init__(self, start=None, end=None):
        if start is None:
            raise Exception('start is required')
        if end is None:
            raise Exception('end is required')
        self.start = int(start)
        self.end = int(end)

    def start_requests(self):
        for i in range(self.start, self.end):
            url = 'https://www.behappy2day.com/girls_info.php?i={}'.format(i)
            yield scrapy.Request(url)

    def parse(self, response):
        id = get(response, 'table#tbl_ tr:nth_child(1) td:nth_child(2)::text')
        location = get(response, 'table#tbl_ td a::text')
        city, country = location.split(', ')
        url = get_url(response, 'img.sp_menu_avatar::attr(src)')
        yield {'id': id, 'country': country, 'city': city, 'url': url}

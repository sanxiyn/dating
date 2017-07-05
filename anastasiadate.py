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

class AnastasiaDateSpider(scrapy.Spider):
    name = 'anastasiadate'

    def __init__(self, start=None, end=None):
        if start is None:
            raise Exception('start is required')
        if end is None:
            raise Exception('end is required')
        self.start = int(start)
        self.end = int(end)

    def start_requests(self):
        for i in range(self.start, self.end):
            url = 'http://www.anastasiadate.com/pages/lady/profile/profilepreview.aspx?LadyId={}'.format(i)
            yield scrapy.Request(url)

    def parse(self, response):
        if 'profile-is-unavailable' in response.url:
            return
        _, id = get(response, 'div.lady-id span::text').split(': ')
        location = get_element(response, '.ladyProfile-content td:nth-child(2) div:nth-last-child(2)')
        _, city, country = (text.strip('\r\n ,') for text in location.css('::text').extract())
        url = get_url(response, '.lady-star-name div.lady-thumbnail-container img::attr(href)')
        if url is None:
            return
        yield {'id': id, 'country': country, 'city': city, 'url': url}

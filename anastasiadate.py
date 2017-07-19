from base import Spider
from base import get, get_element, get_url

not_available = "Therefore, it won't be available for a couple of days."

class AnastasiaDateSpider(Spider):
    name = 'anastasiadate'
    url_format = 'http://www.anastasiadate.com/pages/lady/profile/profilepreview.aspx?LadyId={}'

    def parse(self, response):
        if 'profile-is-unavailable' in response.url:
            return
        if not_available in response.body:
            return
        _, id = get(response, 'div.lady-id span::text').split(': ')
        location = get_element(response, '.ladyProfile-content td:nth-child(2) div:nth-last-child(2)')
        _, city, country = (text.strip('\r\n ,') for text in location.css('::text').extract())
        url = get_url(response, '.lady-star-name div.lady-thumbnail-container img::attr(href)')
        if url is None:
            return
        yield {'id': id, 'country': country, 'city': city, 'url': url}

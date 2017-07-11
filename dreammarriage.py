from base import Spider
from base import get, get_url

class DreamMarriageSpider(Spider):
    name = 'dreammarriage'
    url_format = 'https://www.dream-marriage.com/{}.html'

    def parse(self, response):
        if 'inactive' in response.url:
            return
        if 'Access denied' in response.body:
            return
        if 'Invalid Profile ID' in response.body:
            return
        _, id = get(response, 'h1::text').split(': ')
        country = get(response, 'div.top_wrapper table tr:nth-child(3) td:nth-child(2)::text')
        city = get(response, 'div.top_wrapper table tr:nth-child(2) td:nth-child(2)::text')
        url = get_url(response, 'div.profile-photos > a img::attr(src)')
        yield {'id': id, 'country': country, 'city': city, 'url': url}

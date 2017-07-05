from base import Spider
from base import get, get_url

class Jump4loveSpider(Spider):
    name = 'jump4love'
    url_format = 'https://j4l.com/user_{}.love'

    def parse(self, response):
        id = get(response, 'div.profile-id::text').strip()
        country = get(response, 'div.profile-data div:nth-child(1) div:nth-child(1)::text').strip()
        city = get(response, 'div.profile-data div:nth-child(1) div:nth-child(2)::text').strip()
        url = get_url(response, '.photo-main img::attr(src)')
        yield {'id': id, 'country': country, 'city': city, 'url': url}

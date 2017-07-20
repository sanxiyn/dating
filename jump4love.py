from base import Spider
from base import get, get_element, get_url

class Jump4loveSpider(Spider):
    name = 'jump4love'
    url_format = 'https://j4l.com/user_{}.love'

    def parse(self, response):
        id = get(response, 'div.profile-id::text').strip()
        data = get_element(response, 'div.profile-data div div')
        keys = (text.strip(':') for text in data.css('span::text').extract())
        values = (text.strip() for text in data.css('div::text').extract())
        map = dict(zip(keys, values))
        country = map['Country']
        city = map['City']
        hair = map['Hair color']
        eye = map['Eye color']
        url = get_url(response, '.photo-main img::attr(src)')
        yield {'id': id, 'country': country, 'city': city, 'hair': hair, 'eye': eye, 'url': url}

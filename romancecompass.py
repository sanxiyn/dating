from base import Spider
from base import get, get_element, get_url
from utils import clean, transliterate

class RomanceCompassSpider(Spider):
    name = 'romancecompass'
    url_format = 'https://romancecompass.com/gallery/profile/{}/'

    def parse(self, response):
        _, id = get(response, 'div.user-id::text').strip().split(': ')
        data = get_element(response, 'div.params div div')
        keys = (text.strip(': ') for text in data.css('div::text').extract())
        values = (clean(text).strip() for text in data.css('span::text').extract())
        map = dict(zip(keys, values))
        location = map['Residence']
        city, country = location.split(', ')
        country = country.strip()
        city = city.strip()
        city = transliterate(city)
        hair = map['Hair color']
        eye = map['Eye color']
        url = get_url(response, 'div.picture img::attr(src)')
        yield {'id': id, 'country': country, 'city': city, 'hair': hair, 'eye': eye, 'url': url}

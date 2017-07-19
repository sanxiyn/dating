from base import Spider
from base import get, get_url
from utils import transliterate

class RomanceCompassSpider(Spider):
    name = 'romancecompass'
    url_format = 'https://romancecompass.com/gallery/profile/{}/'

    def parse(self, response):
        _, id = get(response, 'div.user-id::text').strip().split(': ')
        location = get(response, 'div.params div:nth-child(1) div:nth-child(1) span::text')
        city, country = location.split(', ')
        country = country.strip()
        city = city.strip()
        city = transliterate(city)
        url = get_url(response, 'div.picture img::attr(src)')
        yield {'id': id, 'country': country, 'city': city, 'url': url}

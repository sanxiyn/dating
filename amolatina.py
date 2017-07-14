import json

from base import Spider

class AmoLatinaSpider(Spider):
    name = 'amolatina'
    url_format = 'https://api.amolatina.com/users/{}24'

    def parse(self, response):
        user = json.loads(response.body)
        id = user['id']
        country = user['country']
        city = user['city']
        url = '{}/photos/{}.125x125.thumb-fd'.format(response.url, user['thumbnail'])
        yield {'id': id, 'country': country, 'city': city, 'url': url}

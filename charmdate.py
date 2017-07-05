from base import Spider
from base import get, get_url

sorry = 'Sorry, the profile of this lady has already been removed from our website!'

class CharmDateSpider(Spider):
    name = 'charmdate'
    url_format = 'http://www.charmdate.com/photogallery/woman.php?womanid=C{}'

    def parse(self, response):
        if sorry in response.body:
            return
        _, id = get(response, 'h1::text').strip(' ()').split(': ')
        id = id[1:]
        location = get(response, '.b_bountry::text').strip()
        city, country = location.split(', ')
        url = get_url(response, 'div.pro_l_pht a img::attr(src)')
        yield {'id': id, 'country': country, 'city': city, 'url': url}

from base import Spider
from base import get, get_element, get_url

class BeHappy2daySpider(Spider):
    name = 'behappy2day'
    url_format = 'https://www.behappy2day.com/girls_info.php?i={}'

    def parse(self, response):
        data = get_element(response, 'table#tbl_ tr')
        keys = (text.strip('* ') for text in data.css('td:nth-child(1)::text').extract())
        values = (text.strip() for text in data.css('td:nth-child(2)::text').extract())
        map = dict(zip(keys, values))
        id = map["Lady's ID"]
        location = get(response, 'table#tbl_ td a::text')
        city, country = location.split(', ')
        hair = map['Hair Color'].lower()
        eye = map['Eye Color'].lower()
        url = get_url(response, 'img.sp_menu_avatar::attr(src)')
        yield {'id': id, 'country': country, 'city': city, 'hair': hair, 'eye': eye, 'url': url}

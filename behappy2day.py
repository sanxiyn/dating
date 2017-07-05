from base import Spider
from base import get, get_url

class BeHappy2daySpider(Spider):
    name = 'behappy2day'
    url_format = 'https://www.behappy2day.com/girls_info.php?i={}'

    def parse(self, response):
        id = get(response, 'table#tbl_ tr:nth-child(1) td:nth-child(2)::text')
        location = get(response, 'table#tbl_ td a::text')
        city, country = location.split(', ')
        url = get_url(response, 'img.sp_menu_avatar::attr(src)')
        yield {'id': id, 'country': country, 'city': city, 'url': url}

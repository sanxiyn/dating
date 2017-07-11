from base import Spider
from base import get, get_element, get_url

class AsianGirlsOnlineSpider(Spider):
    name = 'asiangirlsonline'
    url_format = 'https://www.asian-girls-online.com/{}.php'

    def parse(self, response):
        if 'displayInactiveError' in response.url:
            return
        head = get_element(response, 'div.profilehead')
        _, id = (text.strip() for text in head.css('::text').extract())
        _, id = id.split(': ')
        country = get(response, 'table.personal-info-table tr:nth-child(3) td:nth-child(3)::text')
        city = get(response, 'table.personal-info-table tr:nth-child(2) td:nth-child(3)::text')
        url = get_url(response, 'div.photo-wrapper img::attr(src)')
        yield {'id': id, 'country': country, 'city': city, 'url': url}

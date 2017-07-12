from base import Spider
from base import get, get_url

error = 'Undefined offset'

class DreamConnectionsSpider(Spider):
    name = 'dreamconnections'
    url_format = 'http://www.dreamconnections.com/ladies/profile/index.php?ladiesID={}'

    def parse(self, response):
        if error in response.body:
            return
        id = get(response, 'table.ladies-info-table tr:nth-child(1) td:nth-child(1) span::text')
        url = get_url(response, 'img#lprof-main::attr(src)')
        yield {'id': id, 'url': url}

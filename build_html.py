import json

sites = {
    'anastasiadate': 'http://www.anastasiadate.com/pages/lady/profile/profilepreview.aspx?LadyID={}',
    'asiandate': 'http://www.asiandate.com/pages/lady/profile/profilepreview.aspx?LadyID={}',
    'charmdate': 'http://www.charmdate.com/photogallery/woman.php?womanid=C{}',
    'behappy2day': 'https://www.behappy2day.com/girls_info.php?i={}',
    'romancecompass': 'https://romancecompass.com/gallery/profile/{}/',
    'jump4love': 'https://j4l.com/user_{}.love',
}

def read(filename):
    result = []
    with open(filename) as f:
        for line in f:
            item = json.loads(line)
            result.append(item)
    return result

def write(items, args):
    with open(args.output, 'w') as f:
        for item in items:
            id = item['id']
            link = sites[args.site].format(id)
            url = item['url']
            url = url.encode('utf-8')
            f.write('<a href="{}"><img src="{}"></a>\n'.format(link, url))

import argparse
parser = argparse.ArgumentParser()
parser.add_argument('site')
parser.add_argument('input')
parser.add_argument('output')
args = parser.parse_args()

items = read(args.input)
write(items, args)

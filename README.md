You need to have [Scrapy](https://scrapy.org/) installed. Example usage:

```
$ scrapy runspider -a start=30000 -a end=31000 -o behappy2day-30k.jl behappy2day.py
$ cat behappy2day-30k.jl | jq -c 'select(.country == "Ukraine") | {id, url}' | head -n 40 > UA.jl
$ python download.py UA.jl UA
$ python build_html.py behappy2day UA.jl UA.html
```

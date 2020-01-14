import simplejson as json
import urllib.request as req
import os.path

# url
url = 'https://api.github.com'
savename = 'C:/python/webcrolling/section4/webcrolling_section4/gitrego.json'

if not os.path.exists(savename):
    req.urlretrieve(url, savename)

items = json.load(open(savename, 'r', encoding='utf-8'))
# items = json.loads(open(savename, 'r', encoding='utf-8')).read()
# print(items)
# 출력
# for item in items:
#     print(item["full_name"] + " - " + item["owner"]["url"])

'''
爬取拉钩网中的信息
当前本机的 headers
Mozilla/5.0 (Windows NT 6.1; Win64; x64; rv:67.0) Gecko/20100101 Firefox/67.0
'''
from urllib import request

url = r'http://www.lagou.com/zhaopin/Python/?labelWords=label'
headers = {'User-Agent': r'Mozilla/5.0 (Windows NT 6.1; Win64; x64; rv:67.0) Gecko/20100101 Firefox/67.0',
           'Referer': r'http://www.lagou.com/zhaopin/Python/?labelWords=label',
           'Connection': 'keep-alive'}
req = request.Request(url, headers=headers)
page = request.urlopen(req).read()
page = page.decode("utf-8")
print(page)
'''
爬取拉钩网中的信息
当前本机的 headers
Mozilla/5.0 (Windows NT 6.1; Win64; x64; rv:67.0) Gecko/20100101 Firefox/67.0
对获取的信息进行解析
'''
from urllib import request,parse

url = r'http://www.lagou.com/zhaopin/Python/?labelWords=label'
headers = {'User-Agent': r'Mozilla/5.0 (Windows NT 6.1; Win64; x64; rv:67.0) Gecko/20100101 Firefox/67.0',
           'Referer': r'http://www.lagou.com/zhaopin/Python/?labelWords=label',
           'Connection': 'keep-alive'}

#设置data参数进行方法为 post 的访问
data = {'first':'true', 'pn' : 1, 'kd' : 'Python'}
data = parse.urlencode(data).encode('utf-8')
req = request.Request(url, headers=headers, data = data)
#读取数据
page = request.urlopen(req).read()
page = page.decode('utf-8')
print(page)
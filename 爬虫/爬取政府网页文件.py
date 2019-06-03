'''
爬取:一个政府的文件
网址：http://www.gov.cn/zhengce/content/2019-06/03/content_5397093.htm
author:nianzuochen
date:20190603
'''

import requests
import bs4
from bs4 import BeautifulSoup

url = r'http://www.gov.cn/zhengce/content/2019-06/03/content_5397093.htm'
headers = {'User-Agent': r'Mozilla/5.0 (Windows NT 6.1; Win64; x64; rv:67.0) Gecko/20100101 Firefox/67.0',
           'Referer': r'http://www.lagou.com/zhaopin/Python/?labelWords=label',
           'Connection': 'keep-alive'}
# 向服务器发送请求
r = requests.get(url, headers=headers)
print(r.encoding)  # 打印编码格式
r.encoding = 'utf-8'
print(r.text)

#输出指定的内容
soup = BeautifulSoup(r.text, 'lxml', from_encoding='utf-8')
#输出标签名
print(soup.title)
print(soup.title.string)
print(soup.title.get_text())
#打印正文内容
texts = soup.find_all('p')
for text in texts:
    print(text.string)

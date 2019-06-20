'''
date : 20190619
author : nianzuochen
function : 爬取淘宝中的运动衫信息
url = r'https://uland.taobao.com/sem/tbsearch?refpid=mm_26632258_3504122_32538762&clk1=cdc880d9dd081650914dd9f095c0912d&keyword=%E8%BF%90%E5%8A%A8%E8%A1%AB&page=0'
'''

import requests
import bs4
from bs4 import BeautifulSoup

# 根据给定的 url 获取整个页面信息
def getHtmlText(url):
    try:
        headers = {'User-Agent': r'Mozilla/5.0 (Windows NT 6.1; Win64; x64; rv:67.0) Gecko/20100101 Firefox/67.0',
                   'Referer': r'http://www.lagou.com/zhaopin/Python/?labelWords=label',
                   'Connection': 'keep-alive'}
        #生成Response对象
        r=requests.get(url, headers=headers)
        #检查是不是200不是产生异常
        r.raise_for_status()
        #确认编码类型
        r.encoding = r.apparent_encoding
        return r.text
    except:
        return ""

'''
爬取 世界最好大学的排名
网址：http://www.zuihaodaxue.cn/ARWU2018.html
author:nianzuochen
date:20190603
func:爬取全世界的最好大学的排名信息
'''
import requests
import bs4
from bs4 import BeautifulSoup

#beautifulsoup4 库使用的时候使用缩写 bs4
#爬取网页内容
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

#根据内容分析并存储到列表中
def cunNeiRong(ls,html):
    #用BeautifulSoup的parse解析器解析网页
    soup = BeautifulSoup(html,'html.parser')
    #将tbody的儿子结点返回列表类型
    t_list = list(soup.find('tbody').contents)
    for tr in t_list:
        if isinstance(tr,bs4.element.Tag):#判断数据类型是否一样
            tds = tr('td') #这是简写，完整写法是  tds = tr.find_all('td')
            ls.append([tds[0].string,tds[1].string,tds[3].string,tds[4].string])

#把内容以容易理解清晰的表现输出出来
def printNeiRong(ls):
    print(u"学校排名")
    for i in range(100):
        s = ls[i]
        #格式化输出
        print('%-5s%-15s%-10s%-5s'%(s[0], s[1], s[2], s[3]))


def main():
    ls = [] #存储信息
    url = r'http://www.zuihaodaxue.cn/ARWU2018.html'
    bestschools = getHtmlText(url)
    cunNeiRong(ls,bestschools)
    printNeiRong(ls)

main()
'''
爬取 NBA 的排名信息
网址：https://nba.hupu.com/standings
author:wudidate:20180905
func:从新闻中爬取NBA排名
'''
import requests
import bs4
from bs4 import BeautifulSoup

#beautifulsoup4 库使用的时候使用缩写 bs4
#爬取网页内容
def getHtmlText(url):
    try:
        #生成Response对象
        r=requests.get(url)
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
            if tr.find('td').string == u'东部' or tr.find('td').string == u'西部':
                continue
            tds = tr('td') #这是简写，完整写法是  tds = tr.find_all('td')
            ls.append([tds[0].string,tds[1].string,tds[2].string,tds[3].string,tds[4].string,tds[12].string,tds[13].string])

#吧内容以容易理解清晰的表现输出出来
def printNeiRong(ls):
    print(u"东部排名")
    #循环打出NBA东部排名前15
    for i in range(16):
        s = ls[i]
        #格式化输出
        print('%-5s%-8s%-5s%-5s%-5s'%(s[0], s[1], s[2], s[3], s[4]))

def main():
    ls = [] #存储信息
    url = r'https://nba.hupu.com/standings'
    NBA = getHtmlText(url)
    cunNeiRong(ls,NBA)
    printNeiRong(ls)

main()
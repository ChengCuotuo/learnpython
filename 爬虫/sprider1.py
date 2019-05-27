'''
发送请求获取响应，响应的内容是整个网页的源代码，将源代码打印
当爬取次数很多的时候需要设置请求头，伪装成浏览器访问

'''

from urllib import request

#打开一个连接
response = request.urlopen(r'http://nianzuochen.cn')
#读取信息
page = response.read()
page = page.decode("utf-8")
print(page)
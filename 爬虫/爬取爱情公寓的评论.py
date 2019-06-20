import requests
import time
import random
import json

#获取每一页数据
def get_one_page(url) :
    response = requests.get(url=url);
    if response.status_code == 200:
        return  response.text;
    return '';

#解析每一页数据
def parse_one_page(html):
    data = json.loads(html)['cmts'] #获取评论内容
    for item in data:
        yield{'date':item['time'].split(' ')[0], 'nickname':item['nickName'], 'city':item['cityName'],
              'rate':item['score'], 'content':item['content']}

#保存到文本文档中
def save_to_text():
    for i in range(1, 10):
        print("开始保存地%d页"%i);
        url = "http://m.maoyan.com/mmdb/comments/movie/1175253.json?_v_=yes&offset=" + str(i); #爱情公寓
        #url = "http://m.maoyan.com/mmdb/comments/movie/248172.json?_v_=yes&offset=" + str(i); #复仇者联盟
        html = get_one_page(url)
        for item in parse_one_page(html):
            with open('爱情公寓.txt', 'a', encoding='utf-8') as f:
                f.write(item['date'] + ", " + item['nickname'] + ", " + item['city'] + ", "
                        + str(item['rate']) + ", " + item['content'] + "\n")
    time.sleep(random.randint(1, 100) / 20);


save_to_text();
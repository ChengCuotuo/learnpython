import itchat
import time
#自动登录微信
itchat.auto_login(hotReload=True)
#获取用户的所有的朋友信息
friends = itchat.get_friends(update=True);
#输出微信好友的信息
for fr in friends:
    #print(fr["UserName"])
    #print(fr["Sex"])
    print(fr["NickName"])

def send_mess(friends):
    # 给所有的好友发信息
    #for fr in friends:
        #itchat.send(u"你好,%s"%fr["DisplayName"] or fr["NickName"], fr["UserName"])
    #给指定的人发信息
    user = itchat.search_friends(name="Gws")
    username = user[0]["UserName"]
    for i in range(2000):
        itchat.send(u"跪着唱征服", toUserName=username)
        time.sleep(1)

#send_mess(friends)

'''
碾作尘
春风
卍戒酒的李白卍
英琦
我是传奇
(´O｀)
死地豪杰
kawhi
晓
谷中风
勿语°
杨艳
角落
张振
〒_〒
随穆
Imut
Best Express_Vip.Lee
阳光
爱的华尔兹
潘云超
Wool
拾安
一见倾心
Alice的鲸
Ringo·Sun
传义
筱磊
家园
雨路
王诚民
zcc
赵桐
sweet
小臭臭👼
谜.
胡骞宇
凉白开
瑞梅同学
谨此而已
奔儿
fairy🎈
NULL
别说话。。。嘘
🌜
长发绾君心§
YangJing
S--丽丽
King
yzm小蹦蹬😊~
Sgamer
奇点
馒头
子龙
若风
朱航
浪迹天涯
艾薇儿的冰红茶
在路上
怿儿
微笑呀
然
倩🐾
🐼
H
€.張...
开心就好
漁灵
琪.
左
我是你楠神
尾号9527🍻 🇩
安然
嘿嘿
张福贵
糖糖
凌子雯
大数据技术顾问-小新老师
악  군 🇩⁶⁶⁶
俊之假面士
球
LiuBo
L&amp;S
安稳。
七分软萌
扣儿💋(支持花呗)
Harleen
刘休想
婷
小冬
海岛有猫🐱
长街听风
A 奶酪🎀
白芽灿灿🍀 🍀
伊莎贝拉蝶
姜文
任你！
anyhow
谢**
🐨
Your Boy
❇  蜡笔小新 ❇
追忆
条条
QDNET！
宋孝哲
Â 👾  .
🌛
老爷子
蓝桥
沙雕网友最快乐~
老郭
👧
章丘
🔑 Coisni
青春
决明子
oval
'''

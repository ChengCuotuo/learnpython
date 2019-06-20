'''
作业：每天早上7点和晚上10点给指定的人发送信息
每天早上七点的时候给 怿儿 发送信息：早安、晚安
'''

import itchat
import time
import datetime

#自动登录微信
itchat.auto_login(hotReload=True)
#获取所有的好友信息
friends = itchat.get_friends(update=True)

#方法：给指定用户发送信息
def sendMessage(friends, friendName):
    #获取指定的昵称的用户的信息
    user = itchat.search_friends(name=friendName)
    #提取用户信息中的用户名，该用户名是经过加密的
    username = user[0]["UserName"]
    #一直发送指定的信息
    while True:
        #获取当前时间
        now = datetime.datetime.now()
        #print(now) #2019-03-04 21:47:09.242305
        #将获取的时间先按照指定的格式进行格式化，此时省去秒后面的内容
        #再获取从第11位开始的内容，也就是时分秒
        now_str = now.strftime('%Y/%m/%d %H:%M:%S')[11:]
        #print(now_str) #21:47:09
        #当当前的时间和指定的时间（07:00:00）相同时候，发送信息
        if now_str in ['07:00:00']:
            itchat.send(u'早安', toUserName=username)
            #微信好友性别分析.send(u'你好', 'filehelper')
        if now_str in ['22:00:00', toUserName=username]:
            itchat.send(u'晚安');
        time.sleep(1)

#调用方法
sendMessage(friends, u"怿儿")
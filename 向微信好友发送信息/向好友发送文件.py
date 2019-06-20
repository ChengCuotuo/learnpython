import itchat
import time
#自动登录微信
itchat.auto_login(hotReload=True)
#获取用户的所有的朋友信息
friends = itchat.get_friends(update=True);
'''
#输出微信好友的信息
for fr in friends:
    print(fr["UserName"])
    print(fr["Sex"])
    print(fr["NickName"])
'''

def send_mess(friends, myfriend):
    #给指定的人发信息
    user = itchat.search_friends(name=myfriend)
    username = user[0]["UserName"]
    print(username)
    for i in range(1):
        itchat.send(u"老师说上节课发给谁，这节课就发给谁", toUserName=username)
        #发送照片
        itchat.send_image("dog.jpg", username)
        #发送文件
        itchat.send_file("dog.txt", username)
        #发送视频
        itchat.send_video("haha.mp4", username)
        time.sleep(1)

send_mess(friends, "L&amp;S")

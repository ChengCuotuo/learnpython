'''
    图灵机器人，使用在微信
    作业：指定好友回复
'''
import itchat
import requests

def get_response(msg):
    apiUrl = 'http://www.tuling123.com/openapi/api'
    # Tuling Key API的值# 发出去的消息# 用户名
    data = {'key': '8134a6642e354f1ea24521879c8b6f55', 'info': msg, 'userid': '430707',}
    r = requests.post(apiUrl, data=data).json() #post 请求
    return r.get('text');

#用于接收来自朋友间的对话消息
@itchat.msg_register(itchat.content.TEXT)
#isGroupChat=True 该参数判断是否是群消息
#当接收到微信的消息的时候，执行下面的代码
def print_content(msg):
    #指定好友
    if msg.User['NickName'] == '士博':
        return get_response(msg['Text'])
    
itchat.auto_login() #微信扫描二维码登录
itchat.run();


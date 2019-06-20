import itchat
from pyecharts import Map   #省份
from collections import Counter #统计信息
import os   #文件路径
import PIL.Image as Image    #图片处理
import math     #数学计算
import TencentYoutuyun
import os   #文件路径
import re

#自动登录微信
itchat.auto_login(hotReload=True)
#获取用户的所有的朋友信息
friends = itchat.get_friends(update=True)

#获取好友的头像
def headimg():
    base_path='headimg' #放置头像的文件
    #判断文件是否存在，不存在就新建
    if not os.path.exists(base_path):
        os.mkdir(base_path)
    #将每张好友 的头像都写入img这个文件夹下
    for count, f in enumerate(friends):
        img=itchat.get_head_img(userName=f['UserName'])
        img_name=f['NickName'] if f['NickName']!='' else f['NickName']
        img_file=os.path.join(base_path, str(img_name).replace("*", "").replace(".", "").replace(":", "") + '.jpg')
        #按照用户的备注名命名文件，没有备注的用数字
        imgFile=open(img_file, 'wb')
        imgFile.write(img)
        imgFile.close();

appid = '10174324'
secret_id = 'AKIDhkpmyrD8g3HLG47zQii7QdhZGAysKmsv'
secret_key = 'y1UwLZN2gAQcDpiaL1eAgCpcID02wwrB'
userid = '924271966'
end_point = TencentYoutuyun.conf.API_YOUTU_END_POINT #优图的开方平台
youtu=TencentYoutuyun.YouTu(appid, secret_id, secret_key, userid, end_point)

def analyseFace():
    base_path = "headimg"
    find = []
    for file_name in os.listdir(base_path):
        result = youtu.DetectFace(os.path.join(base_path, file_name))
        find = list(set(find))
        if result['errorcode'] == 0:  # 是 0 表示是人脸
            gender = '男' if result['face'][0]['gender'] >= 50 else '女'
            age = result['face'][0]['age']  # 年龄
            beauty = result['face'][0]['beauty']  # 颜值
            print("昵称：%s, 性别：%s, 年龄：%d, 颜值：%d"%(file_name[:-4], gender, age, beauty))  # 用 , 间隔

headimg()
analyseFace()

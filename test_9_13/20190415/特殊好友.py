'''
    屏蔽好友和星标好友
'''
import itchat

#自动登录微信
itchat.auto_login(hotReload=True)
#获取用户的所有的朋友信息
friends = itchat.get_friends(update=True)

def get_var(var):
    variable=[] #存储好友的某一列信息
    for fi in friends:
        value=fi[var]   #临时存储好友指定列的信息
        variable.append(value)
    return variable #返回所有好友指定列的信息

def create_starf(NickName,StarFriend,ContactFlag):
    star_list=[]
    deny_see_list=[]
    no_see_list=[]

    for sid,val in enumerate(StarFriend):
        if val == 1:
            star_list.append(NickName[sid])
    for sid, val in enumerate(ContactFlag[1:]):
        #表示将对方屏蔽
        if val in ['259', '33027', '65795']:
            deny_see_list.append(NickName[sid])
        #表示自己被谁屏蔽
        if val in ['65539', '65795']:
            no_see_list.append(NickName[sid])
    print("星标好友:",star_list)
    print("我屏蔽的好友", deny_see_list)
    print("把我屏蔽的好友", no_see_list)

StarFriend = get_var("StarFriend")
NickName = get_var("NickName")
ContactFlag = get_var("ContactFlag")
create_starf(NickName,StarFriend,ContactFlag)
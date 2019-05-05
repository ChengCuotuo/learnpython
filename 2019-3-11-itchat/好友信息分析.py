'''
    把好友的性别信息保存在txt中，对人数进行分析。
    分析内容：
        人数小于50，请多交朋友，小于10表明性格有些孤僻
        如果 男 > 女，表示，很受小哥哥们的青睐
        如果 女 > 男，表示，很受小姐姐的青睐
'''

import itchat

#自动登录微信
itchat.auto_login(hotReload=True)
#获取用户的所有的朋友信息
friends = itchat.get_friends(update=True)

#获取好友的某一列信息
def get_var(var):
    variable=[] #存储好友的某一列信息
    for fi in friends:
        value=fi[var]   #临时存储好友指定列的信息
        variable.append(value)
    return variable #返回所有好友指定列的信息

#将好友的信息处理保存到文件中
def analysze(fSex):
    sex = dict()  # 使用字典的形式存储信息
    total = len(friends[1:])
    # 提取好友性别
    for f in fSex:
        if f == 1:
            sex["man"] = sex.get("man", 0) + 1
        elif f == 2:
            sex["weman"] = sex.get("weman", 0) + 1
        else:
            sex["unknown"] = sex.get("unknown", 0) + 1
    info = "您的好友共有" + total + "人， 其中帅哥有" + sex["man"] + \
           "人，美女有" + sex["weman"] + "人，不明性别" + sex["unknown"] + "人"
    with open('分析.txt', 'wr', encoding='utf-8') as f:
        f.write(info)

gender=get_var("Sex")
analysze(gender)
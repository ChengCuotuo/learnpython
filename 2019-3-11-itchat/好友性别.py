'''
微信好友性别信息的可视化
'''
import itchat
from pyecharts import Line #画折线图
from pyecharts import Pie  #画饼状图

#自动登录微信
itchat.auto_login(hotReload=True)
#获取用户的所有的朋友信息
friends = itchat.get_friends(update=True);

#获取好友的某一列信息
def get_var(var):
    variable=[] #存储好友的某一列信息
    for fi in friends:
        value=fi[var]   #临时存储好友指定列的信息
        variable.append(value)
    return variable #返回所有好友指定列的信息

def create_sex(fSex):
    sex=dict() #使用字典的形式存储信息
    #提取好友性别
    for f in fSex:
        if f==1:
            sex["man"] = sex.get("man", 0) + 1
        elif f==2:
            sex["weman"] = sex.get("weman", 0) + 1
        else:
            sex["unknown"] = sex.get("unknown", 0) + 1
    #打印统计结果
    total = len(friends[1:])
    print("您的好友共有%d人， 其中帅哥有%d人，美女有%d人，不明性别%d人"%(total, sex["man"], sex["weman"], sex["unknown"]))
    #输出性别比例
    print("您的好友比例为：男%.2f%%，女%.2f%%"%(sex["man"]/total*100, sex["weman"]/total*100))
    drawPie(sex) #画饼状图
    dramLine(sex) #画折线图

# 画好友信息的饼状图
def drawPie(sex):
    total = len(friends[1:])
    attr = ["帅哥", "美女", "性别保密"]
    value = [sex["man"], sex["weman"], sex["unknown"]]
    pie = Pie("微信好友比例", "好友总人数%d" % total, title_pos="center")
    pie.add("", attr, value, radius=[30, 60], is_random=False, label_text_size=20,
            is_label_show=True, is_lengend_show=True)
    pie.show_config()
    pie.render("好友性别比例.html")

#画好友的性别比例的折线图
def dramLine(var):
    gen=["男", "女"]
    list=[]
    list.append(var.get("man"))
    list.append(var.get("weman"))
    line = Line("性别情况", "比例", title_color="red", title_pos="left", width=1200, height=600)
    line.add("Sex", gen, list,
             mark_point=['max', 'min'], mark_line=["average"],
             legend_text_color="red", is_label_show=True, is_datazoom_show=True, legend_pos="right",
             is_convert=False, label_pos="inside", is_smooth=True)
    line.render('性别比例.html')

gender=get_var("Sex")
create_sex(gender);

#输出名字NickName
nickName = get_var("NickName")
#print(nickName)




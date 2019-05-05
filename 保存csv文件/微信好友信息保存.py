'''
时间：20180503
码农：nianzuochen
功能：获取微信好友的信息：UserName, NickName, RemarkName,Signature,
    Province,City ,Sex,AttrStatus,ContactFlag 信息，保存在一个 info.csv 文件中

'''
import itchat           #连接微信
import pandas as pd     #处理 csv 文件
import re               #正则表达式

#自动登录微信
itchat.auto_login(hotReload=True)
#获取用户的所有的朋友信息
friends = itchat.get_friends(update=True)

#输入一个需要获取的属性值，返回一个 list
#attrs 中存储需要获取的信息的名称
def get_vars(attrs):
    #存储好友的所有的信息
    variable=[]
    for fi in friends:
        #存储一个好友指定的 attrs 信息
        fi_var = []
        for attr in attrs:
            #当信息为昵称、备注、个性签名的时候需要对非法字符进行处理
            # 使用正则表达式提取汉字
            # 1.获取 2.编译 3.替换
            if attr == 'NickName' or attr == 'RemarkName' or attr == 'Signature' :
                #获取原始信息，去除前后空格
                value = fi[attr].strip()
                #获取汉字的正则表达式编译器
                rec = re.compile("[^\u4e00-\u9fa5]")
                #将原始数据进行替换
                value = rec.sub("", value)
                #添加
                fi_var.append(value)
            else :
                fi_var.append(fi[attr])
        variable.append(fi_var)
    return variable

#需要获取的信息列
infoName = ['昵称', '备注', '个性签名', '省份', '城市', '性别', '唯一标识', '好友类型']
attrs = ['NickName', 'RemarkName','Signature', 'Province','City' ,'Sex','AttrStatus', 'ContactFlag']
info = get_vars(attrs)
#print(info)
#设置 csv 文件
csv_file = pd.DataFrame(columns=infoName, data=info)
#x写入文件，并指定未见编码,csv 文件用Excel打开的时候是表格形式，
# Excel表的默认编码格式为 ANSI 否则乱码，需要重新另存为 ANSI 文件
csv_file.to_csv("friendsInfo.csv", encoding='ANSI')
'''
好友所在的地方（省份和城市）
'''
import itchat
from pyecharts import Bar   #画柱状图
from pyecharts import Map   #省份
from collections import Counter #统计信息
from pyecharts import Geo #地理坐标图
from pyecharts import Bar #柱状图
import os   #文件路径
import PIL.Image as Image    #图片处理
import math     #数学计算

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

#获取好友的省份信息
def create_province(provinces):
    #创建字典保存信息
    a={}
    for i in provinces:
        a[i]=provinces.count(i);

    #对字典进行排序，是按照所在省份人数进行降序排序
    b=sorted(a.items(), key=lambda item:item[1], reverse=True)

    #将省份的名称和人数拆分
    attrs=[]; #省份名称
    values=[]; #数量
    j=0; #循环计数
    while j < len(b):
        if b[j][0]=='':
            attrs.append("不明省份");
            values.append(b[j][1]);
        else:
            attrs.append(b[j][0]);
            values.append(b[j][1]);
        j = j + 1;
    #将得到的信息进行分析处理
    analysis(attrs, values)

#分析并得到可视化的数据
def analysis(attrs, values):
    # 柱状图显示省份频率
    bar = Bar('好友省份分布图', '人数');  # 定义横纵坐标
    #由于省份过多，导致无法完全显示，所以需要将横坐标旋转60度
    bar.add('', attrs, values, mark_line=["average"], mark_point=['max', 'min'], lenged_txt_color='blue',xaxis_rotate=60);  # 对应横纵坐标把人名和次数绘制柱状图
    bar.render("provinces.html");  # 将绘制完成的柱状图保存为pername.html格式

    #省份地图
    map=Map("微信好友省份分布图",title_color="red", title_pos="left", width=1200, height=600);
    map.add("地图", attrs, values, visual_range=[0,50],maptype="china", is_visualmap=True, visual_text_color="#000");
    map.render("friendsinchina.html");

    # 将结果保存在文件中
    with open("provinces.txt", "w", encoding="utf-8") as f:
        f.write(friends[0]['NickName'] + ",你好，你的省份是：" + provinces[0]
                + "， 你的好友的省份比例如下：\n");
        j = 0;
        while j < len(attrs):
            f.write(attrs[j] + ":");
            f.write(str(values[j]) + "\n");
            j = j + 1;
        f.write(attrs[0] + "省好友最多，人数达到了 " + str(values[0]) + "个人，我猜你也在这个省份。");

#城市好友分布数量
def create_city(cities):
    #统计城市频率
    data=Counter(cities).most_common(10);
    print(data);

#显示好友的城市
def create_city(cities):
    fc=[]
    for v in cities:
        #对好友的城市进行数据清洗
        if v.strip() in ['海淀','丰台', '大兴', '昌平']:
            fc.append('北京')
        elif v=='延边':
            fc.append('延吉')
        elif v in ['', 'Newport', 'Melbourne']:
            pass
        else :
            fc.append(v)
    #print(cities)
    #print(fc)
    #统计人数最多的10个城市
    data=Counter(fc).most_common(10)
    #print(data)
    #生成地理坐标图
    geo = Geo('好友城市分布','可视化', title_color='#fff', title_pos='center', background_color='#404a59')
    attr,value=geo.cast(data)
    geo.add('',attr,value, visual_range=[0, 20], symbol_size=20, is_visualmap=True)
    geo.render("好友城市分布.html")
    bar = Bar('好友城市分布', '人数')
    bar.add('', attr, value, lenged_txt_color='blue')
    bar.render("好友城市的分布柱状图.html")

#获取好友的头像
def headimg():
    base_path='img' #防止头像的文件
    #判断文件是否存在，不存在就新建
    if not os.path.exists(base_path):
        os.mkdir(base_path)
    #将每张好友 的头像都写入img这个文件夹下
    for count, f in enumerate(friends):
        img=itchat.get_head_img(userName=f['UserName'])
        #img_name=f['RemarkName'] if f['RemarkName']!='' else f['RemarkName']
        img_file=os.path.join(base_path, str(count) + '.jpg')
        #按照用户的备注名命名文件，没有备注的用数字
        imgFile=open(img_file, 'wb')
        imgFile.write(img)
        imgFile.close();

#头像拼接
def createImg():
    x = 0 #每行第几个
    y = 0 #第几行
    #经文件夹下的图片读取到imgs中
    imgs = os.listdir('img')
    #创建拼接图片
    newImg = Image.new('RGBA', (680,680))
    #计算每张小图片的宽度
    width = int(math.sqrt(680*680/len(imgs)))
    numLine = int(680 / width)
    #开始放置图片
    for i in imgs:
        try:
            img=Image.open('img/'+i)
            img=img.resize((width, width), Image.ANTIALIAS)
            newImg.paste(img,(x*width, y*width))
            x += 1
            if x > numLine:
                x = 0
                y += 1
        except IOError:
            print("img/%s can't open"%(i))
    newImg.save("all.png")

#调用函数，获得好友的省份信息
#provinces = get_var('Province');
#获取好友省份的分布
#create_province(provinces);
#cities=get_var('City');
#create_city(cities);
headimg();
createImg();
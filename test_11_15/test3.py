'''
分词练习，使用jieba库
'''
import jieba
s = u'我是齐齐哈尔大学软件工程专业的老师'
cut_list = jieba.cut(s)
print('/'.join(cut_list))

cut_list = jieba.cut(s, cut_all=True)
print('/'.join(cut_list))

cut_list = jieba.cut(s, cut_all=False)
print('/'.join(cut_list))
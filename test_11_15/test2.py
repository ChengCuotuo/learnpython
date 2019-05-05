#encoding=utf-8
'''
结巴库的练习使用
各种模式
'''
import jieba

seg_list = jieba.cut(u'我来到北京清华大学', cut_all=True)
print ('Full Mode:', '/'.join(seg_list))#全模式

seg_list = jieba.cut(u'我来到北京清华大学', cut_all=False)
print ('Full Mode:', '/'.join(seg_list))#精确模式


seg_list = jieba.cut(u'我来到北京清华大学')
print ('Full Mode:', '/'.join(seg_list))#默认模式

seg_list = jieba.cut_for_search("小明硕士毕业于中国科学院计算所，后在日本京都大学深造") #搜索引擎模式
print (", ".join(seg_list))
'''
jieba库有优先级并不是完全按照指定的内容进行分析
'''

import jieba

jieba.load_userdict('userdic.txt') #导入自己的分词标准，自定义词典
s = '我是齐齐哈尔大学软件工程专业的学生'
cut_list = jieba.cut(s)
print('/'.join(cut_list))
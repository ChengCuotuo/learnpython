#水浒传分词

import jieba
#jieba.load_userdict('')

with open('水浒传.txt','r',encoding = 'utf-8') as f:
    str1=f.read()
    cut=jieba.cut(str1)
with open('reault.txt','w',encoding = 'utf-8') as f:
    f.write('%'.join(cut))

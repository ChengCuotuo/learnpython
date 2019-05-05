import jieba
from collections import Counter

#femci
with open('水浒传.txt','r',encoding = 'utf-8') as f:
    article=f.read()

words = jieba.cut(article)
#tong ji ci pin
c = Counter(words).most_common(100)
with open("result1.txt", "w", encoding="utf-8")as fw:
    for x in c:
        if len(x[0]) >= 2 and x[0] not in["　","Page","、","\n","『", "』", "；","；","“", "”", "！" ,
                       "？", "」", "「", "，", "。","-", "：", " ","的", "了"]:
            fw.write("{0},{1}\n".format(x[0], x[1]))
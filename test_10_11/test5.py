#!user/bin/python
#-*-coding:utf-8-*-
'''
编写人：王春雷
时间：2019.9.13
功能：数据字典
'''
def getScore(word):
       num = 0
       score={"a" : 1, "c" : 3, "b" : 3, "e" : 1, "d" : 2, "g": 2,
              "f" : 4, "i" : 1, "h" : 4, "k" : 4, "j" : 8}

       for ch in word:
              ch = ch.lower()
              num += score.get(ch)

       return num

print(getScore('aaaaaa'))

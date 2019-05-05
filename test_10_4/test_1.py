#!user/bin/python
#-*-coding:utf-8-*-
'''
编写人：王春雷
时间：2019.9.13
功能：统计字母个数
'''
list_words = list('When I came to college, I felt so excited about the new chapter of my life. '
                  'Now I will graduate soon. When I look back on the passed four years, '
                  'I gain so much knowledge. I have become stronger and are ready to face '
                  'the challenge of life. he greatest harvest of my college life is that I learn '
                  'the major knowledge and have the critical mind. The purpose of education is to '
                  'help us to be a better person, such as making the right judgement and being '
                  'independent. Now I can make my own decision and predict the result.'
                  ' I know what kind of responsibility I should take when I make my choice.'
                  ' It is an important sign of being an adult.')

list_char = list()#将26个字母添加到列表中
for ch in range(97, 123):
    list_char.append(chr(ch))


list_num = list()#用来统计个数的列表
for index in range(0, 26):
    list_num.append(list_words.count(list_char[index]))
    #从list_char中获取字母，在使用list_words的count统计个数，最后添加到统计列表list_num中

for index in range(0, 26):#输出统计结果
    print('%c出现%d次 ' %(list_char[index],list_num[index]))

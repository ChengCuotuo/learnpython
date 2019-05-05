'''
编写人：王春雷
时间：2019.9.13
功能：20个1到100之间不重复的数
'''

import random

a_set = []
while True:
    if len(a_set) == 20:
        break;
    n = random.randint(1, 100)
    if n not in a_set:
        a_set.append(n)
print('使用列表显示20个1到100之间不重复的数：')
print(a_set)
print(sorted(a_set))

x = set()
while len(x) < 20:
    x.add(random.randint(1, 100))
print('使用集合显示20个1到100之间不重复的数：')
print(x)
print(sorted(x))
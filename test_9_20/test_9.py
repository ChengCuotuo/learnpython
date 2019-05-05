'''
编写人：王春雷
时间：2019.9.13
功能：水仙花数字
'''

for i in range(100, 1000):
    first = i % 10
    second = i // 10 % 10
    third = i // 100
    if i == (first ** 3 + pow(second, 3) + pow(third, 3)):
        print(i)


for i in range(100, 1000):
    #这里是序列解包的用法
    bai, shi, ge = map(int, str(i))
    if bai ** 3 + shi ** 3 + ge ** 3 == i:
        print(i)
'''
编写人：王春雷
时间：2019.9.13
功能：计算1到100之和
'''

sum1 = int()
for i in range(1, 101):
    sum1 += int(i)

print("1到100的和是 %s" %sum1)


print("1到100的和是 %s" %sum(range(1, 101)))
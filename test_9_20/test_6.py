'''
编写人：王春雷
时间：2019.9.13
功能：小球跳跳
'''

high = float(100)
sum = float(0)
for i in range(10):
    sum = sum + high
    high = high / 2
    sum += high
print(u'小球弹起十次的总距离是：', end='')
print (sum - high)
print(u'最后的高度是：')
print(high)
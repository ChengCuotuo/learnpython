'''
编写人：王春雷
时间：2019.9.13
功能：99乘法表
'''

for i in range(1, 10):
    for j in range(1, i + 1):
        print('%d*%d=%d ' %(j, i, (i * j)), end='')

    print()

print()
print()
for i in range(1, 10):
    for j in range(i, 10):
        print('%d*%d=%d ' %(i, j, (i * j)), end ='')

    print()

print()
print()
for i in range(1, 10):
    for k in range(1, i):
        print('%2s' %' ', end='')
    for j in range(i, 10):
        print('%d*%d=%d ' %(i, j, (i * j)), end ='')

    print()

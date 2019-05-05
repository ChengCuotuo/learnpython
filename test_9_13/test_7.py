chTest=['1', '2', '3','4','5']
if chTest:
    print(chTest)
else:
    print('null')

a = 5
print(6) if a > 8 else print(5)

print(6 if a > 3 else 5)
b = 6 if a > 13 else 9
print(6)

a = input('输入数据结构的成绩：')
a = int(a)
if a > 0 and a < 100:
    if a > 90:
         print('优秀')
    elif a > 80:
        print('良好')
    elif a > 70:
        print('中等')
    elif a > 60:
        print('及格')
    else :
        print('不及格')
else:
    print('输入的值在0 到100之间')
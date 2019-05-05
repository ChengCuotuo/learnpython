'''
编写人：王春雷
时间：2019.9.13
功能：for 循环， in
'''

for x in range(0, 5):
    print("hello")

for x in range(0, 5):
    print('hello %s' %x)
    print(type(x))

wizard_list = ['splider legs', 'toe of frog', 'snail tongue', 'bat wing', 'slug butter', 'bear hurp']
for i in wizard_list:
    print(i)

for letter in 'Python':
    print(letter)
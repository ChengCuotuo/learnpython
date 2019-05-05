#!user/bin/python
#-*-coding:utf-8-*-
'''
编写人：王春雷
编写时间：2018.9.6
功能：解决鸡兔同笼问题
'''
heads = input ("input the number of heads:");
feet = input("input the numbers of feet") ;
heads = int(heads);
feet = int(feet);
rabit = (feet - 2 * heads) / 2;
chicken = heads - rabit;

print("rabbit : ", rabit);
print("chicken : " , chicken);
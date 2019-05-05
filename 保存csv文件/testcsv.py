'''
保存文件为 csv 文件
'''
import pandas as pd

list = [[1, 2, 3], [4, 5, 6], [7,8, 9]]

name = ['id', 'uid', 'time']

test = pd.DataFrame(columns=name, data=list)

test.to_csv('D:/test1.csv')


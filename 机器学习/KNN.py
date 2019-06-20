'''
机器学习的 knn 算法
需要安装的有 numpy scipy scikit-learn
'''

import numpy as np
from sklearn import neighbors

knn = neighbors.KNeighborsClassifier(n_neighbors=3)
#取得knn 分类器
data=np.array([[3, 104], [2, 100], [1, 81], [101, 10], [99, 5], [98, 2]])
#亲吻和打斗出现的次数
labels = np.array([1, 1, 1, 2, 2, 2])
#标记分类，前三个是1类，后三个是2类
knn.fit(data, labels)
#导入数据进行训练，data对应的打斗次数和亲吻的次数，而lables则是对应的Romance和
print(knn.predict([[19, 90]]))
# 表示输入的数据属于的类别是 [1]

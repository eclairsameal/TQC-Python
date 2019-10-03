# --開始--批改評分使用，請勿變動
set_seed = 123
# --結束--批改評分使用，請勿變動

import numpy as np

x = np.random.RandomState(set_seed).randint(low=5, high=16, size=15)
print('隨機正整數：', x)

x = x.reshape(3, 5)
print('X矩陣內容：')
print(x)

print('最大：', x.max())
print('最小：', x.min())
print('總和：', x.sum())
print('四個角落元素：')
print(x[np.ix_([0, 2], [0, 4])])

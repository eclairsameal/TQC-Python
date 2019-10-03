# --開始--批改評分使用，請勿變動
set_seed = 123
# --結束--批改評分使用，請勿變動

import numpy as np

x = np.random.RandomState(set_seed).randint(low=5, high=16, size=15)
print('隨機正整數：', ___)

x = x.reshape(___, ___)
print('X矩陣內容：')
print(___)
print('最大：', ___)
print('最小：', ___)
print('總和：', ___)
print('四個角落元素：')
print(x[np.ix_([___, ___], [___, ___])])

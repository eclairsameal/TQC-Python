# 載入 numpy 模組
import numpy as np
# 載入 pandas 模組縮
import pandas as pd

# 讀入 read.csv 檔案

npd = np.genfromtxt('read.csv', delimiter=',')

# 判斷資料型態
print('資料型態：%s' % type(npd))

# 計算平均數
print('平均值：%.2f' % np.mean(npd[1:]))

# 計算中位數
print('中位數：%.2f' % np.median(npd[1:]))
# 計算標準差
print('標準差：%.2f' % np.std(npd[1:]))
# 計算變異數
print('變異數：%.2f' % np.var(npd[1:]))
# 計算極差值
print('極差值：%.2f' % np.ptp(npd[1:]))

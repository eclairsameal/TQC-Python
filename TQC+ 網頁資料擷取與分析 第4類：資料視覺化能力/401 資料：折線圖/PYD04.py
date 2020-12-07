# -*- coding: utf-8 -*-
# --開始--批改評分使用，請勿變動
import matplotlib as mpl
mpl.use('Agg')
# --結束--批改評分使用，請勿變動

# 載入 matplotlib.pyplot 並縮寫為 plt
import matplotlib.pyplot as plt

data1 = [1, 4, 9, 16, 25, 36, 49, 64]
data2 = [1, 2, 3, 6, 9, 15, 24, 39]
seq = [1, 2, 3, 4, 5, 6, 7, 8]

# 數據及線條設定
plt.plot(seq, data1, 'ob--', seq, data2, 'or--', linewidth=1)
# 軸刻度
plt.axis([0, 8, 0, 70])
# 圖表標題
plt.title('Figure', fontsize = 24)
# X軸標題
plt.xlabel('x-Value', fontsize = 16)
# Y軸標題
plt.ylabel('y-Value',  fontsize = 16)

# 輸出圖片檔案
plt.savefig('chart.png')
plt.close()

# --開始--批改評分使用，請勿變動
import matplotlib as mpl
mpl.use('Agg')
# --結束--批改評分使用，請勿變動

from matplotlib import pyplot as plt
import numpy as np
import pandas as pd

# 讀取學生分數資料
# 讀取 read.csv
df = ___(___)
scores = df["___"].values

# range_count[0]: range0~19
# range_count[1]: range20~39
# range_count[2]: range40~59
# range_count[3]: range60~79
# range_count[4]: range80~100
# 以0初始化計數串列
range_count = [0] * 5

# 計數過程
for score in scores:
    if score < 20:
        range_count[0] += 1
    elif score < 40:
        range_count[1] += 1
    elif score < 60:
        range_count[2] += 1
    elif score < 80:
        range_count[3] += 1
    else:
        range_count[4] += 1

# y軸標籤
index = np.arange(___, ___, ___)
# X軸刻度
labels = [___, ___, '40~59', ___, '80~100']
# 畫出長條圖
plt.bar(___, range_count, ___)
# 設定X軸名稱
plt.xlabel('___', fontsize=___)
# 設定Y軸名稱
plt.ylabel('___', fontsize=___)
# 設定x軸標籤
plt.xticks(index, labels)
# 設定y軸標籤
plt.yticks(index)
# 設定圖名稱
plt.title('___', fontsize=___)
# 輸出圖片檔案
plt.___('___')
plt.close()

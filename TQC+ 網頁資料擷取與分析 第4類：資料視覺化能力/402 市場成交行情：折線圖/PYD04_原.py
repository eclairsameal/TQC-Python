# --開始--批改評分使用，請勿變動
import matplotlib as mpl
mpl.use('Agg')
# --結束--批改評分使用，請勿變動

# 載入 matplotlib.pyplot 並縮寫為 plt
import ___ as ___
# 載入 csv 模組
import ___

x = []
y = []

# 讀入 read.csv
with open('___', 'r', encoding='utf8') as csvfile:
    plots = csv.reader(csvfile, delimiter=',')
    for row in plots:
        x.append(row[0])
        y.append(float(row[1]))

x_ticks = range(1, len(x) + 1)
plt.___(x_ticks, y, label=___)
plt.xticks(x_ticks, x)
plt.xlabel(___)
plt.ylabel(___)
plt.ylim(___)
# 添加圖表標題 title()
plt.___('Market Average Price')
plt.legend()
# 使用 savefig() 函數
plt.___('chart.png')
plt.close()

# --開始--批改評分使用，請勿變動
import matplotlib as mpl
mpl.use('Agg')
# --結束--批改評分使用，請勿變動

# 載入 matplotlib.pyplot 並縮寫為 plt
import matplotlib.pyplot as plt
# 載入 csv 模組
import csv

x = []
y = []

# 讀入 read.csv
with open('read.csv', 'r', encoding='utf8') as csvfile:
    plots = csv.reader(csvfile, delimiter=',')
    for row in plots:
        x.append(row[0])
        y.append(float(row[1]))

x_ticks = range(1, len(x) + 1)
plt.plot(x_ticks, y, label='banana')
plt.xticks(x_ticks, x)
plt.xlabel('date')
plt.ylabel('NT$')
plt.ylim([15, 25])
# 添加圖表標題 title()
plt.title('Market Average Price')
plt.legend()
# 使用 savefig() 函數
plt.savefig('chart.png')
plt.close()

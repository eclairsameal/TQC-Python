# -*- coding: utf-8 -*-
# 載入 pandas 模組縮寫為 pd
import pandas as pd

# 資料輸入
datas = [[75, 62, 85, 73, 60], [91, 53, 56, 63, 65],
         [71, 88, 51, 69, 87], [69, 53, 87, 74, 70]]
indexs = ["小林", "小黃", "小陳", "小美"]
columns = ["國語", "數學", "英文", "自然", "社會"]
df = pd.DataFrame(datas, columns=columns,  index=indexs)

print('行標題為科目，列題標為個人的所有學生成績')
print(df)
print()

# 輸出後二位學生的所有成績
print('後二位的成績')
print(df.tail(2))
print()

# 將自然成績做遞減排序輸出
df1 = df.sort_values(by="自然", ascending=False)
print('以自然遞減排序')
print(df1.loc[:,"自然"])
print()

# 僅列小黃的成績，並將其英文成績改為80
df.loc["小黃", "英文"] = 80
print('小黃的成績')
print(df.loc["小黃"])

# 載入 pandas 模組縮寫為 pd
import pandas as pd

# 讀取csv檔
df1 = pd.read_csv("read.csv", encoding="utf-8", sep=",", header=0)

# 居住縣市病例人數，並按遞減順序顯示
df_county = df1.groupby("居住縣市")["居住縣市"].count()
print(df_county.sort_values(ascending=False))
# 顯示感染病例人數最多的5個國家，並按遞減順序顯示
df_country = df1.groupby("感染國家")["感染國家"].count()
print(df_country.sort_values(ascending=False).head(5))
# 台北市各區病例人數
df_taipei = df1[df1.居住縣市 == "台北市"]
print(df_taipei.groupby("居住鄉鎮")["居住鄉鎮"].count())
# 台北市最近病例的日期
print("發病日: " + df_taipei['發病日'].max())

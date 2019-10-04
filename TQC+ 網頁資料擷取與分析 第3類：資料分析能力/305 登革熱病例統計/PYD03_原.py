# 載入 pandas 模組縮寫為 pd
import ___ as ___

# 讀取csv檔
df1 = pd.read_csv(___, encoding="utf-8", sep=",", header=0)

# 居住縣市病例人數，並按遞減順序顯示
df_county = df1.groupby("居住縣市")["___"].___
print(df_county.sort_values(___=___))
# 顯示感染病例人數最多的5個國家，並按遞減順序顯示
df_country = df1.groupby("感染國家")["___"].___
print(df_country.sort_values(___=___).___)
# 台北市各區病例人數
df_taipei = df1[df1.居住縣市 == "___"]
print(df_taipei.groupby("居住鄉鎮")["___"].___)
# 台北市最近病例的日期
print("發病日: " + df_taipei.___.___())

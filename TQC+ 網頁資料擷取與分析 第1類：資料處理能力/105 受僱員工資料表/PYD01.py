# 載入 sqlite3 模組
import sqlite3

# 建立資料庫連結
con = sqlite3.connect('read.db')
# 建立cursor物件
c = con.cursor()

# 查詢Employee資料表
cursor = c.execute("SELECT * FROM Employee")

# 印出查詢結果
for row in cursor:
    print(row)

# 關閉與資料庫的連結
con.close()

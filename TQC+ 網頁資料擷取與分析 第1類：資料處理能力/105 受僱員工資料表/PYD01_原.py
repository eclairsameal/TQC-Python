# 載入 sqlite3 模組
import ___

# 建立資料庫連結
con = ___.___('___')
# 建立cursor物件
___ = con.___

# 查詢Employee資料表
___.___("SELECT * FROM Employee")

# 印出查詢結果
for ___ in ___:
    print(___)

# 關閉與資料庫的連結
con.close()

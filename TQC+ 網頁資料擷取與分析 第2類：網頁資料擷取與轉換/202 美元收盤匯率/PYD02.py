# 載入 csv 模組
import csv
# 自 urllib.request 模組載入 urlopen 函數
from urllib.request import urlopen
# 自 bs4 模組載入 BeautifulSoup 函數
from bs4 import BeautifulSoup


# 將資料寫入csv檔案，編碼為 utf8
file_name = "write.csv"
f = open(file_name, "w", encoding='utf8')
# 以 csv 模組的 writer 函數初始化寫檔
w = csv.writer(f)

# 爬取的目標網頁
htmlname = "file:read.html"
# urlopen 函數讀取 html 檔案
html = urlopen(htmlname)
# 指定 BeautifulSoup 的解析器為 lxml
bsObj = BeautifulSoup(html, "lxml")

count = 0
# 將其中日期、NTD/USD 兩個欄位的名稱與資料轉存為csv
# 資料位置
for single_tr in bsObj.find("table", {"class": "DataTable2"}).findAll("tr"):
    if count == 0:
        # 擷取資料位置
        cell = single_tr.findAll("th")
    else:
        # 擷取資料位置
        cell = single_tr.findAll("td")
    F0 = cell[0].text
    F1 = cell[1].text
    data = [[F0, F1]]
    w.writerows(data)
    count = count + 1
f.close()

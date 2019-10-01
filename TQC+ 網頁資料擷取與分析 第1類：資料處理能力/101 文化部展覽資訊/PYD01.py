# 載入 json 與 csv 模組
import csv
import json

# 讀取 json 檔案並指定編碼為 utf8 
# with : https://blog.gtwang.org/programming/python-with-context-manager-tutorial/
with open("read.json", encoding='utf8') as file:
    data = json.load(file)

# 寫入 csv 檔案並指定編碼為 utf8
with open("write.csv", "w", encoding='utf8') as file:
    csv_file = csv.writer(file)
    # 寫入 title（活動名稱）、showUnit（演出單位）、startDate（活動起始日期）、endDate（活動結束日期）等四個欄位
    for item in data:
        csv_file.writerow([item['title'], item['showUnit'],
                           item['startDate'], item['endDate']])

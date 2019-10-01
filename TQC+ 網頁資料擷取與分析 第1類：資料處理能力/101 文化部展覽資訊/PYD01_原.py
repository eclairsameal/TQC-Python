# 載入 json 與 csv 模組
import ___
import ___

# 讀取 json 檔案並指定編碼為 utf8
with ___("___", encoding='___') as file:
    data = json.load(file)

# 寫入 csv 檔案並指定編碼為 utf8
with ___("___", "___", encoding='___') as file:
    csv_file = csv.writer(file)
    # 寫入 title（活動名稱）、showUnit（演出單位）、startDate（活動起始日期）、endDate（活動結束日期）等四個欄位
    for item in data:
        csv_file.writerow([___['___'], ___['___'],
                           ___['___'], ___['___']])

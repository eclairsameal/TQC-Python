# 載入 xml.etree.ElementTree 模組並縮寫為 ET
import ___ as ___
# 載入 csv 模組
import ___

# 讀取 xml
tree = ___.___("___")
root = tree.getroot()

# 寫入 csv 檔案，編碼設定為 utf8
ubikefile = ___("___", "___", encoding='___')
csvwriter = csv.writer(ubikefile)

# 將其中 sno（站點代號）、sna（中文場站名稱）、tot（場站總停車格）等三個欄位寫出
for row in root:
    ubike = []
    sno = row.find('___').text
    ubike.append(___)
    sna = row.find('___').text
    ubike.append(___)
    tot = row.find('___').text
    ubike.append(___)
    csvwriter.writerow(ubike)
ubikefile.close()

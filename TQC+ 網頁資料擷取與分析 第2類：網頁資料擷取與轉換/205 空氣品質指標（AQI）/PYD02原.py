# 載入 requests 與 json 模組
import ___
import ___

# 開放資料Json格式連結
url = ___
# 發出Get請求
response = ___
# 回傳內容長度
print(___, ___)
# 將取得的回傳內容轉換成Json格式
response = ___

print()

# 顯示新北市每一個地區的PM2.5相關資料
print('新北市PM2.5相關資料：')
for record in response:
    if record['County'] == '___':
        print('%s：' % record['___'])
        print('AQI：%s' % record['___'])
        print('PM2.5：%s' % record['___'])
        print('PM10：%s' % record['___'])
        print('資料更新時間：%s' % record['___'])

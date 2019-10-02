# 載入 requests 模組
import requests
# 載入 json 模組
import json

# 開放資料連結
url = 'http://tqc.codejudger.com:3000/target/5204.json'
# 以 requests 模組發出 HTTP GET 請求
res = requests.get(url)

# 將回傳結果轉換成標準JSON格式
data = json.loads(res.text)

# 輸出新北市大專院校名單
print('新北市大專院校名單：\n')
for record in data:
    if record['type'] == '大專院校':
        print('名稱：%s' % record['name'])
        print('地址：%s' % record['address'])
        print('聯絡電話：%s' % record['tel'])
        print('網站：%s' % record['website'])
        print('資料更新時間：%s' % record['update_date'])
        print()

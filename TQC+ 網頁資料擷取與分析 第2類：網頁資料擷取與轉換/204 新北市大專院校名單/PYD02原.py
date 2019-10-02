# 載入 requests 模組
import ___
# 載入 json 模組
import ___

# 開放資料連結
url = '____'
# 以 requests 模組發出 HTTP GET 請求
res = ___.___(url)

# 將回傳結果轉換成標準JSON格式
data = json.loads(res.text)

# 輸出新北市大專院校名單
print('新北市大專院校名單：\n')
for record in data:
    if record['type'] == '大專院校':
        print('名稱：%s' % record['___'])
        print('地址：%s' % record['___'])
        print('聯絡電話：%s' % record['___'])
        print('網站：%s' % record['___'])
        print('資料更新時間：%s' % record['___'])
        print()

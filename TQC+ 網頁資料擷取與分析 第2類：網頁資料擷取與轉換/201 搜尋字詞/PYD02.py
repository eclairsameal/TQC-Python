# 載入模組
import re
import requests

url = 'http://tqc.codejudger.com:3000/target/5201.html'

# 使用 GET 請求
htmlfile = requests.get(url)
# 驗證HTTP Status Code
if htmlfile.status_code == 200:
    # 欲搜尋的字串
    sstr = input("請輸入欲搜尋的字串 : ")
    rstr = re.findall(sstr, htmlfile.text)
    if sstr in htmlfile.text:
        print(sstr, "搜尋成功")
        print(sstr, "出現 %d 次" % len(rstr))
    else:
        print(sstr, "搜尋失敗")
        print(sstr, "出現 0 次")
else:
    print("網頁下載失敗")

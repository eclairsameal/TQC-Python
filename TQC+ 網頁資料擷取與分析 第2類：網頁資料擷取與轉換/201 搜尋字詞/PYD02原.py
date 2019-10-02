# 載入模組
import ___
import ___

url = '___'

# 使用 GET 請求
htmlfile = requests.___(___)
# 驗證HTTP Status Code
if htmlfile.status_code == ___:
    # 欲搜尋的字串
    ___ = input("請輸入欲搜尋的字串 : ")
    ___ = re.findall(___, htmlfile.text)
    if ___ in htmlfile.text:
        print(___, "搜尋成功")
        print(___, "出現 %d 次" % len(___))
    else:
        print(___, "搜尋失敗")
        print(___, "出現 0 次")
else:
    print("網頁下載失敗")

# -*- coding: utf-8 -*-

import bs4
import requests

url = 'http://tqc.codejudger.com:3000/target/5203.html'
# GET 請求
html = requests.get(url)

# 使用 lxml 解析器
objSoup = bs4.BeautifulSoup(html.text, 'html')

dataTag = objSoup.select('.contents_box02')

balls = dataTag[2].find_all('div', {'class': 'ball_tx ball_yellow'})
print("大樂透開獎 : ")
print('-------------')

# 開出順序
print("開出順序 : ", end='')
for i in range(6):
    print(balls[i].text, end='   ') 

# 大小順序
print("\n大小順序 : ", end='')
for i in range(6, len(balls)):
    print(balls[i].text, end='   ')

# 特別號：資料位於 <div class="ball_red"></div>
redball = dataTag[2].find('div', {'class': 'ball_red'})

print("\n特別號   :", redball.text)

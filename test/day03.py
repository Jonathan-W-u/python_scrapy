# -*- enconding:utf-8 -*-

import requests

url = 'https://hotel.meituan.com/wuxi/'

dic = {
    "User-Agent": "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/96.0.4664.45 Safari/537.36"
}

res = requests.get(url, headers = dic)

# print(res)
# print(res.text)
# print(res.text)

with open("meituan.html", mode = "w", encoding = 'utf-8') as f:
    f.write(res.text)


# with open("index.html", mode = "w", encoding = 'utf-8') as f:
#     # f.seek(0, 0)
#     f.write(res.read().decode('utf-8')) 
#     # print("测试")
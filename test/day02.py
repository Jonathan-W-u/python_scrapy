# -*- encoding:utf-8 -*-

import requests

query = input("请输入需要查询的内容")

url = 'https://www.sogou.com/web?query={query}'

dic = {
    'user-agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/96.0.4664.45 Safari/537.36'
}

res = requests.get(url, headers = dic)

print(res)
print(res.text)
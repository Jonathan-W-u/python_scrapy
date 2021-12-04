# -*- conding:utf-8 -*-

from urllib.request import urlopen

url ="http://www.baidu.com"
res = urlopen(url)

# print(res.read().decode("utf-8"))

with open("index.html", mode = "w", encoding = 'utf-8') as f:
    # f.seek(0, 0)
    f.write(res.read().decode('utf-8')) 
    # print("测试")


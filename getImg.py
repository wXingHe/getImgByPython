import requests
import re
import os
# r = requests.get("http://www.9ku.com")
# print(r.text)

from bs4 import BeautifulSoup,Comment

#图片路径
url = "http://www.9ku.com/play/528667.htm"
#请求头信息
headers = {'User-Agent':'Mozilla/5.0 (Windows NT 6.1; WOW64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/49.0.2623.221 Safari/537.36 SE 2.X MetaSr 1.0'}
#发送请求，返回网页
html = requests.get(url,headers)
print(html.text)
imgs = BeautifulSoup(html.text,'lxml').find_all("a",class_="songName")
i = 0
for img in imgs:
    matObj = re.match("/play/(.*)htm",img['href'])
    if matObj != None:
        print(str(i)+":http://www.9ku.com"+matObj.group())
        imgurl = matObj.group()
        file = requests.get(imgurl,headers)
        file_name = str(i)+'.jpg'
        f = open("./img/"+file_name,"ab")
        f.write(file.content)
        f.close()
        i = i+1




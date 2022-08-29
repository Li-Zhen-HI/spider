import requests
import re  #正则
import os  #创建文件夹
if not os.path.exists('./糗图爬取图片'):
    os.mkdir('./糗图爬取图片')
headers={'User-Agent':'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/100.0.4896.60 Safari/537.36'}
url='https://book.douban.com/top250?start=25'
for aaa in range(0,226,25):
    newurl = 'https://book.douban.com/top250?start=%d' % aaa

    jieguo=requests.get(url=newurl,headers=headers).text
    ttt='https:.*?jpg'
    im=re.findall(ttt,jieguo)
    for i in im:
        imglist=requests.get(url=i,headers=headers).content
        name=i.split('/')[-1]
        pathi='./糗图爬取图片/'+name
        with open(pathi,'wb') as fp:
            fp.write(imglist)
        print(name,'ok')



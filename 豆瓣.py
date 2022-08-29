import requests
import json

date={'type': '25',
'interval_id': '100:90',
'action':'',
'start': '0',
'limit':'20'}
url='https://movie.douban.com/j/chart/top_list'
headers={'User-Agent':'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/100.0.4896.60 Safari/537.36'}

hhh=requests.get(url=url,params=date,headers=headers)

jieguo=hhh.json()
filename='douban'+'.json'
fp=open(filename, 'w' , encoding='utf-8')


json.dump(jieguo,fp=fp,ensure_ascii=False)
print('over')
import requests
import json
world=input('请输入需要翻译的词语：')
date={'kw':world}
url='https://fanyi.baidu.com/sug'
headers={'User-Agent':'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/100.0.4896.60 Safari/537.36'}

hhh=requests.post(url=url,params=date,headers=headers)

jieguo=hhh.json()
filename=world+'.json'
fp=open(filename, 'w' , encoding='utf-8')


json.dump(jieguo,fp=fp,ensure_ascii=False)
print('over')
import requests
import json
url='http://www.kfc.com.cn/kfccda/ashx/GetStoreList.ashx?op=keyword'
keyword=input('请输入一个地方：')
key={'cname': '',
'pid': '',
'keyword': keyword,
'pageIndex':'1',
'pageSize': '10'}
headers={'User-Agent':'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/100.0.4896.60 Safari/537.36'}

result=requests.post(url=url,params=key,headers=headers)
ww=result.json()
filename=keyword+'.json'
fp=open(filename,'w',encoding='utf-8')
json.dump(ww,fp=fp,ensure_ascii=False,indent=True)
print('完成！！！！')
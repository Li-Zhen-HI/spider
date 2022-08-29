
import requests
url = 'https://www.baidu.com/s'

shuru=input('输入关键词：')
canshu={'wd':shuru}
headers={'User-Agent':'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/100.0.4896.60 Safari/537.36'}
mm=requests.get(url = url , params = canshu,headers=headers )
jieguo=mm.text
filename=shuru+'.html'
with open(filename, 'w' , encoding='utf-8') as fp:
    fp.write(jieguo)
    print(filename,'保存成功')

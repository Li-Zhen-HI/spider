from lxml import etree
import requests
import chardet

headers = {
    'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/100.0.4896.60 Safari/537.36'}

url = 'https://b5p22.com/pic/katong/'
page = requests.get(url=url, headers=headers)
page.encoding=chardet.detect(page.content)['encoding']

tree = etree.HTML(page.text)
lilist = tree.xpath('/html/body/div[6]/div/div[2]/dl')

for i in lilist:

    newurl =i.xpath('./dt/a/img/@data-original')[0]
    title=i.xpath('./dt/a/img/@alt')[0]
    imgdeta = requests.get(url=newurl, headers=headers).content
    iii=title+'.jpg'

    with open(iii, 'wb') as fp:
        fp.write(imgdeta)
    print(title, "成功！！！！")
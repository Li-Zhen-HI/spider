from lxml import etree
import requests
headers = {
    'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/100.0.4896.60 Safari/537.36'}
a=int(input('共134叶，您要前几页的内容：'))
if a == 1:

    url='https://pic.netbian.com/4kdongman/'
else:
    for l in range(1,a+1):
        url='https://pic.netbian.com/4kdongman/index_%d.html'%l
        page =requests.get(url=url,headers=headers).text

        tree =etree.HTML(page)
        lilist=tree.xpath('/html/body/div[2]/div/div[3]/ul/li')

        for i in lilist:
            newurl='https://pic.netbian.com'+i.xpath('./a/img/@src')[0]


            title=i.xpath('./a/img/@alt')[0]
            title=title.encode('iso-8859-1').decode('gbk')    #大部分解决中文乱码
            imgdeta=requests.get(url=newurl,headers=headers).content
            imgpath=title+'.jpg'
            with open(imgpath,'wb') as fp:
                fp.write(imgdeta)
            print(title,"成功！！！！")
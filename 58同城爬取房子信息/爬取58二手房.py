from lxml import etree
import requests
import os
if not os.path.exists('./58同城爬取房子信息'):
    os.mkdir('./58同城爬取房子信息')
headers = {
    'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/100.0.4896.60 Safari/537.36'}
url = 'https://jiaozuo.58.com/ershoufang/?utm_source=sem-360-pc'
page =requests.get(url=url,headers=headers).text
tree =etree.HTML(page)
divlist =tree.xpath('//section[@class="list"]/div')
fp = open('./58同城.text', 'w', encoding='utf-8')
for i in divlist:

    title =i.xpath('./a/div[2]/div[1]/div[1]/h3/text()')[0]
    price1 = i.xpath('./a/div[2]/div[2]/p[1]/span/text()')

             #*price1可输出列表多元素中的字符串
    price2=i.xpath('./a/div[2]/div[2]/p[2]/text()')[0]
    fp.write("{}------{}{}-------{}\n".format(title,*price1,price2))


    print(title,'成功！！！！')
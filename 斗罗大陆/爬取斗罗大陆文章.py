import requests
import bs4

import os  # 创建文件夹


headers = {
    'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/100.0.4896.60 Safari/537.36'}
url = 'https://www.qu-la.com/booktxt/99253093116/'

jieguo = requests.get(url=url, headers=headers).text
soup = bs4.BeautifulSoup(jieguo, 'lxml')
alist = soup.select('.cf li')
fp = open('./斗罗大陆.text', 'w', encoding='utf-8')
for i in alist[9:]:
    title = i.a.string
    urlnewnew = 'https://www.qu-la.com' + i.a['href']
    neirong = requests.get(url=urlnewnew, headers=headers).text
    soup2 = bs4.BeautifulSoup(neirong, 'lxml')
    wenzhang = soup2.find('div', class_='txt')
    www = wenzhang.text

    fp.write(title+'\n'+www+'\n')

    print(title,'爬取成功')

# 『如果章节错误，点此举报』　　　　柔和

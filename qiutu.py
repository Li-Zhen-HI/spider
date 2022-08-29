import requests
headers={'User-Agent':'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/100.0.4896.60 Safari/537.36'}
url='https://gimg2.baidu.com/image_search/src=http%3A%2F%2F5b0988e595225.cdn.sohucs.com%2Fq_70%2Cc_zoom%2Cw_640%2Fimages%2F20200127%2Fad0f5f5f5bd44407bb88aba1f2643f40.jpeg&refer=http%3A%2F%2F5b0988e595225.cdn.sohucs.com&app=2002&size=f9999,10000&q=a80&n=0&g=0n&fmt=auto?sec=1653124376&t=164071c267622028c43e9d9fe798d80f'
jieguo=requests.get(url=url,headers=headers).content
with open('./糗图.jpg','wb') as fp:
    fp.write(jieguo)
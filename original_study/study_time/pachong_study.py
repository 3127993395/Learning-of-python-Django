import requests
import re

url = 'https://pvp.qq.com/web201605/herodetail/157.shtml'

headers = {
    'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/108.0.0.0 Safari/537.36 Edg/108.0.1462.54'
}

yuanma = requests.get(url=url, headers=headers)
yuanma.encoding = 'gbk'
# print(yuanma.text)

pifulist = re.findall('class="pic-pf-list pic-pf-list3" data-imgname="(.*)">', yuanma.text)[0]
pifunum = len(pifulist.split('|'))

for i in range(1, pifunum+1):
    pifu_url = f'https://game.gtimg.cn/images/yxzj/img201606/skin/hero-info/157/157-bigskin-{i}.jpg'
    print(pifu_url)
    image = open(str(i) + '.jpg', 'wb')
    image.write(requests.get(pifu_url, headers=headers).content)
    image.close()

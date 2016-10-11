from bs4 import BeautifulSoup
import requests
import time
import pymongo

url1 = 'http://www.0831home.com/archive.php?aid=40535'
urls = ['http://www.0831home.com/index.php?caid=3&addno=1&ccid1=1&page={}'.format(str(i)) for i in range(1, 15)]
headers = {
    'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; WOW64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/55.0.2868.3 Safari/537.36'
}
# 连接数据库
client=pymongo.MongoClient('localhost',27017)
# 创建一个库
sanj=client['sanj']
# 创建一个表
fwxx=sanj['fwxx']

def get_urls(url, headers):
    wb_data = requests.get(url, headers=headers)
    soup = BeautifulSoup(wb_data.text, 'lxml')
    for url in soup.select('p.title > a'):
        print(url.get('href'))
        get_details(url.get('href'), headers)


def get_details(url, headers):
    time.sleep(2)
    wb_data = requests.get(url, headers=headers)
    soup = BeautifulSoup(wb_data.text, 'lxml')
    # 标题
    titles = soup.select('div.mt20 > h1')[0].text.strip()
    # 发布时间
    times = soup.select('div.fyother.colorg.clearfix > span:nth-of-type(2)')[0].text.split('：')[-1].split(' ')[
        0].strip()

    if soup.select('span.fy-pri')[0].text =='面议':
        shoujias =soup.select('span.fy-pri')[0].text
        fwDanJias='面议'
    else:
        # 售价
        shoujias = soup.select('span.fy-pri > b')[0].text.strip()
        print(shoujias)
        # 单价
        fwDanJias = soup.select('span.fy-pri > span')[0].text.replace('(', '').split('元')[0].strip()
    fangwu = soup.select('div.house_info.l.w450 > div:nth-of-type(2)')[0].text.split('：')[-1].split('(')
    # 户型
    huxing = fangwu[0]
    # 面积
    fwMianjis = fangwu[-1].strip().replace(')', '').replace('㎡', '')
    # 电话
    tel = soup.select('div.house_info.l.w450  > ul > li.tel > p > b')[0].text.strip()
    # 装修类型
    zhuangxiu = soup.select('div.house_info.l.w450  > ul > li:nth-of-type(2)')[0].text.split('：')[-1].strip()
    # 楼层
    louceng = soup.select('div.house_info.l.w450  > ul > li:nth-of-type(3)')[0].text.split('：')[-1].split(" ")
    # 位置
    weizhi = soup.select('div.house_info.l.w450  > ul > li:nth-of-type(4)')[0].text.split('：')[-1].split(" ")
    # 地址
    dizhi = soup.select('div.house_info.l.w450  > ul > li:nth-of-type(5)')[0].text.split('：')[-1].split("(")[0]
    # 修建年代
    xiujianniandai = soup.select('div.house_info.l.w450  > ul > li:nth-of-type(6)')[0].text.split('：')[-1].replace(' ',
                                                                                                                   '')
    # 配套
    peitao = []
    temp = soup.select('div.house_info.l.w450  > ul > li:nth-of-type(7)')[0].text.split('：')[-1].split(' ')
    for i in temp:
        if len(i) != 0:
            peitao.append(i)

    data = {
        'title': titles,
        'time': times,
        'shoujia': shoujias,
        'danjia': fwDanJias,
        'huxing': huxing,
        'mianji': fwMianjis,
        'tel': tel,
        'zhuangxiu': zhuangxiu,
        'louceng': louceng,
        'weizhi': weizhi,
        'dizhi': dizhi,
        'xiujianniandai': xiujianniandai,
        'peitao': peitao
    }
    # fwxx.insert_one(data)
    print(data)
get_details(url1,headers)

# for url in urls:
#     get_urls(url, headers)

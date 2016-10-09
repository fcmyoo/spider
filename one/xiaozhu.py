from bs4 import BeautifulSoup
import requests
import time

fw_data = []

urls = ['http://bj.xiaozhu.com/search-duanzufang-p{}-0/'.format(str(i)) for i in range(1, 31)]


def get_urls(url):
    web_data = requests.get(url)
    soup = BeautifulSoup(web_data.text, 'lxml')
    site_urls = soup.select('#page_list > ul > li > a')
    for site_url in site_urls:
        site_url = site_url.get('href')
        get_details(site_url)


def get_details(url):
    time.sleep(2)
    web_data = requests.get(url)
    soup = BeautifulSoup(web_data.text, 'lxml')
    titles = soup.select('body > div.wrap.clearfix.con_bg > div.con_l > div.pho_info > h4 > em')
    address = soup.select('body > div.wrap.clearfix.con_bg > div.con_l > div.pho_info > p')
    moneys = soup.select('#pricePart > div.day_l > span')
    pics = soup.select('#curBigImage')
    fdPics = soup.select('#floatRightBox > div.js_box.clearfix > div.member_pic > a > img')
    sexs = soup.select('#floatRightBox > div.js_box.clearfix > div.member_pic > div')
    names = soup.select('#floatRightBox > div.js_box.clearfix > div.w_240 > h6 > a')
    for title, addres, money, pic, fdPic, sex, name in zip(titles, address, moneys, pics, fdPics, sexs, names):
        sex1 = ''.join(sex.get('class'))
        # print(sex1)
        if sex1 == 'member_ico1':
            sex = '女'
        elif sex1 == 'member_ico':
            sex = '男'
        else:
            sex = '男'
        data = {
            'title': title.get_text(),
            'addres': addres.get('title'),
            'money': money.get_text(),
            'pic': pic.get('src'),
            'fdPic': fdPic.get('src'),
            'sex': sex,
            'name': name.get_text(),
        }
        fw_data.append(data)
        print(data)


for i in urls:
    print(i)
    get_urls(i)

print(len(fw_data))

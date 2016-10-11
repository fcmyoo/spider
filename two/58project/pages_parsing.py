from bs4 import BeautifulSoup
import time
import requests
import pymongo

# urls = 'http://bj.58.com/shouji/pn3/'
client = pymongo.MongoClient('127.0.0.1', 27017)
ceshi = client['ceshi']
url_list = ceshi['url_list']
item_list = ceshi['item_list']


def get_detail_urls(url, page, who_sells=1):
    url = '{}{}/pn{}'.format(url, str(who_sells), str(page))
    web_data = requests.get(url)
    soup = BeautifulSoup(web_data.text, 'lxml')
    # print(soup.select('td.t'))
    if soup.find_all('td', 't'):
        for link in soup.select('td.t a.t'):
            url_list.insert_one(link.get('href').split('?')[0])
            print(link.get('href').split('?')[0])
    else:
        pass


def get_all_detail(url):
    web_data = requests.get(url)
    soup = BeautifulSoup(web_data.text, 'lxml')
    no_loger_exist = '404' in soup.find('script', type="text/javascript").get('src').split('/')
    if no_loger_exist:
        pass
    else:
        time.sleep(2)
        title = soup.select('div.mainTitle > h1')[0].text if soup.find_all('div', 'mainTitle') else None
        price = soup.select('.price.c_f50')[0].text if soup.find_all('span', 'price c_f50') else None
        times = soup.select('.time')[0].text if soup.find_all('li', 'time') else None
        area = []
        temp = soup.select('.c_25d a') if soup.find_all('span', 'c_25d') else None
        for a in temp[1:]:
            area.append(a.text)
        item_list.insert_one({
            'title': title,
            'price': float(price),
            'time': time,
            'area': area
        })
        print({
            'title': title,
            'price': float(price),
            'time': times,
            'area': area
        })


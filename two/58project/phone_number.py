from bs4 import BeautifulSoup
import time
import requests
import pymongo

urls = 'http://bj.58.com/shoujihao/'
client = pymongo.MongoClient('127.0.0.1', 27017)
phone_58 = client['phone58']
phone_url_list = phone_58['url_list']
phone_item_list = phone_58['item_list']
headre = {
    'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; WOW64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/55.0.2868.3 Safari/537.36'
}


def get_links_urls(url, page):
    url = '{}pn{}/'.format(url, str(page))
    print(url)
    web_data = requests.get(url, headers=headre)
    soup = BeautifulSoup(web_data.text, 'lxml')
    for temp in soup.select('.t'):
        link = temp.get('href').split('?')[0]
        # print(link)
        if 'jump' in link.split('/'):
            pass
        else:

            if phone_58.collection_names() != None:
                for s in phone_url_list.find({'link': link}):
                    if s['link'] == link:
                        print(s['link'] == link)
                        pass
                    else:
                        number = temp.find_all('strong')[0].text
                        data = {
                            'link': link,
                            'number': number
                        }
                        phone_url_list.insert_one(data)
                        print(data)
            else:
                number = temp.find_all('strong')[0].text
                data = {
                    'link': link,
                    'number': number
                }
                phone_url_list.insert_one(data)
                print(data)


def get_all_detail(url):
    web_data = requests.get(url, headres=headre)
    soup = BeautifulSoup(web_data.text, 'lxml')
    time.sleep(2)
    number = soup.select('div.col_sub.mainTitle > h1')[0].text.strip().split(' ')[0].split('\n')[0]
    yys = soup.select('div.col_sub.mainTitle > h1')[0].text.strip().split(' ')[-1].split('\t')[-1]
    price = soup.select('.price.c_f50')[0].text.strip().split(' ')[0]
    area = [i.text for i in soup.select('div.su_con > a')]
    date = soup.select('.time')[0].text
    name = soup.select('.tx')[0].text
    data = {
        'number': number,
        'yys': yys,
        'price': price,
        'area': area,
        'date': date,
        'name': name
    }
    phone_item_list.insert_one(data)
    print(data)


# get_all_detail('http://bj.58.com/shoujihao/27591517413685x.shtml')
# get_links_urls(urls, 71)
time3 = time.time()

for i in range(1, 4):
    time1 = time.time()
    get_links_urls(urls, i)
    time.sleep(2)
    time2 = time.time()
    print('这是爬取的第{}页,用时{}.'.format(i, time2 - time1))
time4 = time.time()
print('总用时:{}.'.format(time4 - time3))

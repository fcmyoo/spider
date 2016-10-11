from bs4 import BeautifulSoup
import requests

url = 'http://bj.58.com/sale.shtml'
web_url = 'http://bj.58.com/'


def get_index_link(url):
    web_data = requests.get(url)
    soup = BeautifulSoup(web_data.text, 'lxml')
    links = soup.select('ul.ym-submnu > li > b > a')
    for link in links:
        all_links = '{}{}'.format(web_url, link.get('href'))
        print(all_links)

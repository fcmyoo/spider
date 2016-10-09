from bs4 import BeautifulSoup
info=[]
with open(u'E:/pyweb/exceltest/传智播客/爬虫/web/new_index.html', 'r') as web_data:
    soup = BeautifulSoup(web_data, 'lxml')
    images = soup.select('body > div.main-content > ul > li > img')
    titles = soup.select('body > div.main-content > ul > li > div.article-info > h3 > a')
    descs = soup.select('body > div.main-content > ul > li > div.article-info > p.description')
    cates = soup.select('body > div.main-content > ul > li > div.article-info > p.meta-info')
    rates = soup.select('body > div.main-content > ul > li > div.rate > span')

for title, image, desc, cate, rate in zip(titles, images, descs, cates, rates):
    data = {
        'title': title.get_text(),
        'desc': desc.get_text(),
        'cate': list(cate.stripped_strings),
        'rate': rate.get_text(),
        'image': image.get('src')
    }
    info.append(data)

for i in info:

    if float(i['rate'])>3:
        print(i['title'],i['cate'])
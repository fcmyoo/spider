from bs4 import BeautifulSoup

info = []

with open(u'E:/pyweb/exceltest/传智播客/爬虫/homework/index.html', 'r') as web_data:
    soup = BeautifulSoup(web_data, 'lxml')
    images = soup.select('body > div > div > div.col-md-9 > div > div > div > img')
    titles = soup.select('body > div > div > div.col-md-9 > div > div > div > div.caption > h4 > a')
    prices = soup.select('body > div > div > div.col-md-9 > div > div > div > div.caption > h4.pull-right')
    contents = soup.select('body > div > div > div.col-md-9 > div > div > div > div.caption > p')
    reviews = soup.select('body > div > div > div.col-md-9 > div > div > div > div.ratings > p.pull-right')
    stars = soup.select('body > div > div > div.col-md-9 > div > div > div > div.ratings > p:nth-of-type(2)')
    # star=soup.find_all('span', class_='glyphicon-star')
for title, price, content, review, star, image in zip(titles, prices, contents, reviews, stars, images):

    data = {
        'title': title.get_text(),
        'price': price.get_text()[1:],
        'content': content.get_text(),
        'review': review.get_text()[0:2],
        'star': len(star.find_all('span', attrs={'class': 'glyphicon glyphicon-star'})),
        'image': image.get('src')
    }
    info.append(data)

for i in info:
    if float(i['price']) < 500 and int(i['star']) > 3:
        print(i['title'], i['price'],i['star'])

import pymongo

temp = [
    'http://bj.58.com/shoujihao/27671048379344x.shtml',
    'http://bj.58.com/shoujihao/27671048379344x.shtml',
    'http://bj.58.com/shoujihao/27671041970763x.shtml',
    'http://bj.58.com/shoujihao/27671041970763x.shtml',
    'http://bj.58.com/shoujihao/27671027262777x.shtml',
    'http://bj.58.com/shoujihao/27671027262777x.shtml',
    'http://bj.58.com/shoujihao/27671022061999x.shtml',
    'http://bj.58.com/shoujihao/27671022061999x.shtml',
    'http://bj.58.com/shoujihao/27671005175595x.shtml',
    'http://bj.58.com/shoujihao/27671005175595x.shtml',
    'http://bj.58.com/shoujihao/27670999120572x.shtml',
    'http://bj.58.com/shoujihao/27670999120572x.shtml',
    'http://bj.58.com/shoujihao/27670956917821x.shtml',
    'http://bj.58.com/shoujihao/27670956917821x.shtml',
    'http://bj.58.com/shoujihao/27670953118790x.shtml',
    'http://bj.58.com/shoujihao/27670953118790x.shtml',
    'http://bj.58.com/shoujihao/27670949027383x.shtml',
    'http://bj.58.com/shoujihao/27670949027383x.shtml',
    'http://bj.58.com/shoujihao/27670944939315x.shtml',
    'http://bj.58.com/shoujihao/27670944939315x.shtml',
    'http://bj.58.com/shoujihao/27670925682370x.shtml',
    'http://bj.58.com/shoujihao/27670925682370x.shtml',
    'http://bj.58.com/shoujihao/27670922487997x.shtml',
    'http://bj.58.com/shoujihao/27670922487997x.shtml',
    'http://bj.58.com/shoujihao/27670918424772x.shtml',
    'http://bj.58.com/shoujihao/27670918424772x.shtml',
    'http://bj.58.com/shoujihao/27670921278663x.shtml',
    'http://bj.58.com/shoujihao/27670921278663x.shtml',
    'http://bj.58.com/shoujihao/27670912730931x.shtml',
    'http://bj.58.com/shoujihao/27670912730931x.shtml',
    'http://bj.58.com/shoujihao/27670916564399x.shtml',
    'http://bj.58.com/shoujihao/27670916564399x.shtml',
    'http://bj.58.com/shoujihao/27670907664695x.shtml',
    'http://bj.58.com/shoujihao/27670907664695x.shtml',
    'http://bj.58.com/shoujihao/27670901924542x.shtml',
    'http://bj.58.com/shoujihao/27670901924542x.shtml',
    'http://bj.58.com/shoujihao/27670903565133x.shtml',
    'http://bj.58.com/shoujihao/27670903565133x.shtml',
    'http://bj.58.com/shoujihao/27670897764430x.shtml',
    'http://bj.58.com/shoujihao/27670897764430x.shtml',
    'http://bj.58.com/shoujihao/27670886591539x.shtml',
    'http://bj.58.com/shoujihao/27670886591539x.shtml',
    'http://bj.58.com/shoujihao/27670894083372x.shtml',
    'http://bj.58.com/shoujihao/27670894083372x.shtml',
    'http://bj.58.com/shoujihao/27670881341623x.shtml',
    'http://bj.58.com/shoujihao/27670881341623x.shtml',
    'http://bj.58.com/shoujihao/27670885649199x.shtml',
    'http://bj.58.com/shoujihao/27670885649199x.shtml',
    'http://bj.58.com/shoujihao/27670843437996x.shtml',
    'http://bj.58.com/shoujihao/27670843437996x.shtml',
    'http://bj.58.com/shoujihao/27670805677388x.shtml',
    'http://bj.58.com/shoujihao/27670805677388x.shtml',
    'http://bj.58.com/shoujihao/27670801235269x.shtml',
    'http://bj.58.com/shoujihao/27670801235269x.shtml',
    'http://bj.58.com/shoujihao/27670797418042x.shtml',
    'http://bj.58.com/shoujihao/27670797418042x.shtml',
    'http://bj.58.com/shoujihao/27670793903806x.shtml',
    'http://bj.58.com/shoujihao/27670793903806x.shtml',
    'http://bj.58.com/shoujihao/27670789653693x.shtml',
    'http://bj.58.com/shoujihao/27670789653693x.shtml'
]

client = pymongo.MongoClient('127.0.0.1', 27017)
phone58 = client['phone58']
url_list = phone58['url_list']
print(phone58.collection_names()[0]=='url_list1')
#
# for i in temp:
#     data = url_list.find({'link': i})
#     print(data)
#     for d in data:
#         print(d['link'])
#         print(d['link'] == i)

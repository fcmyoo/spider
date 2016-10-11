import pymongo

# 连接数据库
client=pymongo.MongoClient('localhost',27017)
# 创建一个库
sanj=client['sanj']
# 创建一个表
fwxx=sanj['fwxx']

for item in fwxx.find({'danjia':{'$gte':5000}}):
    print(item)

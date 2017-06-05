import json
import random
import time

import requests
from requests.exceptions import ProxyError

nums = 0

headers = {
    'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 \
    (KHTML, like Gecko) Chrome/54.0.2840.71 Safari/537.36',
    'Accept-Encoding': 'gzip, deflate, sdch',
    'Accept-Language': 'zh-CN,zh;q=0.8',
    'Host': '114.55.235.53',
    'Referer': 'http://scmdsn.kids21.cn/Mdsn2017/index/cid/12.html?from=timeline&isappinstalled=0'
}


def url_s():
    all_url = []
    for url_num in range(0, 10):
        ids = [random.randint(5000, 9999) for i in range(0, 20)]
        num_id = random.sample(ids, 1)
        jquery_id = '149663054{0}'.format(str(num_id[0]))
        _id = '149663054{0}'.format(str(int(num_id[0]) + 1))
        urls = 'http://114.55.235.53/index.php/home/vote.html?callback=jQuery191049242572441268617_{0}&id=98&from=2017_MDSN&_={1}'.format(
            jquery_id, _id)
        all_url.append(urls)
    return all_url


def get_proxy():
    r = requests.get('http://127.0.0.1:5000/?types=0&count=100&country=国内')
    ip_ports = json.loads(r.text)
    return ip_ports


def zan(proxy):
    proxies = {'http': proxy}
    for i in range(0, 10):
        num = random.randint(1000, 9000)
        jquery_id = '149663054{0}'.format(str(num))
        _id = '149663054{0}'.format(str(num + 1))
        urls = 'http://114.55.235.53/index.php/home/vote.html?callback=jQuery191049242572441268617_{0}&id=98&from=2017_MDSN&_={1}'.format(
            jquery_id, _id)
        try:
            requst = requests.get(urls, proxies=proxies, headers=headers)
            time.sleep(3)
            if requst.status_code == 200:
                print(requst.text)
                if 'success' not in requst.text:
                    ip = proxy.split(':')[0]
                    r = requests.get('http://127.0.0.1:5000/delete?ip={0}'.format(ip))
                    print('{0},换IP,{1}'.format(i, r.text))
                    break
                else:
                    global nums
                    nums += 1
                    print('已点赞{0},此ip执行次数{1}'.format(nums, i))
            else:
                break
        except ProxyError:
            ip = proxy.split(':')[0]
            r = requests.get('http://127.0.0.1:5000/delete?ip={0}'.format(ip))
            print('删除IP{0}'.format(ip))
            break


def get_main():
    proxy = get_proxy()
    for ip in proxy:
        ip_s = '{0}:{1}'.format(ip[0], ip[1])
        zan(ip_s)
        print('ip:{0}'.format(ip_s))
    return 'ok'



# #
if __name__ == '__main__':
    urls = url_s()
    for url in urls:
        get_main()
#         # pool = Pool()
#         # pool = Pool(processes=4)
#         # pool.map(get_main, urls)
#         # pool.close()
#         # pool.join()

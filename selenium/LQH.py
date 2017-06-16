import json
import random
import time

import requests
from selenium import webdriver
from selenium.webdriver.common.proxy import ProxyType

userAgent = [
    'Mozilla/5.0 (Macintosh; Intel Mac OS X 10.9; rv:25.0) Gecko/20100101 Firefox/50.0 ',
    'Mozilla/5.0 (Macintosh; U; Intel Mac OS X 10_6_8; en-us) AppleWebKit/534.50 (KHTML, like Gecko) Version/5.1 Safari/534.50',
    'Mozilla/5.0 (Windows; U; Windows NT 6.1; en-us) AppleWebKit/534.50 (KHTML, like Gecko) Version/5.1 Safari/534.50',
    'Mozilla/5.0 (Windows NT 10.0; WOW64; rv:38.0) Gecko/20100101 Firefox/38.0',
    'Opera/9.80 (Windows NT 6.1; U; en) Presto/2.8.131 Version/11.11',
    'Opera/9.80 (Macintosh; Intel Mac OS X 10.6.8; U; en) Presto/2.8.131 Version/11.11',
    'Opera/9.80 (Windows NT 6.1; U; en) Presto/2.8.131 Version/11.11',
    'Mozilla/5.0 (Macintosh; Intel Mac OS X 10_7_0) AppleWebKit/535.11 (KHTML, like Gecko) Chrome/17.0.963.56 Safari/535.11',
]


class DZLqh(object):
    def __init__(self):
        dcap = webdriver.DesiredCapabilities.PHANTOMJS
        # dcap["phantomjs.page.settings.loadImages"] = False
        agent = random.choice(userAgent)
        dcap["phantomjs.page.settings.userAgent"] = agent
        dcap["phantomjs.page.customHeaders.User-Agent"] = agent
        self.driver = webdriver.PhantomJS(desired_capabilities=dcap)

    def setProxy(self, proxyStr):
        # 利用DesiredCapabilities(代理设置)参数值，重新打开一个sessionId
        proxy = webdriver.Proxy()
        proxy.proxy_type = ProxyType.MANUAL
        proxy.http_proxy = proxyStr
        # 将代理设置添加到webdriver.DesiredCapabilities.PHANTOMJS中
        proxy.add_to_capabilities(webdriver.DesiredCapabilities.PHANTOMJS)
        self.driver.start_session(webdriver.DesiredCapabilities.PHANTOMJS)

    def dz(self, url, proxyStr=None):
        if proxyStr:
            self.setProxy(proxyStr)
        try:
            self.driver.get(url)
            proxies = {'http': proxyStr}
            for i in range(0, 10):
                self.driver.find_element_by_xpath("//li/h3/img[@data='98']").click()
                msg = self.driver.page_source
                url = msg.split('src="')[1].split('"></script>')[0].replace('amp;', '')
                time.sleep(2)
                msg = requests.get(url, proxies=proxies)
                if msg.status_code == 200:
                    if 'success' in msg.text:
                        span_clk = self.driver.find_element_by_id('count_98').text
                        print('当前票数:{0}'.format(span_clk))
                    else:
                        break
                else:
                    break
            self.driver.delete_all_cookies()
            self.driver.quit()
            time.sleep(5)
        except Exception as e:
            print()


# dz.dz('http://www.ip138.com/','61.160.233.8:80')
url = ['http://scmdsn.kids21.cn/Mdsn2017/index/cid/12.htm', 'http://scmdsn.kids21.cn/Mdsn2017/index/cid/12.htm',
       'http://scmdsn.kids21.cn/Mdsn2017/index/cid/12.htm', 'http://scmdsn.kids21.cn/Mdsn2017/index/cid/12.htm',
       'http://scmdsn.kids21.cn/Mdsn2017/index/cid/12.htm', 'http://scmdsn.kids21.cn/Mdsn2017/index/cid/12.htm',
       'http://scmdsn.kids21.cn/Mdsn2017/index/cid/12.htm', 'http://scmdsn.kids21.cn/Mdsn2017/index/cid/12.htm',
       'http://scmdsn.kids21.cn/Mdsn2017/index/cid/12.htm', 'http://scmdsn.kids21.cn/Mdsn2017/index/cid/12.htm',
       ]


# url = 'http://www.ip138.com'

def get_proxy():
    r = requests.get('http://127.0.0.1:5000/?types=0&count=100&country=国内')
    ip_ports = json.loads(r.text)
    return ip_ports


def get_main(url):
    proxy = get_proxy()
    try:
        for ip in proxy:
            ip_s = '{0}:{1}'.format(ip[0], ip[1])
            proxies = {'http': ip_s}
            statu = requests.get('http://www.baidu.com', proxies=proxies)
            if statu.status_code == 200:
                dz = DZLqh()
                dz.dz(url, ip_s)
                requests.get('http://127.0.0.1:5000/delete?ip={0}'.format(ip[0]))
            else:
                requests.get('http://127.0.0.1:5000/delete?ip={0}'.format(ip[0]))
    except Exception as e:
        print(e)


if __name__ == '__main__':
    from multiprocessing import Pool

    pool = Pool(processes=4)
    pool.map(get_main, url)
    pool.close()
    pool.join()

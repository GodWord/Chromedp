import random
import time

import requests

from chromedp import Chromedp

city_list = ['beijing', 'shanghai', 'guangzhou', 'shenzhen', 'tianjin', 'hangzhou', 'nanjing', 'jinan', 'chongqing',
             'qingdao', 'dalian', 'ningbo', 'xiamen', 'kunming', 'wenzhou', 'zibo', 'zhuhai', 'mianyang', 'zhuzhou',
             'zaozhuang', 'xuchang', 'tongliao', 'zhaoqing', 'qujing', 'jiujiang', 'shangqiu', 'shantou', 'yibin',
             'zhangjiakou', 'maanshan', 'lvliang', 'fushun', 'linfen', 'weinan', 'kaifeng', 'putian', 'jingzhou',
             'huanggang', 'siping', 'chengde', 'jinjiang', 'zhuji', 'danyang', 'yuhuan', 'changshu',
             'congming', 'yuyao', 'fenghua', 'haining']


def push_cookie():
    ch = Chromedp()
    count = 0
    while True:
        ch.clear_browser_cookies()
        ch.clear_browser_cache()
        city = random.choice(city_list)
        ch.open_url('https://www.dianping.com/%s/ch10' % (city,))
        ch.wait_visible('/html/body/div[2]/div[3]/div[1]/div[1]')
        data = ch.get_cookies()
        params = {
            'cookie': ';'.join(str(value['name'] + ':' + value['value']) for value in data),
            'city': city,
        }
        print(params['cookie'])
        requests.get('http://127.0.0.1:5000/push_cookie', params=params)
        count += 1
        sleep = random.randint(5, 10)
        print('已上传cookie数量:%d个' % (count,))
        print('开始休眠:[%d]秒' % (sleep,))
        time.sleep(sleep)


if __name__ == '__main__':
    push_cookie()

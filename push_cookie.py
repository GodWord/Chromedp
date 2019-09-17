import json
import os
import random
import time

import requests

from chromedp import Chromedp

BASE_DIR = os.path.dirname(os.path.abspath(__file__))


def get_city():
    path = os.path.join(BASE_DIR, 'static/city.json')
    with open(path, 'r', encoding='utf-8') as f:
        data = json.loads(f.read())
    return list(data['city'].values())


def push_cookie():
    ua = 'Mozilla/5.0 (Linux; Android 8.0; Pixel 2 Build/OPD3.170816.012) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/75.0.3770.100 Mobile Safari/537.36'
    # ch = Chromedp(ua=ua) #移动端
    ch = Chromedp()  # PC
    count = 0
    for i in range(100):
        try:
            for city in get_city():
                ch.clear_browser_cookies()
                ch.clear_browser_cache()
                ch.open_url('http://www.dianping.com/%s/ch10' % (city,))
                # ch.open_url('https://www.dianping.com/%s/ch10' % (city,))
                # ch.wait_visible('//*[@id="app"]/div/div[2]/ul/li[1]/div/div/div/div[2]')  # 移动端
                ch.wait_visible('/html/body/div[2]/div[3]/div[1]/div[1]')  # PC
                data = ch.get_cookies()
                params = {
                    'cookie': ';'.join(str(value['name'] + ':' + value['value']) for value in data),
                    'city': city,
                    'is_mobile': False,
                }

                print(params['cookie'])
                requests.get('http://39.106.87.227:5000/push_cookie', params=params)
                count += 1
                sleep = random.randint(5, 10)
                print('已上传cookie数量:%d个' % (count,))
                print('开始休眠:[%d]秒' % (sleep,))
                time.sleep(sleep)
        except KeyboardInterrupt as e:
            ch.quit()
            return
        except Exception as e:
            print(e)
            ch.quit()
            ch = Chromedp()  # PC


if __name__ == '__main__':
    push_cookie()

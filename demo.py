# -*- coding:utf-8 -*-
from functools import reduce

__author__ = 'zhoujifeng'
__date__ = '2019/4/3 20:17'

if __name__ == '__main__':
    s = [{'name': '_lxsdk', 'value': '169e321c342c8-07f8397166badc-7a1437-2a3000-169e321c342c8',
          'domain': '.dianping.com', 'path': '/', 'expires': 1648901834, 'size': 62, 'httpOnly': False, 'secure': False,
          'session': False},
         {'name': 's_ViewType', 'value': '10', 'domain': '.dianping.com', 'path': '/', 'expires': 1617365833.169877,
          'size': 12, 'httpOnly': False, 'secure': False, 'session': False},
         {'name': '_lxsdk_cuid', 'value': '169e321c342c8-07f8397166badc-7a1437-2a3000-169e321c342c8',
          'domain': '.dianping.com', 'path': '/', 'expires': 1648901834, 'size': 67, 'httpOnly': False, 'secure': False,
          'session': False},
         {'name': '_hc.v', 'value': '6d779825-8905-c8da-ee05-ed53d0334582.1554293835', 'domain': '.dianping.com',
          'path': '/', 'expires': 1585829834, 'size': 52, 'httpOnly': False, 'secure': False, 'session': False},
         {'name': '_lxsdk_s', 'value': '169e321c343-608-3e8-2cf%7C%7C20', 'domain': '.dianping.com', 'path': '/',
          'expires': 1554295635, 'size': 39, 'httpOnly': False, 'secure': False, 'session': False}]

    test = ';'.join(str(d['name'] + ':' + d['value']) for d in s)

    print(test)

# -*- coding: utf-8 -*-

import time
import threading
import urllib.request, urllib.parse
from datetime import datetime

# 定期実行処理
def schedule():
    # 温度シミュレート(25度+α)
    now = time.time()
    temp = 25 + now % 5 + (now / 10) % 10
    # 小数点第2位に切り捨て
    str = "{0:.2f}".format(temp)
    temp = float(str)


    addr = "1a:2b:3c:46:2b:3c 1a:2b:3c:46:2b:3c 1a:2b:3c:4e:5f:6g"

    print("post")
    data = {}
    data["addr"] = addr
    url = "http://127.0.0.1:5000"
    try:
        data = urllib.parse.urlencode(data).encode("utf-8")
        req = urllib.request.Request(url, data=data, method="POST")
        with urllib.request.urlopen(req) as res:
            res = res.read().decode("utf-8")
            print(res)
    except:
        print('Error')


    addr2 = "1a:2b:3c:46:2b:3c"

    print("post")
    data = {}
    data["addr2"] = addr2
    url = "http://127.0.0.1:5000/2"
    try:
        data = urllib.parse.urlencode(data).encode("utf-8")
        req = urllib.request.Request(url, data=data, method="POST")
        with urllib.request.urlopen(req) as res:
            res = res.read().decode("utf-8")
            print(res)
    except:
        print('Error')


    addr3 = "1a:2b:3c:46:2b:3c"

    print("post")
    data = {}
    data["addr3"] = addr3
    url = "http://127.0.0.1:5000/3"
    try:
        data = urllib.parse.urlencode(data).encode("utf-8")
        req = urllib.request.Request(url, data=data, method="POST")
        with urllib.request.urlopen(req) as res:
            res = res.read().decode("utf-8")
            print(res)
    except urllib.error.HTTPError as err:
        print(err.reason)

# 定期実行設定処理
def scheduler(interval, f, wait = True):
    base_time = time.time()
    next_time = 0
    while True:
        t = threading.Thread(target = f)
        t.start()
        if wait:
            t.join()
        next_time = ((base_time - time.time()) % interval) or interval
        time.sleep(next_time)

if __name__ == "__main__":
    # 定期実行設定(3秒間隔)
    scheduler(3, schedule, True)
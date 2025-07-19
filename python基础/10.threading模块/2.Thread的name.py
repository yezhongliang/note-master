# author = 'guoshunxian'
# data = "2024/8/1 11:52"
# -- coding: utf-8 --
# python3.11

import threading
import time

"""
每一个Thread都有一个name的属性，代表的就是线程的名字，这个可以在构造方法中赋值。
如果在构造方法中没有为name赋值的话，默认就是“Thread-N”的形式，N是数字。
"""

def demo():
    for i in range(5):
        print(threading.current_thread().name + "test", i)
        time.sleep(1)

thread = threading.Thread(target=demo,name="shunxian")
thread.start()

for i in range(5):
    print("This is "+threading.current_thread().name+"main ",i)
    time.sleep(1)


# author = 'guoshunxian'
# data = "2024/8/1 11:02"
# -- coding: utf-8 --
# python3.11

import threading
import time

"""
Thread的构造方法中，最终的参数是target，我们需要将一个callable对象赋值给它，线程才能正常运行。
如果要让Thread对象启动，调用它的start()方法即可
"""
def demo():
    for i in range(5):
        print('The {} child thile '.format(i))
        time.sleep(1)
thread = threading.Thread(target=demo)
thread.start()

for i in range(5):
    print('The {} main thile '.format(i))
    time.sleep(1)
# The 0 child thile
# The 0 main thile
# The 1 main thile
# The 1 child thile
# The 2 main thile
# The 2 child thile
# The 3 main thile
# The 3 child thile
# The 4 main thile
# The 4 child thile  在主线程上打印5次，子线程上打印5次，但是打印的顺序有点奇怪
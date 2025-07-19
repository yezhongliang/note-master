"""集合点

"""
import time
import datetime
from threading import Semaphore, Thread

def demo1(index, sem):
    sem.acquire()  # 计数器-1，当前5个线程到达时计数器就为0，此时会阻塞后面5个线程
    print('{0} is waiting semaphore({1}).'.format(index, datetime.datetime.now().strftime('%Y-%m-%d-%H:%M:%S.%f')))
    time.sleep(2)
    sem.release()  # 计数器+1，当前面5个调用了release时计数器+1，计数器大于0，此时后面五个线程就可以执行了
    print('{0} is release semaphore({1}).'.format(index, datetime.datetime.now().strftime('%Y-%m-%d-%H:%M:%S.%f')))

if __name__ == '__main__':
    sem = Semaphore(5)  # 计数器初始值为1
    for i in range(10):
        Thread(target=demo1, args=(i, sem)).start()  # 启动十个线程调用test1


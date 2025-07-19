# author = 'guoshunxian'
# data = "2024/7/29 16:25"
# -- coding: utf-8 --
# python3.11
"""
多线程编程的定义：
    创建Thread对象，让他们运行，每一个Thread对象代表一个线程，在每个线程中我们可以让程序处理不同的任务，就是多线程编程

创建Thread对象的两种方法：
1、直接创建Thread，将一个callable对象从类的构造器传递出来，这个callable就是回调函数，用来处理任务。
2、便携一个自定义类继承Thread，然后重写run() 方法，在run()方法中便携任务处理代码，然后创建Thread的子类。
"""

import threading
#直接创建Thread对象
from threading import  Thread
#创建一个线程
mythread =  threading.Thread(target = function_name,args = (function_parameter1,function_parameterN))
"""参数说明：
function_name: 需要线程去执行的方法名
args: 线程执行方法接收的参数，该属性是一个元组，如果只有一个参数也需要在末尾加逗号
"""

"""方法与属性：
start()        启动线程，等待CPU调度
run()          线程被cpu调度后自动执行的方法
getName()      获取线程名称
setName()      设置线程名称
setDaemon()    用于设置为前台线程or后台线程，默认值为False，前台线程
    如果是前台线程，那么在主线程执行过程中，前台线程也在进行，主线程执行完毕后，等待前台线程执行完后，程序才停止；
    如果是后台线程，那么在主线程执行过程中，后台线程也在进行，主线程执行完毕后，后台线程不论成功与否都会停止执行；
ident          获取线程的标识符。线程标识符是非零整数，只有在调用了satrt()方法之后此属性才有效，否则只返回None
is_alive()     判断线程是否激活的。从调用start()方法启动线程，到run()方法执行完毕或遇到未处理异常而中断这段时间内，线程是激活状态的
isDaemon()和daemon属性   是否为守护线程
join([timeout])  调用此方法将会使主线程堵塞，直到被调用线程运行结束或超时，参数timeout是一个数值类型，表示超时时间，
                 如果未提供该参数，那么主调线程将一直堵塞到被调线程结束
"""

























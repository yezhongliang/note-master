# author = 'guoshunxian'
# data = "2024/7/19 16:07"
# -- coding: utf-8 --
# python3.11

"""需要导入SequentialTaskSet
如果1个TaskSet里面有多个task，执行顺序：
    1、如果task不分配权重weight，那么每一个task执行的比例是一样的，默认weight=1（随机顺序）
    2、如果task分配了权重weight，那么会按照分配的权重比例来执行（随机顺序）
    3、如果想要按照顺序执行task，需要导入SequentialTaskSet,定义task的顺序就是执行的顺序

"""
from locust import HttpUser, SequentialTaskSet ,task


class MySequentialTaskSet(SequentialTaskSet):
    @task(1)
    def task1(self):
        # 执行第一个任务
        print("Executing task1")

    @task(1)
    def task2(self):
        # 执行第二个任务，它会在task1之后执行
        print("Executing task2")

        # 你可以继续定义更多的任务，并通过@seq_task装饰器来指定它们的执行顺序


class MyUser(HttpUser):
    tasks = [MySequentialTaskSet]


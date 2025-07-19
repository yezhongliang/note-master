# author = 'guoshunxian'
# data = "2024/7/17 10:08"
# -- coding: utf-8 --
# python3.11


from locust import  TaskSet, task ,User


class MyUserBehavior(TaskSet):
    def setup(self):
        print('taskset的setup 每个任务开始前执行')

    def teardown(self):
        print('taskset的teardown 每个任务结束前执行')

    def on_start(self):
        # 虚拟用户启动Task时运行
        print('on_start 虚拟用户启动Task前运行')

    def on_stop(self):
        # 虚拟用户结束Task时运行
        print('on_stop 虚拟用户结束Task后运行')

    @task(2)
    def index(self):
        self.client.get("https://www.baidu.com/1")
        self.client.get("/")

    @task(1)
    def profile(self):
        self.client.get("/index")


class WebsiteUser(User):
    def setup(self):
        print('setup 开始测试前执行')

    def teardown(self):
        print('teardown 测试结束后执行')

    task_set = [MyUserBehavior.index,MyUserBehavior.profile]
    min_wait = 5000
    max_wait = 9000


'''
上面的执行顺序：
    taskset的setup 每个任务开始前执行
    on_start 虚拟用户启动Task前运行
    task
    on_stop 虚拟用户结束Task后运行
    taskset的teardown 每个任务结束前执行

总结执行顺序：
Locust setup → TaskSet setup → TaskSet on_start →
TaskSet tasks → TaskSet on_stop → TaskSet teardown →
Locust teardown

每个虚拟用户执行操作时运行on_start方法，退出时执行on_stop方法
'''



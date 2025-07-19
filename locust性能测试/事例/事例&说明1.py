import  locust
from locust import HttpLocust,user,tag,task,HttpUser,User

class WebsiteUser(locust.HttpUser):
    """
        wait_time = between(0.5, 10)  #每个用户在每次任务执行之间等待0.5到10秒
        wait_time = constant(1)       #每个用户每次任务执行之间等待1秒
        wait_time = constant_pacing(1)  # 每个用户在1秒内运行1次
        如果不设置wait_time的话，那么默认值是1秒
    """
    # 设置等待时间间隔 5~15秒，每个task间隔5~15秒，一般设置1~2，这里用5~15举例
    wait_time = locust.between(5, 15)


    """
    client.get 和client.post 和requests的用法是一样的，下面的两个方法中传的是json数据
    """
    def on_start(self):
        self.client.post("/login", {
            "username": "test_user",
            "password": "123456"
        })

    @locust.task
    def index(self):
        self.client.get("/")
        self.client.get("/static/assets.js")

    @locust.task
    def about(self):
        self.client.get("/about/")






"""执行顺序事例?????????????????????????????????????????"""
class UserBehavor(locust.TaskSet):
    #这个方法是TaskSet的Setup
    def setup(self):
        """
        setup方法是在每个TaskSet实例被创建并且其任务开始执行之前被调用,做一些初始化工作
        作用：设置测试数据 登录到系统（请求登录接口） 预热缓存等等
        setup 方法只会在每个 TaskSet 实例的生命周期中调用一次，而不是在每个任务执行前都调用
        """
        self.client.tasksetpost(url = "/login",json = {"username": "user", "password": "pass"})
        print('taskset setup')

    def teardown(self):
        """
        teardown方法是在TaskSet实例完成所有任务执行之后被调，做一些清理工作
        作用：退出登录、清理测试数据、关闭数据库连接等
        teardown 方法也只会在每个 TaskSet 实例的生命周期结束时调用一次
        """
        print('taskset teardown')
        self.client.post(url = "/logout",json = None)


    #虚拟用户启动task时运行
    def on_start(self):
        """
        当做requests.session来使用，常用于操作登录接口，记住登录态
        因为上面类继承的是TaskSet类，所有这里的on_start / on_stop只会执行一次，无论下面有多少个task
        """
        print('start')

    #虚拟用户结束task时运行
    def on_stop(self):
        print('end')

    @locust.task(2)
    def index(self):
        self.client.get('/')

    @locust.task(1)
    def profile(self):
        self.client.get('/profile')

"""上面的执行顺序为：
    taskset setup
    on_start
    task
    on_stop
    taskset teardown
"""







# 自己写一个全的!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!
class MyTasks(locust.TaskSet):

    """
    wait_time = between(0.5, 10)  #每个用户在每次任务执行之间等待0.5到10秒
    wait_time = constant(1)       #每个用户每次任务执行之间等待1秒
    wait_time = constant_pacing(1)  # 每个用户在1秒内运行1次
    """
    wait_time = locust.between(1, 2)



    """
    装饰器@task() 括号里可以填写参数，也是表示权重，当同一个类中有多个task的时候如果不设置权重，就按正常比例分，每一个的比例相同
    如果taskA设置了1，taskB设置了5，那么taskB的执行几率是taskA的5倍    

    装饰器tag，打标签功能，选择执行拿些带上某些标签的task，tag传字符串
    命令行执行时：参数--exclude-tags与--tags参数作用相反
    """

    @tag("No2")
    @locust.task(1)
    def index_page(self):
        self.client.get(url = "https://www.baidu.com/123")
    @tag("No1")
    @locust.task(5)
    def list_page(self):
        self.client.post(url = "/list")


class User1(locust.HttpUser):
    """
    weight的作用：分配用户权重
    1、假如设置了100个用户，User1和User2的权重分别是3和1，那么User1类分配的用户是User2类的3倍用户
    2、weight的默认值是1
    """
    weight = 3

    """
    1、host可以是IP或者域名，用户拼接接口路径，所以下面的URL只需要填写接口的路径即可，会自动拼接，相当于一个全局变量
    2、但是如何使用命令行的方式执行，并且换了一个host，那么优先用的命令行输入的host
    3、如果是多个类连接到同一个host，有两种做法
        做法一：每一个类都去声明相同的host
        做法二：写一个基类BasHttpUser，这个基类继承HttpUser，后面的User类再继承这个基类即可
            class BasHttpUser(HttpUser):
                host = "192.168.0.1"
            class User3(BasHttpUser):
                ...
    """
    host = "192.168.0.1"
    @locust.task()
    def task1(self):
        self.client.get(url = "/")
class User2(locust.HttpUser):
    weight = 1
    @locust.task()
    def task2(self):
        self.client.post(url = "/")


class MyUser(HttpUser):
    """
    task数据类型为列表时，则每次执行任务时，都会从task属性中随机选择
    task数据类型为字典时，则每次执行任务时，按照字典值比例执行任务
    """
    #task数据类型为列表,随机选中一个
    tasks1 = [MyTasks.index_page,MyTasks.list_page]

    #task数据类型为字典，按照字典值比例执行任务,执行比例是1：10
    # tasks2 = {MyTasks.index_page:1,MyTasks.list_page:10}


















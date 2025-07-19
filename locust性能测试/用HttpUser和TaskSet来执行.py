# author = 'guoshunxian'
# data = "2024/7/17 16:20"
# -- coding: utf-8 --
# python3.11

from locust import TaskSet,HttpUser,between,task

"""
1、当只有1个用户的时候，on_start方法只会执行1次
2、当有10个用户的时候，on_start方法会执行10次
所以每个用户都会去在执行task前去执行on_start方法去做前置操作
"""
#先声明task任务集
class UserBahavior(TaskSet):
    #声明每个任务之间间隔多少时间
    wait_time = between(0.5,1)


    def login(self):   #登录操作,这里不需要操作token了，因为client有session的功能，自动记住登录状态
        self.client.post(url = "/UserApi/login",json = {"username":"admin","password":"123456"})


    def on_start(self):
        """用来进行登录操作,包括请求登录接口和保存登录的token信息等等"""
        self.login()


    # def on_stop(self):
    #     """用来清理测试数据等等"""
    #     pass

    @task(weight=1)
    def GetCourseList(self):
        self.client.post(url = "/CourseApi/semesterCourseList",json={"isstudy":1,
                                                                     "reqtimestamp":1721207051422,
                                                                     "search":"",
                                                                     "semester":"2023-2024",
                                                                     "term":"0"})


    @task(weight=1)
    def GetTaskList(self):
        """
        获取任务接口，目前里面是空的，没有数据
        """
        self.client.post(url = "/Futurev2/Task/getTaskList",json = {"page":1,
                                                                    "reqtimestamp":1721210627275,
                                                                    "size":20,
                                                                    "type":1})


class WebsiteUser(HttpUser):
    host = "https://openapiv5.ketangpai.com/"

    tasks = [UserBahavior]

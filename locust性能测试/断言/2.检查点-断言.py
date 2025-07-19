"""断言
从网上看到可以用catch_response=True设置断言
所以自己写断言的方式assert的方式来断言

locust默认情况下会使用默认的检查点，比如当接口超时、链接失败等原因是会自动判断失败的

如接口测试一样，断言一般不会只去断言状态码，还会去断言响应体里面的其他内容
"""
from locust import task,constant,HttpUser,TaskSet

"""自己写的，用assert"""
class UserBahavior1(TaskSet):
    @task()
    def task_1(self):
        response = self.client.get(url = "123")
        assert  response.status_code == 200, "断言成功，状态码为200"
        assert  response.status_code != 200, "断言成功，状态码不为200"
        assert  response.data.msg == "登录成功" , "断言成功，登录成功"


class MyUser(HttpUser):
    constant(1)
    tasks = [UserBahavior1]
    host = "https://www.baidu.com"





"""网上的例子
使用self.client提供的catch_response=True`参数， 添加locust提供的ResponseContextManager类的上下文方法手动设置检查点。
ResponseContextManager里面的有两个方法来声明成功和失败，分别是 success和 failure。其中failure方法需要我们传入一个参数，内容就是失败的原因。
"""
from requests import codes
from locust import between
class DemoTest(HttpUser):
    host = 'https://www.baidu.com'
    wait_time = between(2, 15)

    def on_start(self):
        # 通过手动传入catch_response=True 参数手动设置检查点
        with self.client.get('/',catch_response=True) as r:
            if r.status_code == codes.bad:
                r.success()
            else:
                r.failure("请求百度首页失败了哦哦")

    @task
    def search_locust(self):
        with self.client.get('/s?ie=utf-8&wd=locust', catch_response=True) as r:
            if r.status_code == codes.ok:
                r.success()
            else:
                r.failure("搜索locust失败了哦哦")





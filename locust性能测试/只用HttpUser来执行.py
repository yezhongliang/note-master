# author = 'guoshunxian'
# data = "2024/7/17 16:14"
# -- coding: utf-8 --
# python3.11

from locust import HttpUser, task, between


class WebsiteUser(HttpUser):
    # 设置用户执行任务之间的等待时间
    wait_time = between(1, 2.5)
    host = "http://192.168.0.1"

    @task(weight=1)  # 首页访问任务，权重为1
    def view_home_page(self):
        """用户访问首页"""
        self.client.get("/")
        print("Visited home page")  # 注意：在分布式运行时，这些print语句可能不会按预期显示

    @task(weight=1)  # 登录任务，权重为2，意味着它将被执行得更频繁
    def login(self):
        """用户登录"""
        # 假设登录需要POST请求到/login，并且需要用户名和密码
        response = self.client.post("/login", json={"username": "testuser", "password": "testpass"})
        if response.status_code == 200:
            print("Login successful")
        else:
            print("Login failed", response.status_code)


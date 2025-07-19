"""locust参数化

"""

from locust import HttpLocust, task, TaskSet, between
import queue


result_list = []
for index in range(100):
    data = {
            "username": "test%04d" % index,
            "password": "pwd%04d" % index,
            "email": "test%04d@debugtalk.test" % index,
            "phone": "186%08d" % index,
        }
    result_list.append(data)



class UserRegister(TaskSet):
    @task
    def test_register(self):
        # get_nowait() 取不到数据直接崩溃，直接跳到except； get() 取不到数据会一直等待
        try:
            # 从队列中取出数据
            data = eval(self.locust.user_data_queue.get_nowait())
            print("测试数据:%s" % data)
        # 使用get_nowait()方法，取不到数据，就进入这里
        except queue.Empty:
            print("测试数据已用完，结束！")
            exit(0)
        print('注册的用户账号: {}, 密码: {}' \
              .format(data['username'], data['password']))
        payload = {
            'username': data['username'],
            'password': data['password']

        }
        self.client.post('/register', data=payload)


class WebSiteUser(HttpLocust):
    host = 'https://www.testregister.com'
    task_set = UserRegister
    # 创建队列，先进先出
    user_data_queue = queue.Queue()
    # 循环加入队列
    for index in range(100):
        data = '''{
            "username": "test%04d",
            "password": "pwd%04d",
            "email": "test%04d@testregister.test",
            "phone": "186%08d"
        }''' % (index, index, index, index)
        # 将data存入队列中
        user_data_queue.put_nowait(data.replace(' ', '').replace('\n', ''))
        # print(user_data_queue.get())

    wait_time = between(1, 1)


if __name__ == '__main__':
    import os
    os.system('locust -f locust_register.py')





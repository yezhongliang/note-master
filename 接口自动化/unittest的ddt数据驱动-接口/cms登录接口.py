import unittest
import  requests
import ddt
from HTMLTestRunner3 import HTMLTestRunner
from python基础.各种包的学习.time模块 import File_time_create_other_function


@ddt.ddt
class Cms_login(unittest.TestCase):
    headers = {'Content-Type':'application/x-www-form-urlencoded'} #公有类属性

    @ddt.file_data(r'cms_login.yaml')
    def test_cms_login1(self,method,url,params):
        res = requests.request(method=method,  url=url,  params=params,headers = self.headers).json()
        print(res)
        #接口自动化的断言都是要对返回的数据进行校验
        msg = res['msg']
        self.assertEqual(msg,'登录成功！')  #A 和B 的位置是可以调换的，注意!!!


if __name__ == '__main__':
    #第一步：声明一个suite
    suite = unittest.TestSuite()
    #把用例加载到suite里面
    loader = unittest.TestLoader()

    suite.addTests(loader.loadTestsFromTestCase(Cms_login))
    #创建一个执行器runner
    file  = open(file=File_time_create_other_function(),mode='wb')
    runner = HTMLTestRunner(stream=file, verbosity=2, title='接口驱动一下',
                            description='疯狂星期一，今天好挤')
    #执行器执行套件
    runner.run(suite)
    file.close()

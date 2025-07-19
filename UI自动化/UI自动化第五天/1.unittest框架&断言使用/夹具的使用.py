# -*- coding: utf-8 -*-
"""
@Time    :2022/10/26 9:48
@version :Python3.7.4
@Software:pycharm2020.3.2
"""
"""
TestFixtrue夹具
包含setup和teardown
    一条用例就会触发一词setup和teardown，如果有10条用例，那么会触发10次
还有setupclass和teardownclass
    无论测试类里面有多少条用例，都只会触发一次setupclass和teardownclass
    
setup和setupclass方法的区别？
1.setup是实例方法，setupclass是类方法
2.setup运行的次数取决于测试类里面用例的数量，setupclass无论测试类里面有多少条用例都只运行一次
3.setupclass使用的使用需要带上类装饰器@classmethod
"""
import  unittest

class Test_Login(unittest.TestCase): #定义一个测试类，这个测试类的名字是：登录的测试类
    def setUp(self) -> None: #用于测试环境的初始化工作准备，例如实例化对象、浏览器最大化，打开网站
        print('这是开始工作。。。。。。。。。')

    def tearDown(self) -> None:
        print('这是结尾工作。。。。。。。。。')


    @classmethod
    def setUpClass(cls) -> None:
        print('setupclass--只执行一次')
    @classmethod
    def tearDownClass(cls) -> None:
        print('teardownclass--只执行一次')

    def test_login_dengluchenggong(self):
        print('这个用例是登录成功的用例')

    def test_1_login(self):
        print('这个用例是登录失败的用例------1')

    def test_A_login(self):
        print('这个用例是登录失败的用例------A')

    def test_a_login(self):
        print('这个用例是登录失败的用例------a')


if __name__ == '__main__':  #测试执行的入口，py文件如果有这个if __name__ == '__main__':就会执行这个代码下面的操作
    unittest.main()  #这句话的意思，执行当前文件的所有unittest的用例




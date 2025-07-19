# -*- coding: utf-8 -*-
"""
@Time    :2022/8/23 0:26
@version :Python3.7.4
@Software:pycharm2020.3.2.用例执行的三种方式
"""
"""测试夹具fixture
setup()和teardown()----setupclass()和teardown()运行的逻辑：
1.setupclass()和teardown()：无论有多少条测试用例，都只会运行一次
2.setup()和teardown()：如果有10条用例，就会执行10次setup和teardown
3.setupclass()和teardown()使用的时候需要配合类装饰器@classmethod来使用

"""
import  unittest
from shop_zhuce import zhuce
from selenium import  webdriver
from time import sleep

#需求：每执行一条测试用例，都会调用一次setup和teartdown

class Test_zhuce(unittest.TestCase):
    # def setUp(self) -> None:
    #     print('每个用例执行前的准备工作')
    #
    # def tearDown(self) -> None:
    #     print('每个用例执行完后的回收工作')

    #输入正确username=admin password=123456
    def test_zhuce1(self):  #执行的顺序-setup-》test_zhuce1-》teardown
        zhuce('admin','123456')

    #输入username=admin，password=666
    def test_zhuce2(self): #执行的顺序-setup-》test_zhuce2-》teardown
        zhuce('admin','666')

    #输入username=haha，password=111
    def test_zhuce3(self): #执行的顺序-setup-》test_zhuce3-》teardown
        zhuce('haha','111')

    def test_zhuce4(self):
        zhuce('hahaha','111111111111')

    def test_zhuce5(self):
        zhuce('zhangsan','1234567')

    def test_zhuce6(self):
        zhuce('lisi','1234567777')

if __name__ == '__main__':
    unittest.main()
# -*- coding: utf-8 -*-
"""
@Time    :2022/8/22 23:45
@version :Python3.7.4
@Software:pycharm2020.3.2.用例执行的三种方式
"""

"""setup()和teardown()----setupclass()和teardown()运行的逻辑：
1.setupclass()和teardownclass()：无论有多少条测试用例，都只会运行一次
setup()和teardown()：如果有10条用例，就会执行10次setup和teardown
2.用例执行的三种方式.setupclass()和teardown()使用的时候需要配合类装饰器@classmethod来使用
3.类级别的方法，使用的时候，都要带上@classmethod这装饰器，不然会报错===@classmethod-》类装饰器
"""
import  unittest
from shop_zhuce_cls import zhuce_cls
from selenium import  webdriver
from time import sleep

#需求1：只打开一个浏览器和关闭一次浏览器

class Test_zhuce(unittest.TestCase):
    @classmethod
    def setUpClass(cls) -> None:
        print("不管执行多少个测试用例，只执行一次这个方法")
        global driver  #声明一个全局变量，在类中间和这个py文件里面都可以用
        driver = webdriver.Chrome()  #实例化一个对象driver
        #打开网站
        driver.get('http://39.98.138.157/shopxo/index.php?s=/index/user/reginfo.html')
        #窗口最大化
        driver.maximize_window()
        sleep(3)

    @classmethod  #对于类级别的方法使用，需要类装饰器
    def tearDownClass(cls) -> None:
        print("不管执行多少个测试用例，只执行一次这个方法")
        driver.quit()

    #输入sername=admin password=123456
    def test_zhuce1(self):
        zhuce_cls(driver,'admin','123456')

    #输入username=admin，password=666
    def test_zhuce2(self):
        zhuce_cls(driver,'admin','666')

    #输入username=haha，password=111
    def test_zhuce3(self):
        zhuce_cls(driver,'haha','111')

if __name__ == '__main__':
    unittest.main()























































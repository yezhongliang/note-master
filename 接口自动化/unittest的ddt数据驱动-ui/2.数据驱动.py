""""""
"""数据驱动：
数据驱动测试的方法是将测试数据与测试用例脚本分离的一种方法。
形成数据与操作分开的形式。
数据：正确的账号，正确的密码；正确的账号，错误的密码等等
操作：输入账号和密码
优势：实现同一脚本对多组数据进行测试，最终实现数据与脚本的分离，便于维护与扩展
ddt中模块主要用到data-数据、unpack-解包、file_data-数据文件  ==都是装饰器
"""

from selenium import  webdriver
from time import sleep
import  ddt
import unittest
# from ddt import ddt,file_data,data,unpack
#ddt:


@ddt.ddt #在类上面使用的装饰器，叫做类装饰器（类级别）； 在实例方法上面使用的装饰器，叫函数装饰器（函数级别）
class My_Test(unittest.TestCase):
    def setUp(self) -> None:
        # global driver
        self.driver = webdriver.Chrome()
        # self.driver.get('https://www.baidu.com')
        self.driver.get('http://127.0.0.1:5000/signin')
        self.driver.implicitly_wait(10)
        sleep(1)

    def tearDown(self) -> None:
        self.driver.quit()

    #驱动源码里面的字符串
    # @ddt.data('test1_txt', 'test2_txt','test3_txt','test4_txt')  # 参数用字符串保存来操作
    # def test01(self,data):
    #     self.driver.find_element('id','kw').send_keys(data)
    #     sleep(5)

    #驱动源码里面的字典的。
    # @ddt.data({'username':'15521048080','password':'123456'})  #字典用列表保存来操作，入参的名字要和键的名字相同，不然会报错
    # @ddt.unpack   #unpack 解包，把字典里面的值拿出来
    # def test02(self,username,password):
    #     self.driver.find_element('name','username').send_keys(username)
    #     sleep(1)
    #     self.driver.find_element('name', 'password').send_keys(password)
    #     sleep(4)




    # @ddt.file_data(r'D:\TestTool\project_for15\接口自动化\unittest的ddt数据驱动-ui\data\file_data.json') #绝对路径
    # @ddt.file_data(r'file_data.json')---相对路径
    # def test04(self,username,password):
    #     self.driver.find_element('name','username').send_keys(username)
    #     self.driver.find_element('name','password').send_keys(password)
    #     sleep(5)
    #     A=self.driver.title
    #     B=self.driver.current_url
    #     self.assertEqual(A,B)

    # @ddt.file_data(r'D:\TestTool\project_for15\接口自动化\unittest的ddt数据驱动\file_data.yaml')
    # def test_05(self,username,password):
    #     self.driver.find_element('name','username').send_keys(username)
    #     self.driver.find_element('name','password').send_keys(password)
    #     sleep(5)

    @ddt.file_data(r'D:\TestTool\project_for15\接口自动化\unittest的ddt数据驱动-ui\data\file_data.yaml')
    def test_login(self,username,password):
        self.driver.find_element('name','username').send_keys(username)
        sleep(1)
        self.driver.find_element('name','password').send_keys(password)
        sleep(2)

if __name__ == '__main__':
    unittest.main()






























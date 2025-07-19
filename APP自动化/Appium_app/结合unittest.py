"""初始化操作步骤：
1.从appium中引入webdriver
2.添加配置
    deviceName：设备名称
    platfromName：测试平台名称  无非就是安卓或者IOS
    platformVersion：平台版本   手机系统的版本
    appPackage：被测app的包名    包名通过：adb shell pm list packages -3
    appActivity：测试app启动入口
    adb shell dumpsys window windows | findstr mFocusedApp：查看当前打开的应用包名和界面
    adb shell dumpsys activity | find "mFocusedActivity"：查看当前打开的界面
3.创建驱动
"""
#从appium中引入webdriver
from appium import  webdriver
from time import sleep
import unittest
from HTMLTestRunner3 import  HTMLTestRunner

#找到设备，打开对应的应用,今日头条极速版为例
des = {
    "deviceName":"127.0.0.1:62001",
    "platformName":"Android",
    "appPackage":"com.ss.android.article.lite",
    "appActivity":"com.ss.android.account.v2.view.AccountLoginActivity",
    "platformVersion":"5.1.1"
    # "noReset":"True"  #是否重置测试环境，可要可不要
}
class Test_toutiao(unittest.TestCase):
    def setUp(self) -> None:
        #实例化对象
        self.driver = webdriver.Remote('http://127.0.0.1:4723/wd/hub',desired_capabilities=des)

    def test_login(self):
        self.driver.find_element('id','com.ss.android.article.lite:id/ahx').send_keys('888888')
        sleep(2)
        self.driver.find_element('id','com.ss.android.article.lite:id/ahv').send_keys('11111')


        sleep(2)
    def tearDown(self) -> None:
        pass
        print(123456)
        #后置操作一般是退出整个app，或者回到首页
        # self.driver.close()
        # sleep(10)

if __name__ == '__main__':
    #实例化一个套件suite
    suite = unittest.TestSuite()

    #把用例加载进去，addtest addtests
    suite.addTest(Test_toutiao('test_login'))

    #创建一个执行器runner
    file1  =  open(file ='./report.html',mode='wb' )
    runner = HTMLTestRunner(stream=file1, verbosity=2, title='App自动化', description=None)

    #执行器执行套件
    runner.run(suite)

    file1.close()
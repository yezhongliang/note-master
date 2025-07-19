# -*- coding: utf-8 -*-
"""
@Time    :2022/9/5 22:21
@version :Python3.7.4
@Software:pycharm2020.3.2
"""


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
from appium import webdriver
from time import  sleep

#找到设备，打开对应的应用,今日头条极速版为例
des = {
    "deviceName":"127.0.0.1:62001",
    "platformName":"Android",
    "appPackage":"com.ss.android.article.lite",
    "appActivity":"com.ss.android.account.v2.view.AccountLoginActivity t41",
    "platformVersion":"5.1.1"
    # "noReset":"True"  #是否重置测试环境，可要可不要
}

#实例化对象
driver = webdriver.Remote('http://127.0.0.1:4723/wd/hub',desired_capabilities=des)

#元素定位的两个工具：inspecter定位（appium自带）、UIautomator viewer（SDK自带-tools里面）
#根据id选中手机号输入框
driver.find_element('id','com.ss.android.article.lite:id/ahx').send_keys('181818')

sleep(2)

#根据id输入验证码输入框
xpath ='/hierarchy/android.widget.FrameLayout/android.widget.LinearLayout/android.widget.FrameLayout/android.widget.LinearLayout/android.widget.FrameLayout/android.widget.LinearLayout/com.ss.android.account.customview.slidingdrawer.SuperSlidingDrawer/android.widget.FrameLayout/android.widget.RelativeLayout/android.widget.RelativeLayout[2]/android.widget.EditText'

driver.find_element('xpath',xpath).send_keys('666')
sleep(10)

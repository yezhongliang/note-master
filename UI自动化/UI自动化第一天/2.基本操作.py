# -*- coding: utf-8 -*-
"""
@Time    :2022/8/18 22:58
@version :Python3.7.4
@Software:pycharm2020.3.2.
"""
"""
打开网页：get(url)
刷新页面：refresh()
前进forward()
后退：back()
窗口最大化：maximize_window()
窗口最小化:minimize_window()
截屏：get_screenshot_as_file(保存路径)
关闭浏览器：close()
    关闭浏览器是会关闭当前的窗口，不会退出整个浏览器，如果1个浏览器有10个窗口，那么会关闭1个窗口
退出浏览器：quit()
    如果1个浏览器有10个窗口，那么会退出整个浏览器，10个窗口也退出了
"""#F12用法、ctrl+F的用法

#导包
from selenium import  webdriver
from time import sleep

#实例化一个driver对象，驱动的谷歌浏览器
driver = webdriver.Chrome()

#driver对象去打开一个web的网址：一定要加上协议http，不加会报错
#此时已经去到百度的首页了
driver.get('https://www.baidu.com')

#窗口最大化
driver.maximize_window()

#休眠2秒
sleep(2)


#窗口最大化
driver.maximize_window()

#刷新一下
driver.refresh()

#截屏，注意，截图截到的图片格式要求是png，jpg会警告
driver.get_screenshot_as_file('test.jpg')

#休眠2秒
sleep(2)

#关闭窗口：close()
driver.quit()


# 面试题：close()和quit()的区别？
# 1.close会关闭当前的窗口，有10个，关闭1个；quit会关闭所有的窗口，有10个，关闭10个。
# 2.close关闭网页后不会进行资源的回收，临时文件会越来越多；quit会对资源进行释放。
# 3.都会退出session。

# 4.close常用于一个用例执行完后的操作；quit常用于整个脚本运行完后的操作。

# 元素定位的方式有哪些？

#  你常用的定位方式是哪个？

#xpath的相对路径怎么写？

# 怎么去切换窗口

#怎么去处理弹窗

#8种定位方式，哪种是最快的？
# 最快：css  id      最慢：xpath

# 定位不到元素的原因有哪些？
# 1.新窗口没有切换--switch_to.window
# 2.有iframe没有去切换 --switch_to.iframe
# 3.有alert弹窗没有处理 --switch_to.alert
# 4.因为网络的原因，页面元素没有加载完成就去操作---给智能等待
# 5.网站上面有广告，把要定位的元素遮挡住了（广告不定时弹出来）
# 6.变化的id（auto_id）--用其他的定位方法
# 7.当前元素不可见（JS去把元素设置为可见就行了）







# -*- coding: utf-8 -*-
"""
@Time    :2022/8/22 20:06
@version :Python3.7.4
@Software:pycharm2020.3.2.用例执行的三种方式
"""
"""图像识别技术
验证码识别操作：
1.对元素截图：思路-》先对整个界面截图，再从截图中截取需要的图片范围
    第一步：截取整个界面
    第二步：导包 from PIL import Image  ->pip install pillow
    第三步：定位到截图的元素->截取图片范围->保存截图
        image = Image.open('quantu.png')
        image = image.crop([left,top,right,bottom])
    第四步：保存截图, image.save('code.png')
2.调用百度开放平台的接口，图像识别的接口，让百度那边处理完后给我们返回那些验证码，再输入到验证码的输入框 （用的比较少）    
"""































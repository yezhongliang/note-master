# -*- coding: utf-8 -*-
"""
@Time    :2022/9/6 22:44
@version :Python3.7.4
@Software:pycharm2020.3.2
"""
"""
简介：
uiautomator2是一个可以是使用python对Android设备进行UI自动化的库，
底层是基于谷歌的uiautomator。
目前只支持android平台的原生应用测试

特点：
功能丰富：设备和开发机可以脱离数据线，可以通过wifi相连

安装：
    1.pip install --pre uiautomator2
    安装完1后，确认好模拟器已经连接上（adb devices），
    然后打开cmd 输入 python -m uiautomator2 init,
    初始化完成后模拟器会有一个ATX服务
    2.安装可视化UI查看器
    打开cmd 输入 pip install weditor   这条先不执行（pip install weditor==0.6.4）
    或者  pip install --pre --upgrade weditor
    如果报错则执行：git clone https://github.com/alibaba/web-editor.git再执行pip3 install -e weditor
    3.都执行完上面的步骤后就可以打开了 在dos窗口执行：python -m weditor
"""













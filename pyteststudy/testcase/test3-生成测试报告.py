# -*- coding: utf-8 -*-
"""
@Time    :2022/10/27 14:29
@version :Python3.7.4
@Software:pycharm2020.3.2
"""

import pytest
"""
pytest生成测试测试报告的方式有两种：
    1.用pytest-html这个插件生成html的报告
        步骤：pip install pytest-html
              在配置文件里面配置好生成测试报告的路径和文件名即可
    2.用allure（中文翻译：魅力报告）生成非常好看的测试报告
        步骤：需要安装好allure，然后把allure的根目录配置到环境变量
        下载地址：https://github.com/allure-framework/allure2/releases
        配置教程：https://blog.csdn.net/gaomingjian218/article/details/121071149
        运行allure需要jdk环境：需要配置好jdk环境：http://t.csdn.cn/z50fe http://t.csdn.cn/z50fe
        JDK包下载： https://www.oracle.com/cn/java/technologies/downloads/#jdk19-windows
        先需要去生成测试数据，再根据测试数据转换成为allure的测试报告
            生成测试数据命令：pytest testcasePath --alluredir=resultPath
            数据转换成报告命令：allure generate resultPath -o reportPath --clean
            -o 参数表示output，输出到某个目录里面
            --clean用来清除之前生成过的数据，因为allure每一次生成报告都需要在一个空的文件夹
"""













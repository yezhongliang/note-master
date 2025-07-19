# -*- coding: utf-8 -*-
"""
@Time    :2023/1/2 11:08
@version :Python3.7.4
@Software:pycharm2020.3.2
"""

"""pytest的setup和teardown
unittest的setup和teardown是一样用法，但是会有警告，而且这两个方法是没有提示
unittest的setup_class和teardown_class是一样用法，而且这两个方法是没有提示
"""
import pytest
import unittest

class Test_pytest():
    # def setup(self):
    #     print('开始')
    #
    # def teardown(self):
    #     print('这是pytest的teardown方法，用来做环境的初始化')

    def setup_class(self):
        print('类级别的开始')

    def teardown_class(self):
        print('类级别的结束')

    def test_01(self):
        print('这是第一条测试用例，查看是否会调用setup和teardown')

    def test_02(self):
        print('这是第二条测试用例，查看是否会调用setup和teardown')

if __name__ == '__main__':
    pytest.main()


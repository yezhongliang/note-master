# -*- coding: utf-8 -*-
"""
@Time    :2022/10/27 17:20
@version :Python3.7.4
@Software:pycharm2020.3.2
"""

#这个文件是整个文件夹的执行用例的入口

import pytest


if __name__ == '__main__':
    pytest.main()

#逻辑
# 在run.py里面去执行用例，首先会去加载pytest.ini配置文件里面的内容，确定好testpath，以及匹配的规则，
# 然后再去执行里面的可选项配置

    
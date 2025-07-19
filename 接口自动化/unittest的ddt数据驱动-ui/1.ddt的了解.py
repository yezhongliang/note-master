import unittest
import ddt

"""
ddt是为了驱动unittest所构建的测试用例而生,全称：data driver test
所以ddt一般都是结合着unittest在使用：
pip install ddt
"""
"""
我们通过运行ddt和unittest构建的用例，我们发现，
1、数据结合ddt可以驱动测试用例的生成，测试用例中的数据的传入；
2、数据是迭代数据；
    str、list、dict、tuple
3、ddt所有的方法都是通过装饰器来使用
4、ddt兼容了键值对的无序特性
"""

"""
为什么要做数据驱动，特别是在接口自动化里面。
    为了减少代码的重复编写，以及把数据与业务区分开来，更加关注我们数据的校验

测试数据，也是数据
数据的封装有几种类型？
1、参数化
2、方法化/函数化
3、类化
4、文档化---数据驱动，把参数、数据放到文件里面去读取，
    文件的读取：
        txt    open     with open __enter__  __exit__
        excel xlrd  xlwt  openpyxl  pandas
        yaml  with open 
        json  with open
"""











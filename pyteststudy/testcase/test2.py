""""""
"""
编写测试用例对比：
    unittest:运行一条，需要在一个类里面继承unittest.TestCase
    pytest:不需要继承，可以单独运行方法，也可以运行类
    pytest:
        测试类：以Test开头，如果不以Test来命名类，那么不被pytest所识别
        测试方法：以test开头，如果不以test来命名类，那么不被pytest所识别
    unittest：
        测试类：所有的测试类都要继承unittest.TestCase

生成测试报告对比：
    unittest需要导入HTMLTestRunner，使用到第三方模板
    pytest只需要下载pytest-html，即可，添加到ini配置文件里面

运行的方式：
    1:命令行运行(不需要导入pytest)：pytest 文件名  
        pytest -s -vv test1--各种装饰器学习.py 或者 pytest -s test1--各种装饰器学习.py -vv
    2：使用main方法(需要导入pytest) ,pytest.main()  此方法需要配合 配置文件来使用

pytest.ini文件说明，这个文件是用来存放pytest框架的配置信息的
testpaths=./testcase  #存放的是装载测试用例的文件夹的路径
python_files = test*.py  #说明测试用例以test开头.py结尾
python_classes = Test*  说明满足Test开头的所有类，都是测试类
python_functions=test*  说明满足test开头的所有方法，都是测试级别的方法
参数说明：
-s:表示的是输出print函数里面的内容
-vv 参数表示的是控制台日志的详细程度，对应的参数有 -v -vv 或者不写-v
--maxfail=1，最大有一条用例失败，那下面的用例就不会去执行了，累积失败的用例条数
    常用场景1：冒烟测试，我冒烟测试都不通过，就没有必要执行下面的操作了
    开发提测，我去跑冒烟用例，连冒烟都不过的就没有必要执行下面的全量测试了。
    常用场景2：正常跑自动化用例，错误累积到最大值的时候，不会再执行，通过率没有达到90%，此次自动化不通过，查找原因
    你们UI自动化和接口自动化的通过率为多少的时候说明这次的自动化测试通过？
        98% ，有2%是失败的，有可能是因为网络的波动造成的。
--reruns NUM，失败的用例重跑多少次，用法--reruns 3 ，重跑三次
    常用场景：在平时的测试当中，有可能受到网络的影响或者其他因素的，
    让本来成功的用例执行失败，此时就要让他去重跑。
-n 2，多线程运行，目的是为了提高用例的执行速度，用例极少的时候，不会有多大影响，当用例多起来的时候，
执行效率就会得到非常大的提高，需要安装pytest-xdist这个插件，可以多少个线程去运行，取决于电脑的核数
在用例极少的情况下，所花的时间不减反增，是因为线程启动也是需要时间

--html，生成测试报告的插件，需要声明好报告的路径以及名字 ./表示当前路径 ../表示当前路径的上一层
    --html=./report/report.html

-m=标签名，可以给用例打上标签，打上冒烟、正向、反向用例的标签，执行用例的时候可以单独执行这些
带有标签的用例。应用场景：P0优先级的作为一个标签,PO是冒烟测试用例，P1优先级的作为另一个标签
提示：标签不注册的话，会有警告，但是不影响执行,如何注册？
    在配置文件里面加一个markers的字段
    marker=
        P0
        P1
        P2
    如何执行多个mark标签？在配置文件里面如何写 -m='P0 or P1'
    单个mark标签：-m = P0

@pytest.mark.skip:跳过打上此装饰器的用例
使用场景：有一些用例还对应的功能没有开发完，但是又不想注释掉，可以使用这个skip的方式去跳过

@pytest.mark.xfail:预置失败，由于没有开发完成的用例。这条用里写到一半，发现写不下去了
（写不下去的原因是因为功能没开发好）


#配置文件说明：
pytest的配置文件名字一定是要pytest.ini
文件的第一行内容一定是要[pytest]
markers:是用来注册标签的
addopts=add+options 翻译过来就是增加可选项，这个addopts是用来在运行的时候加载pytest的插件
testpaths:这个字段是用来写明测试文件夹的，路径写的是存放用例的文件夹
    testpaths=./demo  ../
    ./的意思就是以pytest.ini为基准，当前的testcase文件夹
    ../就是往上走两个层级
python_files:这个字段是用来修改pytest默认的执行文件.py
    python_files = test*.py
python_classes:这个字段是用来修改pytest默认的执行测试类
    python_classes = Test*
python_functions:这个字段是用来修改pytest默认的执行测试方法的
    python_functions=test*


xfail:预置失败，用于没有开发完成的用例。这条用例写到一半，发现写不下去了（测不下去的原因是因为功能没开发好）
    用到的方法是：pytest.xfail(reason='写原因的，原因一般是功能开发完')
    写在方法里面

unexpected passes：需用到的是@pytest.mark.xfail(reason='unexpected passes')


"""
import pytest


class TestCase_1():
    @pytest.mark.skip(reason = 'aaaaaaaaaaaaaaaa')
    def test_0(self):
        print(0000000000)
        assert 1>2

    @pytest.mark.skipif(3>2, reason="xxxxxxxxxxxx")
    def test_1(self):
        print(11111111111)
        # assert 1>2

    @pytest.mark.xfail(reason='测试一下这个装饰器')
    def test_2(self):
        print(22222222222)


    # def test_3(self):
    #     pytest.xfail(reason='写原因的，原因一般是功能开发完')
    #     print(3333333333)

    @pytest.mark.P0
    def test_4(self):
        print('冒烟用例1')

    @pytest.mark.P1
    def test_5(self):
        print('冒烟用例2')

    @pytest.mark.P1
    @pytest.mark.P0
    def test_6(self):
        print('冒烟用例3')


    @pytest.mark.run(order=1)
    def test_7(self):
        print('冒烟用例4')

    @pytest.mark.run(order=2)
    def test_8(self):
        print('冒烟用例5')

# def test_function_1():
#     print('function1')
#     assert 1==1


if __name__ == '__main__':
    pytest.main()




pyteststudy文件夹的层架关系以及对应文件夹和文件的作用：
1.report：是用来存放每次执行用例后生成测试报告的文件夹
2.testcase：是用来存放测试用例的地方
3.pytest.ini文件：是pytest框架的配置文件，用来存放testpaths，还有存放测试文件（py文件），还有
测试类，测试方法的匹配规则的，还有配置addopts参数的，pytest.ini文件的命名一定是pytest.ini，如果
文件的名字不是pytest.ini则不会去识别里面写的东西
4.requirement.txt是用来存放依赖库的，可以用过pip install -r requirement.txt这个命令安装所有的依赖库
5.run.py是整个测试框架执行代码的入口，只要在run.py里面去写一个main函数，就自动的执行testcase里面的
所有测试用例，并且生成测试报告
6.readme.md文件可以理解为是一个使用手册，说明书
7.conftest.py：是用来做为数据共享的文件来使用的，是pytest框架非常核心的文件，它的命名也一定是conftest.py

unittest和pytest的对比：
unittest：
    1.编写测试用例：unittest.TestCase，所以测试类都要进程这个TC的类
    2.命名的规范：方法名都是要以test开头，0-9，A-Z，a-z
    3.生成测试报告：用的是第三方的库HTMLTestRunner3的库，生成的是html的，beautiful report
    4.选择想要运行的用例：
        a:unittest.main()执行全部用例
        b:用TestSuite测试套件来把一条条的用例加载到套件里面再去执行，addTest ，addTests
        c：用的是TestLoader把测试类加载到suite里面再去执行
        d：用的是discover把不用的测试py文件去执行 ，匹配的规则自己写，*表示匹配所有
    5.参数化用的是第三方库的叫ddt的库，用来驱动的excel文件，xlrd，xlwt，openpyxl，yaml，json
    6.不支持失败重跑机制
    7.支持构造函数
    8.setup 和 teardown 来做前置和后置的处理，还有setupclass ，teartdownclass（需要用@classmethod）
pytest：
    1.测试用例可以是test开头，测试类是Test开头，测试文件是test*.py
    2.生成测试报告：用的是pytest-html --html=report/report.html ,
                    allure ：
                        a: pytest testcasePath --alluredir=resultPath
                        b：allure generate resultPath -o reportPath --clean
                            -o参数output，输出到某个文件
                            --clean清空之前的文件
                            Path既可以用相对路径（注意层级关系 ./  ../）,也可以用绝对路径
    3.选择想要的用例：可以给用例打上标签，可以给类去打标签也可以给方法去打上标签
    4.有fixture，夹具的使用，配置conftest.py ，还有pytest.ini去使用
    5.支持失败重跑机制，需要用到的是pytest-rerunfailures
    6.不支持构造方法，__init__
    7.参数化的用的是 @pytest.mark.parmastrize


面试：你的数据是如何解耦的？你的数据驱动是怎么做的？（ddt，json，yaml，excel）


token = '1234567'
token1 = 'token'








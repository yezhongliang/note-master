
"""
# pytest和unittest对比.py
"""

"""详细对比
1（是否第三方库）：unittest是python自带的单元测试框架，pytest是第三方库（需要用pip install pytest下载）
2（测试类和方法的命名）：unittest测试类必须要继承unittest.TestCase,用例名称必须以test开头；
pytest的用例文件必须以test开头，测试类必须以Test开头，测试方法必须以test开头
3（断言对比）：unittest使用的是assertEqual、assertNotEqual、assertIn、asserNotIn的unittest的断言方式；
pytest的断言使用的是python的自带的断言方法assert,assume,check
    assert:只能对一个内容进行断言，如果有三个断言的内容，在第一个就断言失败的话，第二个第三个就不会再去断言了，单重断言
    assume：可以对多个内容进行断言，如果有三个断言的内容，在第一个断言失败之后，第二个和第三个断言还是会继续去执行，不会停止，多重断言
    check：也是多重断言，但是check会在控制台详细输出报错的地方，便于测试人员去分析
4（生成测试报告对比）：unittest生成测试报告可以用到HTMLTestRunner模块或者BeautifulReport生成测试报告；
pytest生成测试报告用的pytest的插件pytest-html，或者allure的测试报告生成（依赖java环境，allure环境--配置环境变量）
5（数据驱动）：unittest使用的数据驱动的库为ddt库（第三方库，需要pip install ddt，ddt全程data driver test）；
pytest的数据驱动用的是@pytest.mark.parametrize装饰器来实现的。
6（前置和后置处理）：unittest的前置和后置有setup和teardown以及setupclass和teardownclass
pytest的前置和后置有setup和teardown（用法和unittest相同），但是pytest经常用fixture和yield来进行前置和后置处理，结合conftest
7（运行方式的不同）：unittest收集用例有多种方式（单条用例、单个类，多个类、单个py文件、多个py文件）；
pytest收集用例是根据pytest的配置文件，pytest.ini决定
8（是否支持失败重跑）：原生unittest不支持失败重跑（需要自己写方法），但是pytest支持失败重跑，这也是两个框架最大的特点。
9 （执行顺序对比）：unittest是按照TestSuite加载用例的顺序来控制的，pytest通过pytest-order插件可以控制用例执行的顺序 @pytest.mark.run(order=1) 1最大最先被执行
"""







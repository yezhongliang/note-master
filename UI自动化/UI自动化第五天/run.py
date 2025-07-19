import  unittest
from HTMLTestRunner3 import HTMLTestRunner

from python基础.各种包的学习.time模块 import file_name_utils
from zmail邮件发送测试报告.发送邮件带上附件 import send_mail_utils

if __name__ == '__main__':
    # test_path是装py文件用例的文件夹，翻译过来是测试路径
    test_path = r"D:\TestTool\project_for12\UI自动化\UI自动化第五天\2.用例执行的三种方式"
    discover = unittest.defaultTestLoader.discover(start_dir=test_path, pattern='testcase*.py')
    # discover = unittest.defaultTestLoader.discover(test_path, pattern='testcase1-没有测试报告生成.py')
    file_name = file_name_utils() + ' report.html'
    with open(file_name, mode='wb') as file:  # wb：二进制的覆盖写
        runner = HTMLTestRunner(stream=file,
                                verbosity=1,
                                title=None,
                                description=None)
        runner.run(discover)
    # 执行完用例之后，再去发送邮件
    send_mail_utils()

"""
"""

"""
@pytest.mark.parametrize(args_name,args_value)
args_name:参数名称
args_value：参数值
"""
import requests
import pytest
from 接口自动化.pytest的数据驱动_接口_yaml文件.read_yaml_utils import read_yaml


class Test_cms_login():
    # @pytest.mark.parametrize("args",read_yaml(r'D:\TestTool\project_for18\接口自动化\pytest的数据驱动_接口_yaml文件\data.yaml'))
    @pytest.mark.parametrize("args",read_yaml())
    def test_cms_login1(self,args):

        # print(args) #拿到的是data_yaml的所有内容，拿出来的是字典的数据类型
        # print(args['name'])
        # print(args['request'])
        # print(args['headers.yml'])
        res = requests.request(method=args['request']['method'],
                               url=args['request']['url'],
                                data=args['request']['data']
                               ).json()
        print(res)

if __name__ == '__main__':
    pytest.main()

#数据驱动也叫 数据解耦

#数据解耦怎么做的？
    # 数据解耦的意思：把复杂的，冗余的数据分开存放，存放在不同的文件里面
    # json文件、yaml文件、ini文件
    #     yaml对于接口自动化框架来说是用来存放用例的数据的！
    #     ini文件，作为配置文件来使用（数据库的配置信息，框架的配置信息，或者是
    #         也用于各种环境之间的切换）
    #     json文件：也是用来存储用例的数据的。
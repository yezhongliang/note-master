import pytest
import requests
from 接口自动化.pytest的数据驱动_接口_json文件.read_json import read_json_utils


class Test_cms_login():
    # headers = {"Content-Type":"application/x-www-form-urlencoded"}
    # @pytest.mark.parametrize("args",read_yaml(r'D:\TestTool\project_for18\接口自动化\pytest的数据驱动_接口_yaml文件\data.yaml'))
    @pytest.mark.parametrize("args",read_json_utils())
    def test_cms_login1(self,args):
        #装饰器需要传两个值，一个是变量名，随便命名，一个是拿到的数据，数据会传给
        #变量名，现在希望args这个数据类型是字典

        # print(args) #拿到的是data.json的所有内容，拿出来的是字典的数据类型
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



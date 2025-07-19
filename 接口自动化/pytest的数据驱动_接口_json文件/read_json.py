import json
def read_json_utils():
    with open(file=r'data.json',mode='r',encoding='utf-8') as file1:
        #把数据从json文件读取出来，用read方法即可
        str_data = file1.read()
        #把读取出来的str数据转换成为dict数据
        dict_data = json.loads(str_data)
        return dict_data



import yaml

def read_yaml(yaml_path=r'data.yaml'): #调用此方法的时候，需要传进去一个yaml文件的路径
    with open(yaml_path,encoding='utf‐8') as file:
        value = yaml.safe_load(file)
        return value


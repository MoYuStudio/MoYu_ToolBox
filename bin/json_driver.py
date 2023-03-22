
import json

def json文件读取(json文件路径):
    with open(json文件路径) as 文件:
        数据 = json.load(文件)
    return 数据

def json文件写入(json文件路径,写入数据):
    with open(json文件路径, 'w') as 文件:
        json.dump(写入数据, 文件)
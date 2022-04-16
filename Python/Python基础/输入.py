# coding=utf-8
"""
@Time : 2022/4/11 20:29
@File : 输入.PY 
@Author : Jack_yu（小懒猪） 
@Software : PyCharm
"""
"""
input输入
"""

def input_study():
    # input():用户输入字符串，并存放到变量中，返回类型为 字符串类型
    s = input()
    print(type(s))
    # input()可以让你显示一个字符串来提示用户
    s1 = input("输入字符串：")
    print(s1, "的数据类型：", type(s1))

"""
sys模块接收用户输入
strip():只能去除字符串首尾的字符，默认是空格、\n、\t
split():拆分字符串。通过指定分隔符对字符串进行切片，并返回分割后的字符串列表（list）,默认为空格分隔
"""
def sys_study():
    import sys
    a = sys.stdin.readline().strip().split()
    return a

"""
读写文件：
1.文件对象读取的方法
    调用 f.write() 时，未使用 with 关键字，或未调用 f.close()，即使程序正常退出，也**可能** 导致 f.write() 的参数没有完全写入磁盘。
    
2.使用 json 保存结构化数据
    JSON(JavaScript Object Notation) 是一种轻量级的数据交换格式，易于人阅读和编写。
    json.dumps	将 Python 对象编码成 JSON 字符串
    json.loads	将已编码的 JSON 字符串解码为 Python 对象
    简单的序列化技术可以处理列表和字典
"""
def file_json_study():
    import json
    x = [1,'simple','list']
    # json.dumps 用于将 Python 对象编码成 JSON 字符串。
    # 将数组编码为 JSON 格式数据：
    json_type_str = json.dumps(x)
    print(json_type_str)
    # 使用参数让 JSON 数据格式化输出：
    x1 = [{'a': 'Runoob', 'b': 7}]
    json_type_str1 = json.dumps(x1,sort_keys=True,indent=4,separators = (',',':'))
    print(json_type_str1)
    # json.loads 用于解码 JSON 数据。该函数返回 Python 字段的数据类型。
    data = json.loads(json_type_str1)
    print(data)
file_json_study()




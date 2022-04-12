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
print(sys_study())




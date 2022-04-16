# coding=utf-8
"""
@Time : 2022/4/11 20:30
@File : 数据类型.PY 
@Author : Jack_yu（小懒猪） 
@Software : PyCharm
"""
"""
六大基本类型：
    1.Numbers（数字）
    支持 int（整型）、float（浮点型）、bool（布尔型）、complex（复数）
    2.String（字符串）
    3.List（列表）
    4.Tuple（元组）
    5.Sets（集合）
    5.Dictionaries（字典）
判断数据类型的方法：
    1. type() ：不会认为子类是一种父类类型
    2. isinstance ：会认为子类是一种父类类型
"""
"""
1.Numbers（数字）
    支持 int（整型）、float（浮点型）、bool（布尔型）、complex（复数）
    数值运算：+ - * （加减乘）、/ （除，得到一个浮点数）、// （除，得到一个整数）、%（求余）、** （乘方）
    允许在数字中间以_分隔
"""
def number_study():
    a, b, c, d = 1, 1.5, True, 1+1j
    print(type(a), " : ", type(b), " : ", type(c), " : ", type(d))
    print(isinstance(a, int), " : ", isinstance(b, float), " : ", isinstance(c, bool), " : ", isinstance(d, complex))
    # 数值运算：+、-、*、/、//、%、**
    num1 = 2
    num2 = 3
    print(2 + 3, " : ", 2 - 3, " : ", 2 * 3, " : ", 2 / 3, " : ", 2 // 3, " : ", 2 % 3, " : ", 2 ** 3)
    # 允许在数字中间以_分隔
    print(1_000_91233)
    # 浮点数：把10用e替代，1.23x109就是1.23e9
    print(1.23e9)
    # 复数方式
    print(1+1j, " == ", complex(1, 1))


"""
String（字符串）
    字符串 str 用单引号(' ')或双引号 (" ") 括起来，同时使用反斜杠 (\) 转义特殊字符。
    字符串的截取的语法格式：变量[头下标:尾下标:步长]
    索引值以 0 为开始值，-1 为从末尾的开始位置。
    加号 + 是字符串的连接符， 星号 * 表示复制当前字符串，与之结合的数字为复制的次数
"""
def string_study():
    s1 = '小懒猪@'
    s2 = "小可爱"
    print(s1 + s2, " : ", 3 * s1)
    # 切片
    print(s1[:], "\n", s1[2:], " : ", s1[:3], "\n", s1[::2], " : ", s1[::-1], " : ", s1[-1:1:-2], " : ", s1[-1:-4:-2])
"""
字典（dictionary）是Python中另一个非常有用的内置数据类型。
    字典是另一种可变容器模型，且可存储任意类型对象。
    字典的每个键值 key=>value 对用冒号 : 分割，每个对之间用逗号(,)分割，整个字典包括在花括号 {} 中 ,格式如下所
    d = {key1 : value1, key2 : value2, key3 : value3 }
    添加元素：
        直接赋值： my_dict = dict({3,5}) 
        使用update方法：my_dict.update({1:3})
        通过key放入：my_dict[2]=4
"""
def dict_study():
    my_dict = dict({3,5})
    my_dict.update({1:3})
    my_dict.values()
    # 添加数据
    # 一个key只能对应一个value，所以，多次对一个key放入value，后面的值会把前面的值冲掉
    my_dict[2]=4
    print(my_dict[1])
    print(my_dict)
# number_study()
# string_study()
dict_study()
# coding=utf-8
"""
@Time : 2022/4/11 20:30
@File : 输出.PY 
@Author : Jack_yu（小懒猪） 
@Software : PyCharm
"""
"""
print():输出函数,会自动进行换行,可以通过 end = '' 修改结束的换行符
"""
def print_study():
    # 1、括号内加上字符串，就可以在屏幕上输出指定的内容
    print('hello world')
    # 2、可以接受多个字符串，用逗号隔开，就可以连成一句话。遇到逗号会输出一个空格。
    print('I am', 'woman!')
    # 3、可以打印整数，或者计算结果
    print(100)
    print(100 + 200)
"""
str.format() 函数来格式化字符串，通过 {} 和 : 来代替以前的 % 。
        1.可以接受不限个参数，位置可以不按顺序
        2.可以设置参数：
        3.向 str.format() 传入对象
        4.格式化数字
"""
def format_study():
    # format函数：格式化字符串
    # 1.可以接受不限个参数，位置可以不按顺序
    print("{} {}".format("hello", "world"))
    print("{0} {1}{0}".format("hello", "world"))
    # 2.可以设置参数：
    print("网站名：{name}，地址：{url}".format(name="小可爱", url="真可爱"))
    site = {"name":"小可爱", "url":"真可爱"}  # 通过字典设置参数
    print("网站名：{name}，地址：{url}".format(**site))
    my_list = ["小可爱", "真可爱"] # 通过列表设置参数
    print("网站名：{0[0]}, 地址：{0[1]}".format(my_list)) # "0" 是必须的

"""
sys 模块 输出
【sys.stdout.write(“xxx”)】：屏幕上打印 ---->print会调用sys.stdout的write方法
    注：sys.stdout.write(obj+'\n')中的obj只能是字符串。
write()方法，不会自动换行，需要手动加\n进行换行
print()方法，会自动进行换行,可以通过 end = '' 修改结束的换行符
将输出的值转成字符串，可以使用 repr() 或 str() 函数来实现。
    str() 函数返回一个用户易读的表达形式。
    repr() 产生一个解释器易读的表达形式
str.format() 函数来格式化字符串
"""
def sys_study():
    import sys
    s = 123
    s_str = str(s)+'\n'
    s_repr = repr(s)+'\n'
    sys.stdout.write(s_str)
    sys.stdout.write(s_repr)
    print('s的类型：', type(s))
    print('s_str的类型：', type(s_str))
    print('s_repr的类型：', type(s_repr))
    sys.stdout.write("123\n")
    print("123")
# sys_study()
# print_study()
format_study()
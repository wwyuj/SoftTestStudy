# coding=utf-8
"""
@Time : 2022/4/13 12:01
@File : 1. 两数之和.PY 
@Author : Jack_yu（小懒猪） 1. 两数之和.py
@Software : PyCharm
"""
from typing import List


class Solution:
    """
    方法一：暴力枚举
    """
    def twoSum(self, nums, target):
        n = len(nums)  # 获取数组长度
        # 第一层的循环i，表示依次获取第i个数值，等到内层的循环j，依次获取数组中所有的元素后，在获取第i+1个数，直到获取到最后一个数
        for i in range(n):
            # 第二层循环j，表示依次获取第i+1个数，用来和第一层循环i下标的值进行相加，看是否等于目标值。
            # 等于目标值，就返回本次循环的i，j值；否则接着循环，直到获取最后一个数
            for j in range(i + 1, n):
                if nums[i] + nums[j] == target:
                    return [i, j]


# 调用定义的函数
if __name__ == '__main__':
    # 实例化类
    x = Solution()
    """
    1、输入一行字符串，类似[2,3,4,5]；
        两种输入方法：input、sys模块
    2、使用lstrip、rstrip两个函数分别去除字符串中最左边的 [、最右边的 ] 字符
    3、使用split函数对字符串按 指定分隔符（逗号）进行分割，返回一个列表
    """
    # input：
    line = input().lstrip('[').rstrip(']\r\n').split(',')
    # sys 模块
    import sys
    # line_sys = sys.stdin.readline().lstrip('[').rstrip[']\r\n'].spilt(',')
    # map(f, iterA, iterB, ...) : 返回一个遍历序列的迭代器
    # 主要用于修改整个列表的数据类型
    nums = list(map(int, line))
    target = int(input())
    # 调用暴力破解的方法。
    print(x.twoSum(nums,target))
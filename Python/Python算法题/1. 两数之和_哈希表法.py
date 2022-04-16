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
给定一个整数数组 nums 和一个整数目标值 target，请你在该数组中找出 和为目标值 target  的那 两个 整数，并返回它们的数组下标。
你可以假设每种输入只会对应一个答案。但是，数组中同一个元素在答案里不能重复出现。
你可以按任意顺序返回答案。
输入：nums = [2,7,11,15], target = 9
输出：[0,1]
解释：因为 nums[0] + nums[1] == 9 ，返回 [0, 1] 。

提示：
        2 <= nums.length <= 104
        -109 <= nums[i] <= 109
        -109 <= target <= 109
        只会存在一个有效答案
    进阶：你可以想出一个时间复杂度小于 O(n2) 的算法吗？

    """
    """
    方法二：查找表法 -- 哈希表
    以空间换时间
    使用哈希表，能够将寻找 target - x 的时间复杂度从 O(N) 降低到 O(1)。
    创建一个哈希表，对于每一个x，首先查询哈希表中是否存在targer-x
    不存在，则将x存在哈希表中。
    存在，则返回对应两个元素的下标

    复杂度分析：
        时间复杂度：O(N),N为数组中的元素数量，对于每一个元素 x，我们可以 O(1)地寻找 target - x。。
        空间复杂度：O(N)，其中 N是数组中的元素数量。主要为哈希表的开销
    """
    # 形参标注的定义方式是在形参名后加冒号，后面跟一个表达式，该表达式会被求值为标注的值。
    # 返回值标注的定义方式是加组合符号 ->，后面跟一个表达式，该标注位于形参列表和表示 def 语句结束的冒号之间。
    def twoSum(self,nums:List[int],target:int):
        # 定义一个字典，用来存放每一个不存在的元素。
        hashtable = dict()
        # 在字典中循环时，用 items() 方法可同时取出键和对应的值：
        # 在序列中循环时，用 enumerate() 函数可以同时取出位置索引和对应的值
        for i,x in enumerate(nums):     # i,x 分别表示序列中的下标和对应的值。
            # 判断 target-x 是否存在 哈希表 中
            if target-x in hashtable:
                # target-x 表示字典的key，hashtable[target-x] 获取该key对应的值，就是下标
                return [hashtable[target-x],i]
            # 不存在，则x 当作key，i当作value存入字典中
            hashtable[nums[i]] = i

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
    #调用哈希表的方法
    res_hash = x.twoSums_Hash(nums, target)
    print(res_hash)
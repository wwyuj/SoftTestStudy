# coding=utf-8
"""
@Time : 2022/4/14 14:47
@File : 26. 删除有序数组中的重复项.PY 
@Author : Jack_yu（小懒猪） 
@Software : PyCharm
"""
from typing import List
class Solution:
    def removeDuplicates(self, nums: List[int]) -> int:
        """
        解题思路：
        使用两个指针遍历整个数组。
        1、开始两个指针同时指向第一个数字。
        2、如果两个数字相同，则快指针向前走一步。
        3、如果两个数字不相同，则两个指针都向前走一步，并且当前慢指针所在数字+1 修改为当前快指针所在数字。
        4、当快指针遍历完整个数组后，慢指针所在位置加1就是数组中不同的数字个数。
        :param nums:
        :return: 慢指针所在位置加1
        """
        # 获取nums的长度
        n = len(nums)
        # 定义两个指针的初始位置
        left = 0 # 慢指针所在位置
        right = 0 # 快指针所在位置
        # 循环遍历整个数组，通过两个指针指向位置元素是否相等，判断快指针加1还是两个指针同时加1，直到快指针遍历完数组
        while right < n:
            if nums[left] == nums[right]:  # 相等
                right += 1
            else:  # 不相等
                left += 1
                nums[left] = nums[right]  # 当前慢指针所在位置+1数字修改为当前快指针所在数字
                right += 1
        return left + 1
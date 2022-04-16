# coding=utf-8
"""
@Time : 2022/4/15 14:49
@File : 27.移除元素_双指针.PY 
@Author : Jack_yu（小懒猪） 
@Software : PyCharm
"""
from typing import List
class Solution:
    def removeElement(self, nums: List[int], val: int) -> int:
        """
        解题思路：双指针（快慢指针）
        1、定义两个指针为开始位置。
        2、快指针一直向后遍历。判断快指针是否等于VAL值
        3、快指针等于val值，则快指针向后移动一位，慢指针不变。
        4、快指针不等于val值，则当前快指针的值赋给当前慢指针的值，快慢指针位置同时加1
        5、直到快指针遍历完整个数组
        6、最终返回 慢指针所在位置
        :param nums:
        :param val:
        :return:慢指针所在位置
        """
        # 获取nums数组的长度
        n = nums.__len__()
        # 定义快慢指针为开始位置
        left = 0    #慢指针
        right = 0   # 快指针
        # 遍历循环：快指针不等于val时，当前位置的快指针赋值给慢指针，慢指针才向后移动一位，快指针每次循环都会移动一位
        while right < n:
            # 判断 nums[right] 是否等于 val
            if nums[right] != val:  # 不等于，则当前快指针赋值给慢指针，并且慢指针加1
                nums[left] = nums[right]
                left += 1
            # 快指针一直向后遍历
            right += 1
        return left
if __name__ == '__main__':
    x = Solution()
    nums = [0,1,2,2,3,0,4,2]
    print(type(nums))
    val = 2
    len = x.removeElement(nums,val)
    print(len)
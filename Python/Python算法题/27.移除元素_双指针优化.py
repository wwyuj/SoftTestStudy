# coding=utf-8
"""
@Time : 2022/4/15 14:49
@File : 27.移除元素_双指针优化.PY
@Author : Jack_yu（小懒猪）
@Software : PyCharm
"""
from typing import List
class Solution:
    def removeElement(self, nums: List[int], val: int) -> int:
        """
        解题思路：双指针（使用左右两端的双指针进行处理）
        1、定义左右两端指针。开始 左指针为0，右指针为数组长度减一
        2、循环遍历：判断左指针是否等于val，
        3、等于则把当前右指针的数值赋值给当前左指针，并且右指针左移动一位；
        4、左指针不相等，则左指针向后移动一位；
        5、直到左右指针重合的时候就是遍历完整个数组
        6、最后返回left的值，就是删除后的数组长度
        :param nums:
        :param val:
        :return:最后返回left的值
        """
        # 获取nums数组长度
        n = len(nums)
        # 定义左右两端指针
        left = 0
        right = n-1
        # 循环遍历比较，直到左右指针重合的时候就是遍历完整个数组
        while left <= right:
            # 判断左指针是否等于val
            if nums[left] == val:
                nums[left] = nums[right]
                right -= 1
            else:
                left += 1
        return left
if __name__ == '__main__':
    x = Solution()
    nums = [0,1,2,2,3,0,4,2]
    print(type(nums))
    val = 2
    len = x.removeElement(nums,val)
    print(len)
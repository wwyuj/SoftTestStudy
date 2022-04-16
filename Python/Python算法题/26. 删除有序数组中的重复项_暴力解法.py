# coding=utf-8
"""
@Time : 2022/4/14 14:47
@File : 26. 删除有序数组中的重复项.PY 
@Author : Jack_yu（小懒猪） 
@Software : PyCharm
"""
from typing import List
class Solution:
    def removeDuplicates(self, nums:List[int]) -> int:
        """
        :param nums:
        :return: len ， nums
        """
        # 获取原数组的长度
        n = len(nums)
        # 判断数组长度是否等于0
        if n == 0:
            return 0
        # 定义初始下标为0
        i = 0
        # 定义一个循环
        while i < n-1:
            # 如果第i个和i+1个位置相等，则移除i+1个元素
            if nums[i] == nums[i+1]:
                nums.remove(nums[i])
                n = n-1
            else:
                i +=1
        new_len = len(nums)
        return new_len
if __name__ == '__main__':
    try:

        """
        int[] nums = [...]; // 输入数组
        int[] expectedNums = [...]; // 长度正确的期望答案
        int k = removeDuplicates(nums); // 调用
        assert k == expectedNums.length;
        for (int i = 0; i < k; i++) {
            assert nums[i] == expectedNums[i];
        }
        """
        import re
        x = Solution()
        #  输入数组
        list_nums = input().replace('[','').replace(']','').split(',')
        nums = list(map(int, list_nums))
        # expectedNums = [...]; // 长度正确的期望答案
        expectedNums = list(set(nums))
        # k = removeDuplicates(nums); // 调用,获取长度
        k = x.removeDuplicates(nums)  # 元祖类型
        # 校验长度和期望是否一致
        assert k == expectedNums.__len__()
        # 校验 内容是否一致
        for i in range(k):
            assert nums[i] == expectedNums[i];
        # 打印最后的数组
        # 用例：[0,0,1,1,1,2,2,3,3,4]
        print(expectedNums)
    except AssertionError as aeeor:
        breakpoint()
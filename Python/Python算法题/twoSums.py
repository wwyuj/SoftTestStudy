import json
from  typing import List
class Solution:
    # 暴力破解
    def twoSum(self, nums:  List[int], target: int) ->  List[int]:
        n = len(nums)  # 获取数组长度
        for i in range(n):
            for j in range(i + 1, n):
                if nums[i] + nums[j] == target:
                    return [i, j]



def stringToIntegerList(input):
    return json.loads(input)


def integerListToString(nums, len_of_list=None):
    if not len_of_list:
        len_of_list = len(nums)
    return json.dumps(nums[:len_of_list])


def main():
    import sys
    import io
    def readlines():
        for line in io.TextIOWrapper(sys.stdin.buffer, encoding='utf-8'):
            # 换行终止该行输入（改行字符串属于一个单独的lines）
            # 使用了 yield 的函数被称为生成器，
            # 在调用生成器运行的过程中，每次遇到 yield 时函数会暂停并保存当前所有的运行信息，
            # 返回 yield 的值, 并在下一次执行 next() 方法时从当前位置继续运行
            yield line.strip('\n')

    lines = readlines()
    while True:
        try:
            # 开启一行的输入
            line = next(lines)
            nums = stringToIntegerList(line)
            # 开启新的一行的输入
            line = next(lines)
            target = int(line)

            ret = Solution().twoSum(nums, target)

            out = integerListToString(ret)
            print(out)
        except StopIteration:
            break


if __name__ == '__main__':
    main()
    # [2,7,11,15] 9 [3,2,4] 6 [3,3] 6
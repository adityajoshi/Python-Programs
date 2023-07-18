class Solution(object):
    def twoSum(self, nums, target):
        prev_map = {}

        for i, n in enumerate(nums):
            diff = target - n
            if diff in prev_map:
                return [prev_map[diff], i]
            prev_map[n] = i
        return


if __name__ == "__main__":
    c: Solution = Solution()
    nums = [2, 7, 10, 15]
    target = 9
    output = c.twoSum(nums, target=target)
    print(output)

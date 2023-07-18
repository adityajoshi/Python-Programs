class Solution(object):
    def containsDuplicate(self, nums):
        """
        :type nums: List[int]
        :rtype: bool
        """
        # hashset = set()
        #
        # for num in nums:
        #     if num in hashset:
        #         return True
        #     hashset.add(num)
        # return False
        return len(set(nums)) != len(nums)


if __name__ == "__main__":
    c: Solution = Solution()
    nums = [2, 2, 10, 15]
    # target = 9
    output = c.containsDuplicate(nums)
    print(output)

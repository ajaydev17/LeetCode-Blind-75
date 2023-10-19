class Solution(object):
    @staticmethod
    def two_sum(nums, target):
        """
        :type nums: List[int]
        :type target: int
        :rtype: List[int]
        """
        num_index = {}

        for index, num in enumerate(nums):
            difference = target - num

            if difference in num_index:
                return [num_index[difference], index]
            num_index[num] = index

        return []

class Solution(object):
    @staticmethod
    def max_subarray(array):
        cur_sum = 0
        max_sum = array[0]

        for element in array:
            if cur_sum < 0:
                cur_sum = 0
            cur_sum = cur_sum + element
            max_sum = max(max_sum, cur_sum)
        return max_sum


print(Solution.max_subarray([-2, 1, -3, 4, -1, 2, 1, -5, 4]))
print(Solution.max_subarray([5, 4, -1, 7, 8]))

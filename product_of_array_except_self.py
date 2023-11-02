class Solution(object):
    @staticmethod
    def product_of_array(array):
        prefix = 1
        result = [1] * len(array)

        # find the product of the array before that element prefix
        for i in range(len(array)):
            result[i] = result[i] * prefix
            prefix = prefix * array[i]

        postfix = 1

        # find the product of the array before that element postfix
        for i in range(len(array) - 1, -1, -1):
            result[i] = result[i] * postfix
            postfix = postfix * array[i]

        return result


result = Solution.product_of_array([1, 2, 3, 4])
print(result)

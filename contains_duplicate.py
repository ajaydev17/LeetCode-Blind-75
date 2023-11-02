class Solution(object):
    @staticmethod
    def contains_duplicate(array):
        hash_set = set()

        for element in array:
            if element in hash_set:
                return True
            hash_set.add(element)
        return False

        # solution with checking len
        # return len(set(array)) != len(array)

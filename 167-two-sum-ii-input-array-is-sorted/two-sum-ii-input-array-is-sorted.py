class Solution(object):
    def twoSum(self, numbers, target):
        """
        :type numbers: List[int]
        :type target: int
        :rtype: List[int]
        """
        hash_map = {}

        for i,num in enumerate(numbers):
            comp = target - num
            if comp in hash_map :
                return [(hash_map[comp]+1), i+1]
            hash_map[num] = i
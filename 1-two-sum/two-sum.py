class Solution(object):
    def twoSum(self, nums, target):
        """
        :type nums: List[int]
        :type target: int
        :rtype: List[int]
        """
        hash_map = {}

        for i,num in enumerate(nums) :
            comp = target - num
            if comp in hash_map :
                return [hash_map[comp],i]

            hash_map[num] = i

        return []
    
        
        
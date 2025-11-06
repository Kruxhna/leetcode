class Solution(object):
    def findMaxConsecutiveOnes(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        count,max_c = 0,0

        for num in nums :
            if num == 1 :
                count += 1
                max_c = max(count,max_c)
            else :
                count = 0

        return max_c
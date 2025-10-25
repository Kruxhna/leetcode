class Solution(object):
    def productExceptSelf(self, nums):
        """
        :type nums: List[int]
        :rtype: List[int]
        """
        n = len(nums)
        ans = [1]*n

        prefix_product = 1

        for i in range(n) :
            ans[i] = prefix_product
            prefix_product *= nums[i]

        suffix_product = 1
        for i in range(n-1,-1,-1):
            ans[i] *= suffix_product
            suffix_product *= nums[i]

        return ans
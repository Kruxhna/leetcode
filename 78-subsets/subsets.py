class Solution:
    def subsets(self, nums: List[int]) -> List[List[int]]:
        nums.sort()
        res= []
        n = len(nums)

        for i in range(1<<n) :
            subset = []
            for j in range(n) :
                if (i&(1 << j)) != 0 :
                    subset.append(nums[j])

            res.append(subset)
        return res
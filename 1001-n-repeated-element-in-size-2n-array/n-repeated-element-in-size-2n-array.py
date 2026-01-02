class Solution:
    def repeatedNTimes(self, nums: List[int]) -> int:
        n = len(nums)

        for dis in range(1,4) :
            for i in range(n-dis) :
                if nums[i] == nums[i+dis] :
                    return nums[i]

        return -1
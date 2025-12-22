class Solution:
    def canJump(self, nums: List[int]) -> bool:
        lg_pos = len(nums)-1

        for i in range(len(nums)-2,-1,-1) :
            if i + nums[i] >= lg_pos :
                lg_pos = i

        return lg_pos == 0
class Solution:
    def solve(self,nums,res,idx) :
        if idx == len(nums) :
            res.append(nums[:])
            return
        for i in range(idx,len(nums)) :
            nums[idx], nums[i] = nums[i], nums[idx]

            self.solve(nums,res,idx+1)

            nums[idx], nums[i] = nums[i], nums[idx]
 

    def permute(self, nums: List[int]) -> List[List[int]]:
        res = []
        self.solve(nums,res,0) 
        return res
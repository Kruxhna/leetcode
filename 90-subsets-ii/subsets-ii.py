class Solution:
    def solve(self,nums,idx,subset,res) :
        res.append(subset[:])

        for i in range(idx,len(nums)) :
            if i > idx and nums[i] == nums[i-1] :
                continue
            subset.append(nums[i])
            self.solve(nums,i+1,subset,res)
            subset.pop()

    def subsetsWithDup(self, nums: List[int]) -> List[List[int]]:
        nums.sort()
        res = []
        self.solve(nums,0,[],res)
        return res
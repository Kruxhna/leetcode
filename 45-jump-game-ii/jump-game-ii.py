class Solution:
    def jump(self, nums: List[int]) -> int:
        n = len(nums)
        if n <= 1 :
            return 0

        jump,f,curr_end = 0,0,0

        for i in range(n-1):
            f = max(f,i+nums[i])

            if i == curr_end :
                jump += 1
                curr_end = f

                if curr_end >= n-1 :
                    break
        return jump
class Solution:
    def findErrorNums(self, nums: List[int]) -> List[int]:
        n = len(nums)

        ex_sum = n*(n+1)//2
        ex_sum_sq = n*(n+1)*(2*n+1)//6

        act_sum = sum(nums)
        act_sum_sq = sum(x*x for x in nums)

        diff_sum = ex_sum - act_sum
        diff_sum_sq = ex_sum_sq - act_sum_sq

        sum_xy = diff_sum_sq//diff_sum

        dulpicate = (sum_xy - diff_sum)//2
        missing = (sum_xy + diff_sum)//2

        return [dulpicate,missing]
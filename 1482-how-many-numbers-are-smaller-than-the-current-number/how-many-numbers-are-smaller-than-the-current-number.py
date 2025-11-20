class Solution:
    def smallerNumbersThanCurrent(self, nums: List[int]) -> List[int]:
        sorted_num = sorted(nums)
        dic = {}

        for i, num in enumerate(sorted_num) :
            if num not in dic :
                dic[num] = i
        return [dic[n] for n in nums]
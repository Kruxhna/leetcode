class Solution(object):
    def threeSum(self, nums):
        """
        :type nums: List[int]
        :rtype: List[List[int]]
        """
        sort_arr = sorted(nums)
        result = []

        for i in range(len(sort_arr)) :
            if sort_arr[i] > 0 :
                break
            if i > 0 and sort_arr[i] == sort_arr[i-1] :
                continue

            left, right = i+1,len(sort_arr)-1

            while left < right:
                curr_sum = sort_arr[i]+sort_arr[left]+sort_arr[right]

                if curr_sum > 0 :
                    right -= 1
                elif curr_sum < 0 :
                    left += 1
                else :
                    result.append([sort_arr[i],sort_arr[left],sort_arr[right]])
                    left += 1
                    right -= 1
                    while left < right and sort_arr[left] == sort_arr[left-1] :
                        left += 1

        return result
        
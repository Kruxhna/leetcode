class Solution(object):
    def search(self, nums, target):
        if not nums :
            return -1

        n = len(nums)
        l,r = 0,n-1

        while l <= r :
            mid = l + (r-l)//2

            if nums[mid] == target :
                return mid
            elif nums[mid] > target :
                r = mid-1
            else :
                l = mid+1
        return -1
        
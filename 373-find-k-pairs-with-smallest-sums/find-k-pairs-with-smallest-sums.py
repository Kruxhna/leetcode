import heapq
class Solution:
    def kSmallestPairs(self, nums1: List[int], nums2: List[int], k: int) -> List[List[int]]:
        result = []

        if not nums1 or not nums2 or k == 0 :
            return result

        min_heap = []

        for i in range(min(len(nums1),k)) :
            heapq.heappush(min_heap,(nums1[i]+nums2[0],i,0))

        while k > 0 and min_heap :
            curr_sum,i,j = heapq.heappop(min_heap)
            result.append([nums1[i],nums2[j]])

            if j+1 < len(nums2) :
                heapq.heappush(min_heap,(nums1[i]+nums2[j+1],i,j+1))
            k-=1 
        return result
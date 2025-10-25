class Solution(object):
    def topKFrequent(self, nums, k):
        """
        :type nums: List[int]
        :type k: int
        :rtype: List[int]
        """
        from collections import defaultdict

        freq = defaultdict(int)

        for num in nums :
            freq[num] += 1

        sorted_freq = sorted(freq.items(), key= lambda x: x[1], reverse= True )

        top_k = [element[0] for element in sorted_freq[:k]]

        return top_k

        
        
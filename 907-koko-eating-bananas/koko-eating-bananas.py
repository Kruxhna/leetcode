class Solution(object):
    def minEatingSpeed(self, piles, h):
        low = 1
        high = max(piles)
        min_k = high

        while low <= high :
            k = low + (high-low)//2

            hour_needed = 0
            for pile in piles :

                hour_needed += (pile + k - 1) // k 

            if hour_needed <= h :
                min_k = k
                high= k-1
            else :
                low = k+1

        return min_k
        
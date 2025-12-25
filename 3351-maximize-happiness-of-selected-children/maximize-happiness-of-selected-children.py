class Solution:
    def maximumHappinessSum(self, happiness: List[int], k: int) -> int:
        happiness.sort(reverse=True)
        total = 0 

        for i in range(k) :
            curr = max(0,happiness[i]-i)

            if curr > 0 :
                total += curr
            else :
                break
        return total
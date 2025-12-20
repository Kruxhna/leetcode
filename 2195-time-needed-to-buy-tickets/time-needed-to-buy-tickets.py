class Solution:
    def timeRequiredToBuy(self, tickets: List[int], k: int) -> int:
        time, tar = 0,tickets[k]

        for i in range(len(tickets)) :
            if i <= k :
                time += min(tickets[i],tar)
            else :
                time += min(tickets[i],tar-1)

        return time
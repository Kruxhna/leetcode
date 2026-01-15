class Solution:
    def maximizeSquareHoleArea(self, n: int, m: int, hBars: List[int], vBars: List[int]) -> int:
        hBars.sort()
        vBars.sort()
        
        def consective(bars) :
            max_conse = 1
            curr_conse = 1

            for i in range(1,len(bars)) :
                if bars[i] == bars[i-1] + 1 :
                    curr_conse += 1
                else :
                    curr_conse = 1

                max_conse = max(max_conse,curr_conse)

            return max_conse

        max_h = consective(hBars)
        max_v = consective(vBars)

        side = min(max_h,max_v) + 1
        return side*side
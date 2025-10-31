class Solution:
    def largestRectangleArea(self, heights: List[int]) -> int:
        n,max_area = len(heights), 0
        stack = []
        
        for i in range(n+1) :
            curr_h = 0 if i == n else heights[i]

            while stack and curr_h < heights[stack[-1]] :
                idx = stack.pop()
                h = heights[idx]

                if not stack :
                    left_boundary = -1
                else :
                    left_boundary = stack[-1]
                
                w = i - left_boundary - 1
                max_area = max(max_area,h*w)
            
            stack.append(i)
        return max_area
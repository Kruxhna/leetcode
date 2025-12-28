class Solution:
    def countNegatives(self, grid: List[List[int]]) -> int:
        n,m = len(grid),len(grid[0])
        c = 0
        row,col = 0,m-1

        while row < n and col >= 0 :
            if grid[row][col] < 0 :
                c += (n-row)
                col -= 1
            else :
                row += 1
        return c
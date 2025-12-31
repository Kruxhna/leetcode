class DSU :
    def __init__(self,n) :
        self.parent = list(range(n))

    def find(self,i) :
        if self.parent[i] == i :
            return i 
        self.parent[i] = self.find(self.parent[i])
        return self.parent[i]

    def union(self,i,j) :
        root_i = self.find(i)
        root_j = self.find(j)
        if root_i != root_j :
            self.parent[root_i] = root_j
            return True
        return False




class Solution:
    def latestDayToCross(self, row: int, col: int, cells: List[List[int]]) -> int:
        n = row*col
        dsu = DSU(n+2)
        v_top,v_bottom = n, n+1

        grid = [[0]*col for _ in range(row)]

        direction = [(0,1),(0,-1),(1,0),(-1,0)]

        for i in range(len(cells)-1,-1,-1) :
            r,c = cells[i][0] - 1 , cells[i][1] - 1
            grid[r][c] = 1
            curr_idx = r*col + c

            if r == 0 :
                dsu.union(curr_idx,v_top)
            if r == row-1 :
                dsu.union(curr_idx,v_bottom)

            for dr,dc in direction :
                nr,nc = r + dr , c + dc

                if 0 <= nr < row and 0 <= nc < col and grid[nr][nc] == 1 :
                    dsu.union(curr_idx,nr*col+nc)

            if dsu.find(v_top) == dsu.find(v_bottom) :
                return i
        return 0
 
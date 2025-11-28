class Solution:

    def check(self,board,word,x,y,widx) :
        wlen = len(word)
        n = len(board)
        m = len(board[0])

        if wlen == widx :
            return True
        if x < 0 or y < 0 or x >= n or y >= m :
            return False

        if board[x][y] == word[widx] :
            temp = board[x][y]
            board[x][y] = '#'

            res = (self.check(board,word,x-1,y,widx+1)
                    or self.check(board,word,x+1,y,widx+1)
                    or self.check(board,word,x,y-1,widx+1)
                    or self.check(board,word,x,y+1,widx+1))
            
            board[x][y] = temp
            return res
        return False
            


    def exist(self, board: List[List[str]], word: str) -> bool:
        wlen = len(word)
        n = len(board)
        m = len(board[0])

        if wlen > n*m :
            return False
        
        for i in range(n) :
            for j in range(m) :
                if board[i][j] == word[0] :
                    if self.check(board,word,i,j,0) :
                        return True
        return False
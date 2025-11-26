class Solution:
    def solveNQueens(self, n: int) -> list[list[str]]:
        """
        Solves the N-Queens problem using backtracking with sets for constraint checking.
        """
        # Sets to keep track of restricted zones
        cols = set()
        pos_diag = set() # (r + c)
        neg_diag = set() # (r - c)
        
        res = []
        
        # Initialize the board with empty cells "."
        board = [["."] * n for _ in range(n)]

        def backtrack(r):
            # Base Case: If we've placed queens in all N rows (0 to n-1)
            if r == n:
                # Convert the board list-of-lists into the required string format
                copy = ["".join(row) for row in board]
                res.append(copy)
                return

            # Try placing a queen in every column 'c' for the current row 'r'
            for c in range(n):
                # Check constraints:
                # 1. Is column occupied?
                # 2. Is positive diagonal (r + c) occupied?
                # 3. Is negative diagonal (r - c) occupied?
                if c in cols or (r + c) in pos_diag or (r - c) in neg_diag:
                    continue

                # --- DO (Place Queen) ---
                cols.add(c)
                pos_diag.add(r + c)
                neg_diag.add(r - c)
                board[r][c] = "Q"

                # --- RECURSE (Move to next row) ---
                backtrack(r + 1)

                # --- UNDO (Backtrack / Remove Queen) ---
                cols.remove(c)
                pos_diag.remove(r + c)
                neg_diag.remove(r - c)
                board[r][c] = "."

        # Start the recursion from row 0
        backtrack(0)
        return res
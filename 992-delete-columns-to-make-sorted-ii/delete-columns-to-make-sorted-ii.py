class Solution:
    def minDeletionSize(self, strs: List[str]) -> int:
        n,m,delete = len(strs),len(strs[0]), 0
        is_sorted = [False]*(n-1)
        sorted_count = 0

        for j in range(m) :
            n_del = False

            for i in range(n-1) :
                if not is_sorted[i] and strs[i][j] > strs[i+1][j] :
                    delete += 1
                    n_del = True
                    break
            if n_del :
                continue

            for i in range(n-1) :
                if not is_sorted[i] and strs[i][j] < strs[i+1][j] :
                    is_sorted[i] = True
                    sorted_count += 1

            if sorted_count == n-1 :
                return delete
        return delete
class Solution:
    def solve(self,arr,cur,res,idx,target) :
        if target == 0 :
            res.append(list(cur))
            return
        if  target < 0 or idx > len(arr) :
            return
        for i in range(idx,len(arr)) :
            if i > idx and arr[i] == arr[i-1] :
                continue
            cur.append(arr[i])
            self.solve(arr,cur,res,i+1,target-arr[i])
            cur.pop()

    def combinationSum2(self, candidates: List[int], target: int) -> List[List[int]]:
        candidates.sort()
        cur = []
        res = []
        self.solve(candidates,cur,res,0,target)
        return res
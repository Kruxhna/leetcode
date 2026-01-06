from collections import deque
# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:
    def maxLevelSum(self, root: Optional[TreeNode]) -> int:
        if not root :
            return 0

        queue = deque([root])

        max_sum,res_l,curr_l = float('-inf'),0,1

        while queue :
            level_size = len(queue)
            curr_sum = 0 

            for _ in range(level_size) :
                node = queue.popleft()
                curr_sum += node.val

                if node.left :
                    queue.append(node.left)
                if node.right :
                    queue.append(node.right)

            if curr_sum > max_sum :
                max_sum = curr_sum
                res_l = curr_l

            curr_l += 1
        return res_l
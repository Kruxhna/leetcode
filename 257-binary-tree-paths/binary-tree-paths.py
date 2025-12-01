# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def binaryTreePaths(self, root: Optional[TreeNode]) -> List[str]:
        path = []

        if not root :
            return path

        def dfs(node, curr_path) :
            curr_path += str(node.val)

            if not node.left and not node.right :
                path.append(curr_path)

            if node.left :
                dfs(node.left,curr_path + "->")
            if node.right :
                dfs(node.right,curr_path + "->")

        dfs(root,"")

        return path
# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
#My solution, ideal solution
#O(n) time, O(n) space
class Solution:
    def maxDepth(self, root: Optional[TreeNode]) -> int:
        #Strategy: Simple DFS, the max depth of a certain node is 1 + the max depth of its two subtrees that exist below it
        #Nature of DFS, we will eventually reach an empty node. This will be our base case, and we will return 0, which is the depth of an empty node
        #As, we work up, incrementing by one each time, we will eventually arrive at the maximum depth at the root node
        if not root:
            return 0
        return 1 + max(self.maxDepth(root.left), self.maxDepth(root.right))

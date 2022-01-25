# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
#My solution, ideal solution
#O(1) space, O(min(M, N)) time
class Solution:
    def isSameTree(self, p: Optional[TreeNode], q: Optional[TreeNode]) -> bool:
        
        #Strategy: Recursive solution, check each node individually through a DFS. If one exists and one does not, return False. If they both don't exist, return True. Else, they both exist, and we check the vals. If they have the same val, we continue to recursively go through the tree and verify they are identical
        if q and not p or p and not q:
            return False
        elif not p and not q:
            return True
        elif p.val != q.val:
            return False
        else:    
            return self.isSameTree(p.left, q.left) and self.isSameTree(p.right, q.right)

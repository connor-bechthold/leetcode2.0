# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
#My solution, ideal solution
#O(n) time, O(n) space
class Solution:
    def minDepth(self, root: Optional[TreeNode]) -> int:
        
        #Strategy: Since we want to find the mind depth, BFS makes more sense here. Simply traverse each level of the tree, keeping track of the depth we're at. As soon as we hit a leaf node, we can return the current depth, which will be the min depth
        if not root:
            return 0
        q = deque()
        min_depth = 0
        q.append(root)
        
        while q:
            min_depth += 1
            length = len(q)
            
            for i in range(0, length):
                curr = q.popleft()
                if not curr.left and not curr.right:
                    return min_depth
                if curr.left:
                    q.append(curr.left)
                if curr.right:
                    q.append(curr.right)

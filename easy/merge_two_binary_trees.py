# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
#My solution, ideal solution
# Time O(m + n), where m is the # of overlappimg nodes and n is the # of non overlapping nodes
# Space O(max(h1, h2))
class Solution:
    def mergeTrees(self, root1: Optional[TreeNode], root2: Optional[TreeNode]) -> Optional[TreeNode]:
        
        #Strategy: Contruct a new tree by performing a DFS of both trees along the way
        #If we are passed in two empty trees, we can immediately return None, as our base case
        #Else, we assign the new node to the value of either root1, root2, or the sum
        #We update the left and right subtrees of the new node with the left and right subtrees of root1 and root2. If one of these subtrees does not exist, we can pass None
        #We return the new root at the end
        if not root1 and not root2:
            return None
        new = TreeNode()
        if root1 and root2:
            new.val = root1.val + root2.val
            new.left = self.mergeTrees(root1.left, root2.left)
            new.right = self.mergeTrees(root1.right, root2.right)
        elif root1:
            new.val = root1.val
            new.left = self.mergeTrees(root1.left, None)
            new.right = self.mergeTrees(root1.right, None)
        else:
            new.val = root2.val
            new.left = self.mergeTrees(None, root2.left)
            new.right = self.mergeTrees(None, root2.right)
            
        return new  
    
#Same Solution, more concise
class Solution:
    def mergeTrees(self, root1: Optional[TreeNode], root2: Optional[TreeNode]) -> Optional[TreeNode]:
        if not root1 and not root2:
            return None
        new = TreeNode((root1.val if root1 else 0) + (root2.val if root2 else 0))
        new.left = self.mergeTrees(root1 and root1.left, root2 and root2.left)
        new.right = self.mergeTrees(root1 and root1.right, root2 and root2.right)
        
        return new

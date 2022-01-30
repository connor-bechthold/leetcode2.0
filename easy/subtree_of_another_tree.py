# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
#Let m be # of nodes in root tree, n in subRoot tree
#isSameTree has worst case time complexity O(n)
#isSubtree worst case we will have to traverse all n nodes and check isSameTree
#Thus, time complexity is O(n*m)
class Solution:
    def isSubtree(self, root: Optional[TreeNode], subRoot: Optional[TreeNode]) -> bool:
        #Strategy: Traverse through the tree (preorder) and if a node exists, we confirm that the subtree and the tree defined at that node are the same
        #If it is, we can immediately return True, else, we continue to traverse through the tree
        if not root:
            return False
        if self.isSameTree(root, subRoot):
            return True
        return self.isSubtree(root.left, subRoot) or self.isSubtree(root.right, subRoot)
    
    
    def isSameTree(self, one, two):
            if not one and not two:
                return True
            if not one and two or one and not two:
                return False
            if one.val != two.val:
                return False
            return self.isSameTree(one.left, two.left) and self.isSameTree(one.right, two.right)

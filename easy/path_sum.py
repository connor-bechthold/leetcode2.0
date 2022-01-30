# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

#My solution, ideal solution
#O(n) time, O(h) space
class Solution:
    def hasPathSum(self, root: Optional[TreeNode], targetSum: int) -> bool:
        return self.hasPathRec(root, 0, targetSum)
    
    def hasPathRec(self, node: Optional[TreeNode], currSum: int, targetSum: int) -> bool:
        #Strategy: Recursive DFS approach. If there's no node, we can immediately return False, as it does not add to the path
        #Since we pass in the current sum and the target sum at each step, we also check to see if the current node matches the target sum. NOTE that we check the val for equality and also check if the node is a leaf node, by the question description
        #Else, we continue our DFS down the left and right subtrees. We use OR here, as the path could come from either tree
        #As soon as one path returns True, we can immediately return True
        if not node:
            return False
        if currSum + node.val == targetSum and not node.left and not node.right:
            return True
        return self.hasPathRec(node.left, currSum + node.val, targetSum) or self.hasPathRec(node.right, currSum + node.val, targetSum)

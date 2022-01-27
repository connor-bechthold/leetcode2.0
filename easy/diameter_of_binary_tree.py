# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
#My solution
#O(n) time, O(1) space
class Solution:
    
    #Strategy: Recursively move down to the bottom of the tree, passing in the current node and default diameter (0) as we go
    #Once we reach a null node, we return (0, 0) where we have (node_height, node_diameter)
    #For each node that does exist, we unpack the tuple and store the results into a left/right height and left/right diameter vars. For ex, a leaf node will recieve (0, 0) and (0, 0)
    #From this result, we update the new diameter. We compare the max of the 2 diameters we receieved, and the sum of the left and right heights of the two connected nodes, and take the max of those values to be the new diameter
    #We then return this diameter and pass it back up to its parent, as well as the height of the current node + 1 (as we are moving up the tree)
    #Repeat until we reach the root
    #TLDR: In essence, starting at the bottom of the tree, we are keeping track of the maximum diameter along the way, and updating it where necessary by taking the sum of the max depths of its child nodes 
    
    def diameterOfBinaryTree(self, root: Optional[TreeNode]) -> int:
        
        #Return the max diameter at index 1
        return self.helper(root, 0)[1]
        
    def helper(self, node, diameter):
        
        if not node:
            return (0, 0)
        (left_height, left_diameter)  = self.helper(node.left, diameter)
        (right_height, right_diameter) = self.helper(node.right, diameter)
        
        #Update max diameter by comparing the max of the lower two diameters with the current diameter
        diameter = max(max(left_diameter, right_diameter), left_height + right_height)
        
        #Return the current height +.1 and the updated diameter
        return (1 + max(left_height, right_height), diameter)
        
        
#Ideal (simpler) solution
#O(n) time, O(1) space
class Solution:
    
    #Instead of passing in the max diameter everywhere, just keep a global variable
    
    def diameterOfBinaryTree(self, root: Optional[TreeNode]) -> int:
        
        self.ans = 0
        
        def helper(node):
            if not node:
                return 0
            left_height = helper(node.left)
            right_height = helper(node.right)
            
            self.ans = max(self.ans, left_height + right_height)
            
            return 1 + max(left_height, right_height)
        
        helper(root)
        return self.ans

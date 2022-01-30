# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

#My solution
#O(n) time, O(m) space, "m" is the max level of nodes at any level
class Solution:
    def averageOfLevels(self, root: Optional[TreeNode]) -> List[float]:
        
        #Strategy: Initialize a list of the root node
        #For each iteration, q will hold the nodes at the current level. We temporarily store the current length, for the average calc
        #We pop the nodes, add to the total sum, and add each node's children to a new list
        #Repeat this until the list of current nodes is empty
        averages = q = []
        q.append(root)
        
        while len(q):
            length = len(q)
            total = 0
            upcoming = []
            while len(q):
                curr = q.pop()
                total += curr.val
                if curr.left:
                    upcoming.append(curr.left)
                if curr.right:
                    upcoming.append(curr.right)
                    
            averages.append(total / length)
            q = upcoming
            
        return averages
            
#Alternative but more intuitive solution
#O(n) time, O(n) space
            
class Solution:
    def averageOfLevels(self, root: Optional[TreeNode]) -> List[float]:
        
        #Strategy: Same approach as above, just utilising a queue for normal BFS
        averages = []
        q = deque()
        q.append(root)
        
        while q:
            length = len(q)
            total = 0
            for i in range(0, length):
                curr = q.popleft()
                total += curr.val
                if curr.left:
                    q.append(curr.left)
                if curr.right:
                    q.append(curr.right)
                    
            averages.append(total / length)
            
        return averages

# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, x):
#         self.val = x
#         self.next = None

#My solution, ideal solution
#O(1) space
class Solution:
    def hasCycle(self, head: Optional[ListNode]) -> bool:
        
        #Strategy - fast and slow pointer, move fast pointer two steps for slow pointer's one step
        #If there's a cycle, the fast pointer will "lap" the slow one, and will point to the same node,
        #indicating a cycle. If the fast node reaches a "None" node, there is no cycle
        if not head:
            return False
        slow = fast = head
        while fast.next != None and fast.next.next != None:
            slow = slow.next
            fast = fast.next.next
            if slow == fast:
                return True
        return False

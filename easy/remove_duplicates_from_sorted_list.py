# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
#My solution, ideal solution
#O(n) time, O(1) space
class Solution:
    def deleteDuplicates(self, head: Optional[ListNode]) -> Optional[ListNode]:
        
        #Strategy: Have a fast and slow pointer, start them at the same node, and move the fast node up a spot if it has the same value as the slow node (as we need to remove duplicates)
        #Once the vals are not the same, set the slow pointer's next val to be the fast pointer, and then slide the slow pointer up to the fast pointer's position and repeat the same process
        slow = fast = head
        while slow != None:
            fast = fast.next
            while fast != None and fast.val == slow.val:
                fast = fast.next
            slow.next = fast
            slow = slow.next
        return head
        

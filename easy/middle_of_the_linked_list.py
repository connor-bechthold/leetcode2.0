# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def middleNode(self, head: Optional[ListNode]) -> Optional[ListNode]:
        
        #Strategy: Fast and slow pointer, once the fast pointer either becomes None or the next node it's pointing too is None, the slow pointer will be in the middle or second middle position, and can be returned
        slow = fast = head
        while fast != None and fast.next != None:
            slow = slow.next
            fast = fast.next.next
        return slow

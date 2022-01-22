# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next

#My solution, ideal solution
#O(n) time, O(1) space
class Solution:
    def removeElements(self, head: Optional[ListNode], val: int) -> Optional[ListNode]:
 
        #Check if the first n elements (including an empty list) contain the val, and move the head up accordingly
        while head != None and head.val == val:
            head = head.next
           
        #Set up a traversal node as the new head, and iterate through the list, removing nodes with the same value as we go until we reach the end
        trav = head
        while trav != None:
            if trav.next and trav.next.val == val:
                trav.next = trav.next.next
            else:   
                trav = trav.next
        
        return head

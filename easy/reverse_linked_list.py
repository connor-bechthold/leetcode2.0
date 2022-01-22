# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
#My solution, ideal solution
#O(n) time, O(1) space
class Solution:
    def reverseList(self, head: Optional[ListNode]) -> Optional[ListNode]:
        
        #No explanation, if you mess this up in an interview Connor you don't deserve the job
        trav = head
        back = None
        while trav != None:
            temp = trav
            trav = temp.next
            temp.next = back
            back = temp
        return back

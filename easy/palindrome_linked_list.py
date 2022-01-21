# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next

#My solution
#O(n) time, O(n) space
class Solution:
    def isPalindrome(self, head: Optional[ListNode]) -> bool:
        
        #Strategy: Find middle using two pointers, keeping track of vals along the way with stack. Then pop the stack and move the slow pointer to the end, comparing values along the way
        stack = []
        fast = slow = head
        while fast != None and fast.next != None:
            stack.append(slow.val)
            slow = slow.next
            fast = fast.next.next
        
        #Odd number of vals, middle val of palindrome is irrelevant, so move the slow pointer to the next val
        if fast != None:
            slow = slow.next
        
        while slow != None:
            top = stack.pop()
            if top != slow.val:
                return False
            slow = slow.next
            
        return True
    
#Optimal solution
#O(n) time, O(1) space
class Solution:
    def isPalindrome(self, head: Optional[ListNode]) -> bool:
        
        #Strategy: Same approach, but as we work towards the middle, reverse the first half of the linked list, and compare
        #Basically, an in place reversal of linked list but with more pain
        back = None
        fast = slow = head
        while fast != None and fast.next != None:
            temp = slow
            slow = slow.next
            fast = fast.next.next
            temp.next = back
            back = temp
        
        if fast != None:
            slow = slow.next
            
        while slow != None:
            if slow.val != back.val:
                return False
            slow = slow.next
            back = back.next
        return True
                    

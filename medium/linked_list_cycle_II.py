# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, x):
#         self.val = x
#         self.next = None

#My solution, ideal solution
#O(n) time, O(1) space
class Solution:
    def detectCycle(self, head: Optional[ListNode]) -> Optional[ListNode]:
        
    #Strategy: First find if a cycle exists as normal
    #If one does exist, fast and slow will be at some position past the start of the cycle
    #Let x rep the distance from the head to start
    #Let y rep the distance from the start to the intersection
    #Let z rep the the distance from the instersection to the start
    #Let C rep the length of the loop
    
    #We know the fast pointer travelled a distance x + n * C + y
    #Where n is the number of times it went around the cycle
    #The slow pointer travelled a distance x + y
    #So, because the fast pointer travelled twice the distance as the slow one:
    #2x + 2y = x + n * C + y
    #x + y = n * C
    #x = n * C - y = (n - 1) * C + (c - y) = (n - 1) * C + z
    #So, the distance from the head to the start of the loop is equal to going around the cycle n - 1 times plus going from the intersect to the start
    #The # of times we go around the loop doesn't really matter, as no matter how many times we cycle, we'll end up in the same spot
    #So, we just need to move from the head 'z' times to find the start
    #In order to do this, we simply iterate up from the head and the intersection one spot at a time, until they equal, where we'll be at the start of the loop

        if not head:
            return None
        
        slow = fast = head
        while fast.next and fast.next.next:
            slow = slow.next
            fast = fast.next.next
            if slow == fast:
                temp = head
                while temp != slow:
                    temp = temp.next
                    slow = slow.next
                return temp
        
        return None

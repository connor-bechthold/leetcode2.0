# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
#My solution, ideal solution
#O(n + m) time, O(1) space
class Solution:
    def mergeTwoLists(self, list1: Optional[ListNode], list2: Optional[ListNode]) -> Optional[ListNode]:
        
        #Strategy: Set two temp nodes to the two head nodes
        #While these are both not None, shift forward the temp node with the smaller or equal value when compared to the other node. Do this until the shifted node's next node is greater than the other node or equal to None
        #Here, set a bridge node equal to the shifted node and shift the shifted node up one more spot, and then connect the bridge node with the node that was not shifted
        #Repeat this process, until one of the temp nodes reaches a value of None
        #The smaller head will contain the merged list
        temp1 = list1
        temp2 = list2
        
        while temp1 != None and temp2 != None:
            if temp1.val <= temp2.val:
                while temp1.next != None and temp1.next.val <= temp2.val:
                    temp1 = temp1.next
                bridge = temp1
                temp1 = temp1.next
                bridge.next = temp2
            else:
                while temp2.next != None and temp2.next.val <= temp1.val:
                    temp2 = temp2.next
                bridge = temp2
                temp2 = temp2.next
                bridge.next = temp1
                
        if not list1 and not list2:
            return list1
        elif not list1 and list2:
            return list2
        elif not list2 and list1:
            return list1
        else:
            if list1.val <= list2.val:
                return list1
            else:
                return list2

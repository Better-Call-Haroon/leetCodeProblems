# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def deleteDuplicates(self, head: Optional[ListNode]) -> Optional[ListNode]:
        dummy = ListNode(0, head)  
        prev = dummy 
        seen = set()  

        while head:
            if head.val in seen:
                prev.next = head.next
            else:
                seen.add(head.val)
                prev = head 
            head = head.next  
        
        return dummy.next 
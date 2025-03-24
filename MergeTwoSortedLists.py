class Solution:
    def mergeTwoLists(self, list1: Optional[ListNode], list2: Optional[ListNode]) -> Optional[ListNode]:
        node_to_list1=[]
        node_to_list2=[]
        
        while list1:
            node_to_list1.append(list1.val)
            list1=list1.next
        while list2:
            node_to_list2.append(list2.val)
            list2=list2.next

        list3=node_to_list1+node_to_list2
        list3.sort()
        
        result=ListNode()
        current = result

        for val in list3:
            current.next = ListNode(val)  
            current = current.next
        return result.next
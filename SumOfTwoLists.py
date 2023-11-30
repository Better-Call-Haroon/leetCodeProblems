class Solution:
    def addTwoNumbers(self, l1: Optional[ListNode], l2: Optional[ListNode]) -> Optional[ListNode]:
        combined_variable_list1 = []
        combined_variable_list2 = []
        current=l1
        while current:
            combined_variable_list1.append(current.val)
            current=current.next

        current=l2
        while current:
            combined_variable_list2.append(current.val)
            current=current.next
        combined_result_list1 = ''.join(map(str, reversed(combined_variable_list1)))
        combined_result_list2 = ''.join(map(str, reversed(combined_variable_list2)))

        result = int(combined_result_list1) + int(combined_result_list2)
        dummy_head = ListNode()
        current = dummy_head
        for digit in str(result)[::-1]:
            current.next = ListNode(int(digit))
            current = current.next

        return dummy_head.next

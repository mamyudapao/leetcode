# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def isPalindrome(self, head: Optional[ListNode]) -> bool:
        if head is None:
            return True
        
        first_half_end = self.end_of_first_half(head)
        second_half_start = self.reverse_list(first_half_end.next)
        
        result = True
        first_position = head
        second_position = second_half_start
        while result and second_position is not None:
            if first_position.val != second_position.val:
                result = False
            first_position = first_position.next
            second_position = second_position.next
        return result

    
    def end_of_first_half(self, head):
        fast = head
        slow = head
        while fast.next and fast.next.next:
            fast = fast.next.next
            slow = slow.next
        return slow
    
    def reverse_list(self, head):
        previous = None
        current = head
        while current:
            next_node = current.next
            current.next = previous
            previous = current
            current = next_node
        return previous
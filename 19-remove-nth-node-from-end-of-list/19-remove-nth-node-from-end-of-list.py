class Solution:
    def removeNthFromEnd(self, head: Optional[ListNode], n: int) -> Optional[ListNode]:
      dummy = ListNode(0, head)
      first = head
      second = dummy
      for i in range(n):
        first = first.next

      while first:
        first = first.next
        second = second.next
        
      second.next = second.next.next
      return dummy.next
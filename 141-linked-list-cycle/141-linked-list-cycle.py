class Solution:
    def hasCycle(self, head: Optional[ListNode]) -> bool:
      if head is None:
        return False
      low_speed = head
      high_speed = head.next
      while high_speed != low_speed:
        if high_speed is None or high_speed.next is None:
          return False
        low_speed = low_speed.next
        high_speed = high_speed.next.next
      return True
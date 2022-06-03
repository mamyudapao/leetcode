class Solution:
    def hasCycle(self, head: Optional[ListNode]) -> bool:
      curr = head
      sets = set()
      while curr:
        if curr in sets:
          return True
        sets.add(curr)
        curr = curr.next
        
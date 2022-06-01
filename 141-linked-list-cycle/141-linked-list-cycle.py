class Solution:
  def hasCycle(self, head: Optional[ListNode]) -> bool:
    nodes_seen = set()
    curr = head
    while curr:
      if curr in nodes_seen:
        return True
      nodes_seen.add(curr)
      curr = curr.next
    return False
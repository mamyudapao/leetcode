class Solution:
    def hasCycle(self, head: Optional[ListNode]) -> bool:
        nodes_seen = set()
        while head:
            if head in nodes_seen:
                return True
            nodes_seen.add(head)
            head = head.next
        return False
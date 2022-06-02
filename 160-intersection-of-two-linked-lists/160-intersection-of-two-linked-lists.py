class Solution:
    def getIntersectionNode(self, headA: ListNode, headB: ListNode) -> Optional[ListNode]:
      nodes_in_B = set()
      while headB:
        nodes_in_B.add(headB)
        headB = headB.next
      
      while headA:
        if headA in nodes_in_B:
          return headA
        headA = headA.next
      return None
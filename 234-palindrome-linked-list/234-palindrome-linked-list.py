class Solution:
    def isPalindrome(self, head: Optional[ListNode]) -> bool:
      vals = []
      current_node = head
      while current_node:
        vals.append(current_node.val)
        current_node = current_node.next
      return vals == vals[::-1]
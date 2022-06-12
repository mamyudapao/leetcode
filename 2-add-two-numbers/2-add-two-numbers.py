class ListNode:
  def __init__(self, val=0, next=None):
    self.val = val
    self.next = next

class Solution:
  def addTwoNumbers(self, l1: ListNode, l2: ListNode) -> ListNode:
    carry = 0
    dummy = ListNode(None)
    head = dummy
    
    while l1 or l2 or carry:
      l1_num = l1.val if l1 else 0
      l2_num = l2.val if l2 else 0
      sum_num = l1_num + l2_num + carry
      new_num = sum_num % 10
      carry = sum_num // 10
      head.next = ListNode(new_num)
      head = head.next
      
      # l1たちの更新
      l1 = l1.next if l1 else None
      l2 = l2.next if l2 else None
    return dummy.next
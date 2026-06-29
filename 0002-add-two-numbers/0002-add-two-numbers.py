# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def addTwoNumbers(self, l1: Optional[ListNode], l2: Optional[ListNode]) -> Optional[ListNode]:
        n, n1, n2, s = 0, 0, 0, 0
        while l1:
            n1 += l1.val*10**n
            n += 1
            l1 = l1.next
        n = 0
        while l2:
            n2 += l2.val*10**n
            n += 1
            l2 = l2.next
        s = n1 + n2
        dummy = ListNode()
        tail = dummy
        if s==0:
            return ListNode(0)
        while s > 0:
            d = s%10
            s = s//10
            tail.next = ListNode(d)
            tail = tail.next
        return dummy.next
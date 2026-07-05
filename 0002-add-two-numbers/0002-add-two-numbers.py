# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def addTwoNumbers(self, l1: Optional[ListNode], l2: Optional[ListNode]) -> Optional[ListNode]:
        n1, n2 = 0, 0
        n = 0
        while l1:
            n1 += l1.val*(10**n)
            n += 1
            l1 = l1.next
        n = 0
        while l2:
            n2 += l2.val*(10**n)
            n += 1
            l2 = l2.next
        
        s = n1 + n2

        dummy = ListNode()
        tail = dummy

        if s==0:
            return ListNode(0)

        while s > 0:
            temp = s%10
            node = ListNode(temp)
            tail.next = node
            tail = tail.next
            s = s//10

        return dummy.next
# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def addTwoNumbers(self, l1: Optional[ListNode], l2: Optional[ListNode]) -> Optional[ListNode]:
        digit1 = 0
        digit2 = 0
        n=0
        while l1:
            digit1 += (l1.val*10**n)
            n += 1
            l1 = l1.next
        n = 0
        while l2:
            digit2 += (l2.val*10**n)
            n += 1
            l2 = l2.next
        s = digit1+digit2
        if s==0:
            return ListNode(0)
        dummy = ListNode()
        tail = dummy
        while s > 0:
            digit = s % 10
            s = s//10
            new_node = ListNode(digit)
            tail.next = new_node
            tail = tail.next
        return dummy.next


            
        
# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def deleteMiddle(self, head: Optional[ListNode]) -> Optional[ListNode]:
        if head.next == None:
            return None
        single = head
        double = head.next.next

        while double and double.next:
            single = single.next
            double = double.next.next
        single.next = single.next.next
        return head
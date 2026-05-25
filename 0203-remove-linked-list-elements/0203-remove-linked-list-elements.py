# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def removeElements(self, head: Optional[ListNode], val: int) -> Optional[ListNode]:
        dummy = ListNode(0, head)
        tail = dummy
        while tail:
            while tail.next and tail.next.val==val:
                tail.next = tail.next.next
            tail = tail.next
        return dummy.next
            
        
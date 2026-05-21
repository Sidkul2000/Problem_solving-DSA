# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def removeNthFromEnd(self, head: Optional[ListNode], n: int) -> Optional[ListNode]:
        dummy = ListNode()
        dummy.next = head
        slow, fast = dummy, head
        while n > 1:
            n -= 1
            fast = fast.next
        # slow => 1, fast => 2 (n=2)
        while fast.next:
            slow, fast = slow.next, fast.next
        # slow => 4 and fast=> 5
        slow.next = slow.next.next

        return dummy.next
        


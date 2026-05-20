# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def reorderList(self, head: Optional[ListNode]) -> None:
        """
        Do not return anything, modify head in-place instead.
        """
        # first find the half, then we reverse the second half and then finally we merge the 2 halves.

        slow, fast = head, head.next
        while fast and fast.next:
            slow = slow.next
            fast = fast.next.next

        # 1 -> 2 -> 3 -> 4

        # reverse the second half
        second = slow.next
        prev = None
        slow.next = None
        # 1 -> 2   ||   4 -> 3
        while second:
            temp = second.next
            second.next = prev
            prev = second
            second = temp
        
        # merge the halves

        first, second = head, prev

        while second:
            temp1 = first.next
            temp2 = second.next
            second.next = first.next
            first.next = second
            
            # 1 -> 4 -> 2
            first = temp1
            second = temp2


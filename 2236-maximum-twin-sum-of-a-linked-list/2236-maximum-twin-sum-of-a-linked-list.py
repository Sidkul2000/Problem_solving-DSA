# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def pairSum(self, head: Optional[ListNode]) -> int:
        # first find middle element
        # then reverse the list
        # then add the two lists and find max
        maxi = 0
        slow = head
        fast = head
        while fast and fast.next:
            fast = fast.next.next
            slow = slow.next

        curr = slow
        prev = None

        while curr:
            temp = curr.next
            curr.next = prev
            prev = curr
            curr = temp

        while prev:
            maxi = max(maxi, head.val + prev.val)
            prev = prev.next
            head = head.next
        return maxi


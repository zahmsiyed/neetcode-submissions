# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next

class Solution:
    def reverseList(self, head: Optional[ListNode]) -> Optional[ListNode]:
        done = None
        curr = head
        while curr:
            tail = curr.next
            curr.next = done
            done = curr
            curr = tail
        return done

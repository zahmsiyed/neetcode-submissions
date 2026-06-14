# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next

class Solution:
    def reverseList(self, head: Optional[ListNode]) -> Optional[ListNode]:
        
        new = None
        old = head

        while old is not None:
            temp = old.next
            old.next = new
            new = old
            old = temp

        return new

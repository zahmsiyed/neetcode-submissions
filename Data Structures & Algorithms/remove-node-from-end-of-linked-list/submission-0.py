# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next

class Solution:
    def removeNthFromEnd(self, head: Optional[ListNode], n: int) -> Optional[ListNode]:
        size = 1
        lastNode = head
        while lastNode.next:
            lastNode = lastNode.next
            size+=1
        
        if size == n:
            return head.next
        
        result = head
        finalPos = 1
        while finalPos<(size-n):
            result = result.next
            finalPos+=1
        result.next = result.next.next

        return head

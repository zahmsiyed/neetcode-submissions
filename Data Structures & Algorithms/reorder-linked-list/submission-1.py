# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next

class Solution:
    def reorderList(self, head: Optional[ListNode]) -> None:
        slow = head
        fast = head.next
        while fast and fast.next:
            slow=slow.next
            fast=fast.next.next
         
        secondHalf = slow.next
        slow.next = None
        secondHalf = self.reverseList(secondHalf)

        firstHalf = head
        while secondHalf:
            tail1 = firstHalf.next
            tail2 = secondHalf.next
            firstHalf.next = secondHalf
            secondHalf.next = tail1

            firstHalf = tail1
            secondHalf = tail2

    def reverseList(self, head) -> ListNode:
        done = None
        curr = head
        while curr:
            tail = curr.next
            curr.next = done
            done = curr
            curr = tail
        return done
        
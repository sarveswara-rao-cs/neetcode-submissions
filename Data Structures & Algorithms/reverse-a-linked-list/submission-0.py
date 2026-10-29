# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next

class Solution:
    def reverseList(self, head: Optional[ListNode]) -> Optional[ListNode]:
        if not head: return head

        rev = ListNode(head.val)
        temp = head
        temp = temp.next

        while temp:
            t = ListNode(temp.val)
            t.next = rev
            rev = t
            temp = temp.next
        return rev
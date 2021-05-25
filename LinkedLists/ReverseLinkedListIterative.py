class Solution:
    def reverseList(self, head: ListNode) -> ListNode:
        if head is None: return None
        prev = None
        while head is not None:
            next = head.next
            head.next = prev
            prev = head
            head = next
        return prev

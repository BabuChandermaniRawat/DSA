class Solution:
    def reverseList(self, head: ListNode) -> ListNode:
        def rev(head):
            if head is None or head.next is None: return head
            node1 = rev(head.next)
            head.next.next = head
            head.next = None
            return node1
        return rev(head)

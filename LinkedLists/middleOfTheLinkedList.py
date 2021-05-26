class Solution:
    def middleNode(self, head: ListNode) -> ListNode:
        if not head: return head
        slow, fast = head, head
        while fast.next and fast.next.next:
            slow = slow.next
            fast = fast.next.next
        if fast.next: return slow.next
        return slow

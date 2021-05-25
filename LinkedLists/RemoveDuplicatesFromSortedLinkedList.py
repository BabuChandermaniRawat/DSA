class Solution:
    def deleteDuplicates(self, head: ListNode) -> ListNode:
        if not head or not head.next: return head
        res, tail = head,head
        while head:
            while tail and tail.next and head.val==tail.next.val:
                tail = tail.next
            head.next = tail.next
            tail,head = tail.next, head.next
        return res 

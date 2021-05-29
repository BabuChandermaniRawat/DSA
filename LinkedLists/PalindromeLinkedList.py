class Solution:
    def isPalindrome(self, head: ListNode) -> bool:
        #approach is to break the list in 2, reverse and compare
        #breaking in 2 equal is tricky, keep conditions
        
        if head is None or head.next is None:
            return True
        slow = fast = end = head
        while fast.next and fast.next.next:
            end = slow
            slow = slow.next
            fast = fast.next.next
        
        if fast.next is None:
            end.next = None
            h2 = slow.next
        else:
            h2 = slow.next
            slow.next = None
        
        #reversing h2
        prev = None
        curr = h2
        while curr:
            next = curr.next
            curr.next = prev
            prev = curr
            curr = next
        head2 = prev
        
        #comparing for palindrome
        while head and head2:
            if head.val != head2.val:
                return False
            head = head.next
            head2 = head2.next
        return True

class Solution:
    def intersectionOfSortedLinkedLists(self, head1: ListNode, head2: ListNode) -> List:
        if not head1 and not head2: return []
        if not head1 or not head2: return []
        res = []
        """
        Approach: "sorted" is a hint for implementing it using pointers
        """
        while head1 and head2:
            if head1.val == head2.val: 
                res.append(head1.val)
                head1 = head1.next
            elif head1.val < head2.val:
                head1 = head1.next
            else:
                head2 = head2.next
        return res

class Solution:
    def getIntersectionNode(self, head1: ListNode, head2: ListNode) -> ListNode:
        if not head1 or not head2: return None
        mapp = {}
        while head1:
            mapp[head1] = True
            head1 = head1.next
        while head2:
            if head2 in mapp: return head2
            head2 = head2.next

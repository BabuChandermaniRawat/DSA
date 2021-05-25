class Solution:
    def moveLastItemToFront(self, head: ListNode) -> ListNode:
        """
        Approach 1: swapping the elements
        """
        def valuesSwappingApproach(head):
            if not head and not head.next: return head
            first = head
            result = head
            while head.next is None:
                head = head.next

            #swap values and return the result pointer
            first.val, head.val = head.val, first.val
            return result
        
        """
        Approach 2: split the linkedList into 3 parts and return the new orientation
        """
        def splittingListApproach(head):
            if not head and not head.next: return head
            first = head
            second = head.next
            first.next = None
            third = second
            if third.next.next:
                #logic for more than 2 elements in list
                while third.next.next:
                    third = third.next

                secondEnd = third
                third = third.next
                secondEnd.next = first
                third.next = second
                return third
            else:
                second.next = first
                return second

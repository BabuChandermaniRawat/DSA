"""
Approach: We can use the same approach which we used for adding 2 linked list.
"""

class Solution:
    def addOneToLinkedList(self, head: ListNode) -> ListNode:
        def reverseLinkedList(head):
            if not head: return None
            prev = None
            while head:
                next = head.next
                head.next = prev
                prev = head
                head = next
            return prev
        
        head = reverseLinkedList(head)
        result = head #maintaining pointer to return head of result
        
        carry = 0
        start = ListNode()
        while head:
            currentValue = head2.val + carry
                if currentValue>9:
                    nodeValue = int(str(currentValue)[-1]) #gives the last digit of a number
                    carry = int(str(currentValue)[0])
                else: 
                    carry = 0
                    nodeValue = currentValue
                start.next = ListNode(nodeValue)
                start = start.next
                head = head.next
                
        #very important edge case
        if carry>0:
            start.next = ListNode(carry)
            
        return reverseLinkedList(result.next)
        

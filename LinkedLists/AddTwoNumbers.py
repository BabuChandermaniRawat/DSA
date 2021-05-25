"""
Plain Brute Force Approach: Works for most of the organisation except Netflix and Facebook.
"""
class Solution:
    def addTwoNumbers(self, l1: ListNode, l2: ListNode) -> ListNode:
        def reverseLinkedList(head):
            if head is None: return None
            prev = None
            while head:
                next = head.next
                head.next = prev
                prev = head
                head = next
            return prev
        
        def makeLinkedListFromNumber(num):
            head = ListNode()
            start = head
            for char in num:
                start.next = ListNode(int(char))
                start = start.next
            return reverseLinkedList(head.next)
        
        def BruteForceApproach(head1,head2):
            num1,num2 = "",""
            while head1:
                num1+=str(head1.val)
                head1 = head1.next
            while head2:
                num2+=str(head2.val)
                head2 = head2.next
            return makeLinkedListFromNumber(str(int(num1)+int(num2)))
        
        return BruteForceApproach(l1,l2)
      
      
"""
Optimized Approach: While Traversing, maintain a carry variable and return the result in one pass.
"""
class Solution:
    def addTwoNumbers(self, head1: ListNode, head2: ListNode) -> ListNode:
        start = ListNode()
        result = start #pointer for tracking head of result
        
        #edge cases
        if not head1 and not head2: return None
        if not head1: return head2
        if not head2: return head1
        
        #try to iterate like merge technique of merge-sort Algorithm
        carry, nodeValue = 0, 0
        while head1 and head2:
            currentValue = head1.val + head2.val + carry
            if currentValue>9:
                nodeValue = int(str(currentValue)[-1]) #gives the last digit of a number
                carry = int(str(currentValue)[0])
            else: 
                carry = 0
                nodeValue = currentValue
            start.next = ListNode(nodeValue)
            start = start.next
            head1, head2 = head1.next, head2.next
            
        if head1:
            while head1:
                currentValue = head1.val + carry
                if currentValue>9:
                    nodeValue = int(str(currentValue)[-1]) #gives the last digit of a number
                    carry = int(str(currentValue)[0])
                else: 
                    carry = 0
                    nodeValue = currentValue
                start.next = ListNode(nodeValue)
                start = start.next
                head1 = head1.next
        
        if head2:
            while head2:
                currentValue = head2.val + carry
                if currentValue>9:
                    nodeValue = int(str(currentValue)[-1]) #gives the last digit of a number
                    carry = int(str(currentValue)[0])
                else: 
                    carry = 0
                    nodeValue = currentValue
                start.next = ListNode(nodeValue)
                start = start.next
                head2 = head2.next
                
        #very important edge case
        if carry>0:
            start.next = ListNode(carry)
            
        return result.next

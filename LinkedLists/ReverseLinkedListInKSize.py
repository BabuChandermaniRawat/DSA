class Solution:
    def reverseKGroup(self, head: ListNode, k: int) -> ListNode:
        if not head or not head.next:
            return head
        
        # Find length of list
        scanner, length = head, 0
        while scanner:
            length += 1
            scanner = scanner.next
        
        # Iteratively reverse groups of k, connecting reversed groups
        start = last = None
        while length - k >= 0:
            
            # Reverse first k nodes of head
            o_head = prev = head
            head = head.next
            for i in range(k-1):
                nextNode = head.next
                head.next = prev
                prev = head
                head = nextNode
            o_head.next = head
            head = prev
            
            # Connect last of previous group of k to newly reversed group
            if last:
                last.next = head
            
            # Save first node of reversed list to return after while loop
            if not start:
                start = head
                
            # Skip back through k nodes and save last node as last
            for i in range(k):
                last = head
                head = head.next
                length -= 1 
                   
        return start

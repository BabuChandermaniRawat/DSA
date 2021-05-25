class Solution:
    def removeCycleFromLinkedList(self, head: ListNode) -> ListNode:
        def getSlowPointer(head):
            slow, fast = head,head
            if head is None: return head
            while fast is not None and fast.next is not None:
                slow = slow.next
                fast = fast.next.next
                if slow==fast:
                    return slow
            return None
        
        def getCycleStartingPoint(head):
            slow = getSlowPointer(head)
            if slow is None: return None
            position = 0
            start = head
            while start != slow:
                start = start.next
                slow = slow.next
                position+=1
            return start
        
        def removeCycle(current, target):
            while current.next != target:
                current = current.next
            current.next = None
            
        startingPointOfLoop = getCycleStartingPoint(head)
        if startingPointOfLoop is None: return
        removeCycle(startingPointOfLoop.next, startingPointOfLoop)

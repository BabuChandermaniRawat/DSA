class Solution:
    def removeCycleFromCyclicLinkedList(self, head, deletedNode):
        deletedData = deletedNode.val
        toBeDeleted = head
        while toBeDeleted.next.val!=deletedData:
            toBeDeleted = toBeDeleted.next
        toBeDeleted.next = toBeDeleted.next.next
        return head

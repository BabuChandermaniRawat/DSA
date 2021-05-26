class ListNode(object):
    def __init__(self,val):
        self.val = val
        self.next = None

class LinkedList(object):
    def __init__(self):
        self.head = None

    def append(self,val):
        if not self.head:
            self.head = ListNode(val)
            return
        currentNode = ListNode(val)
        start = self.head
        while start.next:
            start = start.next
        start.next = currentNode

    def sortedMerge(self,head1,head2):
        if not head1: return head2
        if not head2: return head1
        result = None
        if head1.data<head2.data:
            result = head1
            result.next = self.sortedMerge(head1.next,head2)
        else:
            result = head2
            result.next = self.sortedMerge(head1,head2.next)
        return result

    def mergeSort(self,head):
        if not head or not head.next: return head
        middleElement = self.getMiddleElement(head)
        nextToMiddleElement = middleElement.next

        middleElement.next = None #breaking the list into 2 equal parts
        left = self.mergeSort(head)
        right = self.mergeSort(nextToMiddleElement)
        sortedLinkedList = self.sortedMerge(left,right)
        return sortedLinkedList

    def getMiddleElement(self,head):
        if not head or not head.next: return head
        slow, fast = head, head
        while fast.next and fast.next.next:
            slow = slow.next
            fast = fast.next.next
        if fast.next: return slow.next
        return slow

def outputLinkedList(head):
    if not head or not head.next: return None
    while head:
        print(head.val,'')
        head = head.next
    return

if __name__=="__main__":
    li = LinkedList()
    li.append(15)
    li.append(10)
    li.append(5)
    li.append(20)
    li.append(3)
    li.append(2)
    li.head = li.mergeSort(li.head)
    outputLinkedList(li.head)

def merge(head1,head2):
    if not head1: return head2
    if not head2: return head1
    if head1.data<head2.data:
        res = head1
        res.bottom = merge(head1.bottom,head2)
    else:
        res = head2
        res.bottom = merge(head1,head2.bottom)
    res.next = None
    return res

def flatten(head):
    if not head or not head.next: return head
    return merge(head,flatten(head.next))

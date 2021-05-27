/**
 * Definition for singly-linked list.
 * public class ListNode {
 *     int val;
 *     ListNode next;
 *     ListNode() {}
 *     ListNode(int val) { this.val = val; }
 *     ListNode(int val, ListNode next) { this.val = val; this.next = next; }
 * }
 */
class Solution {
    public ListNode middleNode(ListNode head) {
        if(head == null || head.next == null){
            return head;
        }
        int count = 0;
        ListNode node = head;
        while(node != null){
            count++;
            node = node.next;
        }
        int middle = count/2;
        System.out.println(middle);
        for(int i = 1;i<middle;i++){
            head = head.next;
        }
        
        return head.next;
    }
}
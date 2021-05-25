package LinkedList;
public class ReverseLinkedListGroup {
	static Node head;
    static class Node{
    	int data;
    	Node next;
    	Node(int data){
    		this.data = data;
    		this.next = null;
    	}
    }
    
    static Node reverseList(Node head, int k) {
    	if(head == null) {
    		return null;
    	}
    	Node current = head;
    	Node next = null;
    	Node prev = null;
    	
    	int count = 0;
    	
    	while(count < k && current != null) {
    		next = current.next;
    		current.next = prev;
    		prev = current;
    		current = next;
    		count++;
    	}
    	
    	if(next != null) {
    		head.next = reverseList(next,k);
    	}
    	
    	return prev;
    }
    
    static void printList(Node head) {
    	while(head != null) {
    		System.out.print(head.data+ " ");
    		head = head.next;
    	}
    	System.out.println();
    }
	public static void main(String[] args) {
		// TODO Auto-generated method stub
		ReverseLinkedListGroup reverseGroup = new ReverseLinkedListGroup();
		reverseGroup.head = new Node(85);
		reverseGroup.head.next = new Node(15);
		reverseGroup.head.next.next = new Node(4);
		reverseGroup.head.next.next.next = new Node(20);
		reverseGroup.printList(head);
		head = reverseGroup.reverseList(head, 2);
        reverseGroup.printList(head);
	}

}

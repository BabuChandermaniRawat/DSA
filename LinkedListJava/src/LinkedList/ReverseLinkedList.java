package LinkedList;

public class ReverseLinkedList {
	static Node head;
	//Node creation
    static class Node{
    	int data;
    	Node next;
    	
    	Node(int data){
    		this.data = data;
    		this.next = null;
    	}
    }
    static Node reverseList(Node head) {
    	Node prev = null;
    	Node current = head;
    	Node next = null;
    	while(current != null) {
    		next = current.next;
    		current.next = prev;
    		prev = current;
    		current = next;
    	}
    	head = prev;
    	return head;
    }
    //Print the linkedList
    static void printlist(Node node) {
    	while(node != null) {
    		System.out.print(node.data+" ");
    		node = node.next;
    	}
    	System.out.println();
    }
	public static void main(String[] args) {
		// TODO Auto-generated method stub
		ReverseLinkedList reverse = new ReverseLinkedList();
		reverse.head = new Node(85);
		reverse.head.next = new Node(15);
		reverse.head.next.next = new Node(4);
		reverse.head.next.next.next = new Node(20);
		reverse.printlist(head);
		head = reverse.reverseList(head);
        reverse.printlist(head);
	}

}

package LinkedList;

public class MoveToFront {
    static Node head;
    static class Node{
    	Node next;
    	int data;
    	Node(int data){
    		this.data = data;
    		this.next = null;
    	}
    }
    public void movetofront() {
    	Node temp = head;
    	if(head == null || head.next == null) {
    		return;
    	}
    	Node secondLast = null;
    	Node last = temp;
    	while(last.next != null) {
    		secondLast = last;
    		last = last.next;
    	}
    	
    	secondLast.next = null;
    	last.next = head;
    	
    	head = last;
    }
    public void printList(Node node) {
    	while(node != null) {
    		System.out.print(node.data+" ");
    		node = node.next;
    	}
    	System.out.println();
    }
	
	public static void main(String[] args) {
		// TODO Auto-generated method stub
       MoveToFront move = new MoveToFront();
       move.head = new Node(1);
       move.head.next = new Node(2);
       move.head.next.next = new Node(3);
       move.head.next.next.next = new Node(4);
       move.printList(head);
       move.movetofront();
       move.printList(head);
	}

}

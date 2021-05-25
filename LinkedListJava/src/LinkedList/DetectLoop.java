package LinkedList;

public class DetectLoop {
	static Node head;
    static class Node{
    	Node next;
    	int data;
    	Node(int data){
    		this.data = data;
    		this.next = null;
    	}
    }
    
    static boolean detectLoop(Node head) {
    	Node slow = head;
    	Node fast = head.next.next;
    	while(slow != null && fast.next != null) {
    	  if(slow == fast) {
    		return true;
    	  }
    	  slow = slow.next;
    	  fast = fast.next.next;
    	}
    	   return false;
    }
    
    static void printList(Node head) {
    	while(head != null) {
    		System.out.print(head.data);
    		head = head.next;
    	}
    }
	public static void main(String[] args) {
		// TODO Auto-generated method stub
        DetectLoop loop = new DetectLoop();
        loop.head = new Node(5);
        loop.head.next = new Node(10);
        loop.head.next.next = new Node(15);
        loop.head.next.next.next = new Node(20);
        loop.head.next.next.next.next = new Node(25);
        loop.head.next.next.next.next = loop.head.next;
        System.out.print(loop.detectLoop(head));
	}

}

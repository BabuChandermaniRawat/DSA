package LinkedList;
public class DeleteLoop {
    static Node head;
    static class Node{
    	Node next;
    	int data;
    	Node(int data){
    		this.data = data;
    		this.next = null;
    	}
    }
    
    static boolean deleteLoop(Node head) {
    	Node slow = head;
    	Node fast = head;
    	slow = head.next;
    	fast = fast.next.next;
    	while(fast != null && fast.next != null) {
    		if(slow == fast) {
    			break;
    		}
    		slow = slow.next;
    		fast = fast.next.next;
    	}
    	if(slow == fast) {
    		slow = head;
    		while(slow.next != fast.next) {
    			slow = slow.next;
    			fast = fast.next;
    		}
    		fast.next = null;
    		return true;
    	}
    	
    	return false;
    }
    static void printList(Node head) {
    	while(head != null) {
    		System.out.print(head.data+" ");
    		head = head.next;
    	}
    }
	public static void main(String[] args) {
		// TODO Auto-generated method stub
       DeleteLoop delete = new DeleteLoop();
       delete.head = new Node(1);
       delete.head.next = new Node(2);
       delete.head.next.next = new Node(3);
       delete.head.next.next.next = new Node(4);
       delete.head.next.next.next.next = new Node(5);
       delete.head.next.next.next.next.next = new Node(6);
       delete.head.next.next.next.next.next.next = new Node(7);
       delete.head.next.next.next.next.next.next.next = delete.head.next.next;
       System.out.println(delete.deleteLoop(head));
       delete.printList(head);
       
	}

}

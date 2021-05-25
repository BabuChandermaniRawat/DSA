package LinkedList;

public class FirstNodeInLoop {
	static Node head;
    static class Node{
    	int data;
    	Node next;
    	Node(int data){
    		this.data = data;
    		this.next = null;
    	}
    }
    
    public Node loopNode(Node node) {
    	Node temp = null;
    	Node slow = node;
    	Node fast = node;
    	slow = slow.next;
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
    		return fast.next;
    	}
    	return temp;
    }
	public static void main(String[] args) {
		// TODO Auto-generated method stub
       FirstNodeInLoop loop = new FirstNodeInLoop();
       loop.head = new Node(5);
       loop.head.next = new Node(6);
       loop.head.next.next = new Node(7);
       loop.head.next.next.next = new Node(8);
       loop.head.next.next.next.next = loop.head.next.next;
       System.out.print(loop.loopNode(head).data);
	}

}

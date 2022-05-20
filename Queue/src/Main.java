
public class Main {

	public static void main(String[] args) {
		Queue q = new Queue(10);
		q.enQueue(2043);
		q.enQueue(23);
		q.enQueue(53);
		int i = q.deQueue();
		System.out.println(i);
	}

}

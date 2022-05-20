
public class Queue {

	private int size, front, rear;
	private int maxSize;
	int[] array;
	
	public Queue(int maxSize) {
		this.maxSize = maxSize;
		this.size = 0;
		front = 0;
		rear = maxSize -1;
		array = new int[maxSize];
	}
	
	public void enQueue(int item) {
		if(this.isFull()) {
			System.out.println("Queue is full");
			return;
		}
		this.rear = (this.rear + 1) % this.maxSize;
		this.array[this.rear] = item;
		this.size ++;
		System.out.println(item + " added to queue");
	}
	
	public int deQueue() {
		if(this.isEmpty()) {
			System.out.println("Queue is empty, cannot dequeue");
			return Integer.MIN_VALUE;
		}
		int item = this.array[this.front];
		this.front = (this.front + 1) % this.maxSize;
		this.size --;
		return item;		
	}
	
	public boolean isFull() {
		return this.size == this.maxSize;
	}
	
	public boolean isEmpty() {
		return this.size == 0;
	}
	
	public int getSize() {
		return this.size;
	}
	
	public int getFront() {
		if(this.isEmpty()) return Integer.MIN_VALUE;
		return this.array[this.front];
	}
	
	public int getRear() {
		if(this.isEmpty()) return Integer.MIN_VALUE;
		return this.array[this.rear];
	}
	
}

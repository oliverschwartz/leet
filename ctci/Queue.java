import java.util.Stack;

public class Queue {
    private int size = 0;
    private Stack<Integer> mainStack;
    private Stack<Integer> revStack;

    public Queue() {
        mainStack = new Stack<Integer>();
        revStack = new Stack<Integer>();
    }

    public void enqueue(int i) {
        size++;
        mainStack.push(i);
    }

    public int dequeue() {
        if (this.isEmpty()) 
            throw new IllegalArgumentException();

        int newest;
        while (!(mainStack.empty())) {
            newest = mainStack.pop();
            revStack.push(newest);
        }

        int first = revStack.pop();

        while (!(revStack.empty())) {
            newest = revStack.pop();
            mainStack.push(newest);
        }

        size--;
        return first;
    }

    public int size() {
        return this.size;
    }

    public boolean isEmpty() {
        return this.size == 0;
    }

    public static void main(String[] args) {
        Queue q = new Queue();
        q.enqueue(1);
        q.enqueue(2);
        q.enqueue(3);
        System.out.println(q.dequeue());
        System.out.println(q.dequeue());
        System.out.println(q.dequeue());
    }
}

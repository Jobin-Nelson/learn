package collectionsdemo;

import java.util.PriorityQueue;

public class QueueDemo {
    public static void main(String arg[]) {
        PriorityQueue<String> queue = new PriorityQueue<>();

        queue.add("India");
        queue.add("America");
        queue.add("Germany");
        queue.add("Russia");

        System.out.println(queue);

        queue.remove();
        System.out.println("Queue after removing the first item: " + queue);

        String head = queue.peek();
        System.out.println("Head of the queue is: " + head);

        String firstElement = queue.poll();
        System.out.println("Removed element is: " + firstElement);

        System.out.println("Queue after removing its head is " + queue);
    }
}

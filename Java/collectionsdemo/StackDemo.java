package collectionsdemo;

import java.util.Stack;

public class StackDemo {
    public static void main(String arg[]) {
        Stack<String> stack = new Stack<>();

        stack.push("America");
        stack.push("China");
        stack.push("India");
        stack.push("Russia");

        System.out.println(stack);

        String poppedElement = stack.pop();
        System.out.println("Popped element is " + poppedElement);
        System.out.println("Stack after popping element " + stack);
    }
}

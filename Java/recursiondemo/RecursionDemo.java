package recursiondemo;

public class RecursionDemo {
    public static int factorial(int n) {
        if (n == 1) {
            return 1;
        } else {
            return (n * factorial(n - 1));
        }
    }

    public static int fibonnaci(int n) {
        if (n <= 1) {
            return 1;
        } else {
            return (n + fibonnaci(n - 1) + fibonnaci(n - 2));
        }
    }

    public static void main(String arg[]) {
        int n = 5;
        int fact = factorial(n);
        System.out.println("Factorial of " + n + " is " + fact);

        int fib = fibonnaci(n);
        System.out.println("Fibonnaci of " + n + " is " + fib);
    }
}

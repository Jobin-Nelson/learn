/**
 * A program to hype you up!
 */

public class HypeMachine {
    public static void main(String[] args) {
        System.out.println(args.length);
        int repeats = Integer.parseInt(args[0]);
        while (repeats > 0) {
            int randomNumber = (int) (Math.random() * 3);

            if (randomNumber == 0) {
                System.out.println("You are awesome!");
            } else if (randomNumber == 1) {
                System.out.println("You're the best!!!");
            } else {
                System.out.println("Keep up the great work!");
            }
            repeats--;
        }
    }
}
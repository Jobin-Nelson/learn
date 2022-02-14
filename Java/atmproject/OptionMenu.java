package atmproject;

import java.io.IOException;
import java.text.DecimalFormat;
import java.util.HashMap;
import java.util.Scanner;

public class OptionMenu extends Account {
    Scanner menuInput = new Scanner(System.in);
    DecimalFormat moneyFormat = new DecimalFormat("'$'###,##0.00");
    HashMap<Integer, Integer> data = new HashMap<>();

    public void getLogin() throws IOException {
        int x = 1;
        do {
            try {
                data.put(952141, 191904);
                data.put(989947, 71976);

                System.out.println("Welcome to our ATM project!");
                System.out.println("Enter your Customer Number: ");
                setCustomerNumber(menuInput.nextInt());

                System.out.println("Enter your Pin Number: ");
                setPinNumber(menuInput.nextInt());
            } catch (Exception e) {
                System.out.println("\n" + "Invalid character(s). Only numbers." + "\n");
                x = 2;
            }

            int cn = getCustomerNumber();
            int pn = getPinNumber();

            if (data.containsKey(cn) && (data.get(cn) == pn)) {
                System.out.println("Select the account you want to access");
                getAccountType();
            } else {
                System.out.println("\n" + "Wrong Customer Number or Pin Number" + "\n");
            }
        } while (x == 1);
    }

    public void getAccountType() {
        System.out.println("Select the Account you want to access");
        System.out.println(" Type 1 - Checking Account");
        System.out.println(" Type 2 - Saving Account");
        System.out.println(" Type 3 - Exit");

        switch (menuInput.nextInt()) {
            case 1:
                getChecking();
                break;
            case 2:
                getSaving();
                break;
            case 3:
                System.out.println("Thank you for using our ATM, bye. \n");
                break;
            default:
                System.out.println("\nInvalid Choice\n");
        }
    }

    public void getChecking() {
        System.out.println("Checking Account");
        System.out.println(" Type 1 - View balance");
        System.out.println(" Type 2 - Withdraw funds");
        System.out.println(" Type 3 - Deposit funds");
        System.out.println(" Type 4 - Exit");

        switch (menuInput.nextInt()) {
            case 1:
                System.out.println("Checking Account Balance: " + moneyFormat.format(getCheckingBalance()));
                getAccountType();
                break;
            case 2:
                getCheckingWithdraw();
                getAccountType();
                break;
            case 3:
                getCheckingDeposit();
                getAccountType();
                break;
            case 4:
                System.out.println("Thank you for using our ATM, bye. ");
                break;
            default:
                System.out.println("\nInvalid Choice\n");
                getChecking();
        }
    }

    public void getSaving() {
        System.out.println("Saving Account");
        System.out.println(" Type 1 - View balance");
        System.out.println(" Type 2 - Withdraw funds");
        System.out.println(" Type 3 - Deposit funds");
        System.out.println(" Type 4 - Exit");

        switch (menuInput.nextInt()) {
            case 1:
                System.out.println("Saving Account Balance: " + moneyFormat.format(getSavingBalance()));
                getAccountType();
                break;
            case 2:
                getSavingWithdraw();
                getAccountType();
                break;
            case 3:
                getSavingDeposit();
                getAccountType();
                break;
            case 4:
                System.out.println("Thank you for using our ATM, bye. ");
                break;
            default:
                System.out.println("\nInvalid Choice\n");
                getSaving();
        }
    }
}

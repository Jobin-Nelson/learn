package atmproject;

import java.text.DecimalFormat;
import java.util.Scanner;

public class Account {
    private int customerNumber;
    private int pinNumber;
    private int checkingBalance = 0;
    private int savingBalance = 0;

    Scanner input = new Scanner(System.in);
    DecimalFormat moneyFormat = new DecimalFormat("'$'###,##0.00");

    public void setCustomerNumber(int customerNumber) {
        this.customerNumber = customerNumber;
    }

    public void setPinNumber(int pinNumber) {
        this.pinNumber = pinNumber;
    }

    public int getCustomerNumber() {
        return this.customerNumber;
    }

    public int getPinNumber() {
        return this.pinNumber;
    }

    public int getCheckingBalance() {
        return checkingBalance;
    }

    public int getSavingBalance() {
        return savingBalance;
    }

    public double calcCheckingWithdraw(double amount) {
        checkingBalance -= amount;
        return checkingBalance;
    }

    public double calcCheckingDeposit(double amount) {
        checkingBalance += amount;
        return checkingBalance;
    }

    public double calcSavingWithdraw(double amount) {
        savingBalance -= amount;
        return savingBalance;
    }

    public double calcSavingDeposit(double amount) {
        savingBalance += amount;
        return savingBalance;
    }

    public void getCheckingWithdraw() {
        System.out.println("Checking Account Balance: " + moneyFormat.format(checkingBalance));
        System.out.println("Amount you want to withdraw from the account");
        double amount = input.nextDouble();

        if ((checkingBalance - amount) >= 0) {
            calcCheckingWithdraw(amount);
            System.out.println("New Checking Account Balance: " + moneyFormat.format(checkingBalance));
        } else {
            System.out.println("Balance cannot be negative. \n");
        }
    }

    public void getSavingWithdraw() {
        System.out.println("Saving Account Balance: " + moneyFormat.format(savingBalance));
        System.out.println("Amount you want to withdraw from the account");
        double amount = input.nextDouble();

        if ((savingBalance - amount) >= 0) {
            calcSavingWithdraw(amount);
            System.out.println("New Saving Account Balance: " + moneyFormat.format(savingBalance));
        } else {
            System.out.println("Balance cannot be negative. \n");
        }
    }

    public void getCheckingDeposit() {
        System.out.println("Checking Account Balance: " + moneyFormat.format(checkingBalance));
        System.out.println("Amount you want to Deposit to the account");
        double amount = input.nextDouble();

        if ((checkingBalance + amount) >= 0) {
            calcCheckingDeposit(amount);
            System.out.println("New Checking Account Balance: " + moneyFormat.format(checkingBalance));
        } else {
            System.out.println("Balance cannot be negative. \n");
        }
    }

    public void getSavingDeposit() {
        System.out.println("Saving Account Balance: " + moneyFormat.format(savingBalance));
        System.out.println("Amount you want to Deposit to the account");
        double amount = input.nextDouble();

        if ((savingBalance + amount) >= 0) {
            calcSavingDeposit(amount);
            System.out.println("New Saving Account Balance: " + moneyFormat.format(savingBalance));
        } else {
            System.out.println("Balance cannot be negative. \n");
        }
    }

}

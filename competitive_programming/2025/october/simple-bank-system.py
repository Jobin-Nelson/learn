"""
Created Date: 2025-10-26
Qn: You have been tasked with writing a program for a popular bank that will
    automate all its incoming transactions (transfer, deposit, and withdraw).
    The bank has n accounts numbered from 1 to n. The initial balance of each
    account is stored in a 0-indexed integer array balance, with the (i + 1)th
    account having an initial balance of balance[i].

    Execute all the valid transactions. A transaction is valid if:

    - The given account number(s) are between 1 and n, and
    - The amount of money withdrawn or transferred from is less than or equal
      to the balance of the account.

    Implement the Bank class:

    - Bank(long[] balance) Initializes the object with the 0-indexed integer
      array balance.
    - boolean transfer(int account1, int account2, long money) Transfers money
      dollars from the account numbered account1 to the account numbered
      account2. Return true if the transaction was successful, false otherwise.
    - boolean deposit(int account, long money) Deposit money dollars into the
      account numbered account. Return true if the transaction was successful,
      false otherwise.
    - boolean withdraw(int account, long money) Withdraw money dollars from the
      account numbered account. Return true if the transaction was successful,
      false otherwise.
Link: https://leetcode.com/problems/simple-bank-system/
Notes:
    - use simulation
"""

import unittest


class Bank:
    def __init__(self, balance: list[int]):
        self.accounts = balance
        self.total_accounts = len(balance)

    def is_account_valid(self, account: int) -> bool:
        return account <= self.total_accounts

    def has_enough_money(self, account: int, money: int) -> bool:
        return self.accounts[account - 1] >= money

    def transfer(self, account1: int, account2: int, money: int) -> bool:
        if (
            not self.is_account_valid(account1)
            or not self.is_account_valid(account2)
            or not self.has_enough_money(account1, money)
        ):
            return False
        self.accounts[account1 - 1] -= money
        self.accounts[account2 - 1] += money
        return True

    def deposit(self, account: int, money: int) -> bool:
        if not self.is_account_valid(account):
            return False
        self.accounts[account - 1] += money
        return True

    def withdraw(self, account: int, money: int) -> bool:
        if (
            not self.is_account_valid(account)
            or not self.has_enough_money(account, money)
        ):
            return False
        self.accounts[account - 1] -= money
        return True

class TestSolution(unittest.TestCase):
    def test1(self):
        balance = [10, 100, 20, 50, 30]
        b = Bank(balance)
        self.assertEqual(True, b.withdraw(3, 10))
        self.assertEqual(True, b.transfer(5, 1, 20))
        self.assertEqual(True, b.deposit(5, 20))
        self.assertEqual(False, b.transfer(3, 4, 15))
        self.assertEqual(False, b.withdraw(10, 50))


if __name__ == '__main__':
    unittest.main()

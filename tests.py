import unittest
import main


class TestsBankAccount(unittest.TestCase):
    def setUp(self):
        self.bank_account = main.BankAccount()

    def test_deposit_1(self):
        self.bank_account.deposit(100)
        result = self.bank_account.get_balance()
        expected_result = 100
        self.assertEqual(result, expected_result)

    def test_deposit_2(self):
        with self.assertRaises(ValueError):
            self.bank_account.deposit(0)

    def test_deposit_3(self):
        with self.assertRaises(ValueError):
            self.bank_account.deposit(-1)

    def test_withdraw_1(self):
        self.bank_account.deposit(100)
        self.bank_account.withdraw(100)
        result = self.bank_account.get_balance()
        expected_result = 0
        self.assertEqual(result, expected_result)

    def test_withdraw_2(self):
        self.bank_account.deposit(100)
        with self.assertRaises(main.InsufficientFunds):
            self.bank_account.withdraw(101)

    def test_withdraw_3(self):
        with self.assertRaises(ValueError):
            self.bank_account.withdraw(0)

    def test_transfer_1(self):
        with self.assertRaises(TypeError):
            self.bank_account.transfer("ved", 100)

    def test_transfer_2(self):
        self.bank_account.deposit(100)
        other_account = main.BankAccount()
        self.bank_account.transfer(other_account,100)
        result = other_account.get_balance()
        expected_result = 100
        self.assertEqual(result, expected_result)


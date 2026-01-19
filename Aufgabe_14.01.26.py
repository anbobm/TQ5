import unittest
from bank_account import BankAccount, InsufficientFundsError


class TestBankAccount(unittest.TestCase):

    def setUp(self):
        self.alice = BankAccount("Alice", 100.0)
        self.bob = BankAccount("Bob", 50.0)

    def test_initial_balance(self):
        self.assertEqual(self.alice.balance, 100.0)

    def test_negative_initial_balance_raises(self):
        with self.assertRaises(ValueError):
            BankAccount("Eve", -10)

    def test_deposit_increases_balance(self):
        self.alice.deposit(25.0)
        self.assertEqual(self.alice.balance, 125.0)

    def test_deposit_zero_or_negative_raises(self):
        for amount in (0, -5):
            with self.assertRaises(ValueError):
                self.alice.deposit(amount)

    def test_withdraw_decreases_balance(self):
        self.alice.withdraw(40.0)
        self.assertEqual(self.alice.balance, 60.0)

    def test_withdraw_more_than_balance_raises(self):
        with self.assertRaises(InsufficientFundsError):
            self.alice.withdraw(1000.0)

    def test_withdraw_zero_or_negative_raises(self):
        for amount in (0, -1):
            with self.assertRaises(ValueError):
                self.alice.withdraw(amount)

    def test_transfer_moves_money_between_accounts(self):
        self.alice.transfer_to(self.bob, 30.0)

        self.assertEqual(self.alice.balance, 70.0)
        self.assertEqual(self.bob.balance, 80.0)

    def test_transfer_insufficient_funds(self):
        with self.assertRaises(InsufficientFundsError):
            self.bob.transfer_to(self.alice, 100.0)

    def test_transfer_invalid_target_raises(self):
        with self.assertRaises(TypeError):
            self.alice.transfer_to("not an account", 10)

    def test_transfer_is_atomic(self):
        """Balances should not change if transfer fails."""
        alice_balance = self.alice.balance
        bob_balance = self.bob.balance

        with self.assertRaises(InsufficientFundsError):
            self.bob.transfer_to(self.alice, 999)

        self.assertEqual(self.alice.balance, alice_balance)
        self.assertEqual(self.bob.balance, bob_balance)


if __name__ == "__main__":
    unittest.main()
 
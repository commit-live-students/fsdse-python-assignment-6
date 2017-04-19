from unittest import TestCase
from errors import no_function_found, incorrect_output, succeed


class TestAccount(TestCase):
    def test_deposit_savings(self):
        try:
            from account import Savings
            sa = Savings("123")
            try:
                sa.deposit(1500)
            except:
                self.assertFalse(no_function_found("deposit"))
            self.assertEqual(1500, sa.balance)
            self.assertTrue(succeed("Savings.deposit"))
        except ImportError:
            self.assertFalse(no_function_found("Savings"))
        except AssertionError:
            self.assertFalse(incorrect_output())


    def test_widraw_savings(self):
        try:
            from account import Savings
            sa = Savings("123")
            try:
                sa.deposit(1500)
            except:
                self.assertFalse(no_function_found("Savings.deposit"))

            try:
                sa.withdraw(300)
            except:
                self.assertFalse(no_function_found("Savings.widraw"))

            self.assertEqual(1200, sa.balance)
            self.assertTrue(succeed("Savings.deposit"))
        except ImportError:
            self.assertFalse(no_function_found("Savings"))
        except AssertionError:
            self.assertFalse(incorrect_output())

    def test_deposit_current(self):
        try:
            from account import Current
            ca = Current("456")
            try:
                ca.deposit(20000)
            except:
                self.assertFalse(no_function_found("Savings.deposit"))
            self.assertEqual(20000, ca.balance)
            self.assertTrue(succeed("Savings.deposit"))
        except ImportError:
            self.assertFalse(no_function_found("Current"))
        except AssertionError:
            self.assertFalse(incorrect_output())


    def test_widraw_current(self):
        try:
            from account import Current
            ca = Current("456")
            try:
                ca.deposit(20000)
            except:
                self.assertFalse(no_function_found("Current.deposit"))

            try:
                ca.withdraw(1)
            except:
                self.assertFalse(no_function_found("Current.widraw"))

            self.assertEqual(19998.9, ca.balance)
            self.assertTrue(succeed("Current.deposit"))
        except ImportError:
            self.assertFalse(no_function_found("Current"))
        except AssertionError:
            self.assertFalse(incorrect_output())
import unittest
from tkinter import Tk
from entities.credit import Credit


class TestCredit(unittest.TestCase):
    def setUp(self):
        self.root = Tk()
        self.credit = Credit()

    def test_start_credit_balance(self):
        self.assertEqual(self.credit.value.get(), 0)

    def test_add_1_credit(self):
        self.credit.add_1_credit()
        self.assertEqual(self.credit.value.get(), 1)

    def test_add_5_credit(self):
        self.credit.add_5_credit()
        self.assertEqual(self.credit.value.get(), 5)

    def test_add_10_credit(self):
        self.credit.add_10_credit()
        self.assertEqual(self.credit.value.get(), 10)

    def test_use_credits(self):
        self.credit.add_10_credit()
        self.credit.add_10_credit()
        self.assertEqual(self.credit.value.get(), 20)
        self.credit.use_credit(1)
        self.assertEqual(self.credit.value.get(), 19)
        self.credit.use_credit(2)
        self.assertEqual(self.credit.value.get(), 17)
        self.credit.use_credit(5)
        self.assertEqual(self.credit.value.get(), 12)
        self.credit.use_credit(10)
        self.assertEqual(self.credit.value.get(), 2)


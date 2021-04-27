import unittest
from tkinter import Tk
from ui import UI


class TestUi(unittest.TestCase):
    def setUp(self):
        self.root = Tk()
        self.ui = UI(self.root)
        self.ui.start()

    def test_if_gui_exists(self):
        self.assertNotEqual(self.root, None)

    def test_start_credits_balance(self):
        self.assertEqual(self.ui.credits.get(), 0)

    def test_add_1_credits(self):
        self.ui.add_1_credits()
        self.assertEqual(self.ui.credits.get(), 1)

    def test_add_5_credits(self):
        self.ui.add_5_credits()
        self.assertEqual(self.ui.credits.get(), 5)

    def test_add_10_credits(self):
        self.ui.add_10_credits()
        self.assertEqual(self.ui.credits.get(), 10)

    def test_use_credits(self):
        self.ui.add_10_credits()
        self.ui.add_10_credits()
        self.assertEqual(self.ui.credits.get(), 20)
        self.ui.use_credits(1)
        self.assertEqual(self.ui.credits.get(), 19)
        self.ui.use_credits(2)
        self.assertEqual(self.ui.credits.get(), 17)
        self.ui.use_credits(5)
        self.assertEqual(self.ui.credits.get(), 12)
        self.ui.use_credits(10)
        self.assertEqual(self.ui.credits.get(), 2)

    def test_raise_bet(self):
        # starting self.bet is set as 1
        self.assertEqual(self.ui.bet.get(), 1)
        self.ui.raise_bet()
        # self.bet should be now 2
        self.assertEqual(self.ui.bet.get(), 2)
        self.ui.raise_bet()
        # self.bet should be now 5
        self.assertEqual(self.ui.bet.get(), 5)
        self.ui.raise_bet()
        # self.bet should be now 10
        self.assertEqual(self.ui.bet.get(), 10)
        self.ui.raise_bet()
        # self.bet should be now back to 1
        self.assertEqual(self.ui.bet.get(), 1)

    def test_play(self):
        self.assertEqual(self.ui.play(), False)
        self.ui.add_10_credits()
        self.assertEqual(self.ui.play(), True)
        # self.credits should be now 9
        self.ui.use_credits(8)
        # self.credits should be now 1
        self.assertEqual(self.ui.play(), True)
        # self.credits should be now 0
        self.assertEqual(self.ui.play(), False)

    def test_wheel_value_at_start(self):
        self.assertEqual(self.ui.first_wheel.value, None)
        self.assertEqual(self.ui.second_wheel.value, None)
        self.assertEqual(self.ui.third_wheel.value, None)

        self.assertEqual(self.ui.first_wheel_display_value.get(), 0)
        self.assertEqual(self.ui.second_wheel_display_value.get(), 0)
        self.assertEqual(self.ui.third_wheel_display_value.get(), 0)

    def test_spin_all_wheels(self):
        self.ui.spin_all_wheels()
        print(self.ui.first_wheel_display_value.get())
        self.assertNotEqual(self.ui.first_wheel.value, None)
        self.assertNotEqual(self.ui.second_wheel.value, None)
        self.assertNotEqual(self.ui.third_wheel.value, None)

        self.assertNotEqual(self.ui.first_wheel_display_value.get(), 0)
        self.assertNotEqual(self.ui.second_wheel_display_value.get(), 0)
        self.assertNotEqual(self.ui.third_wheel_display_value.get(), 0)

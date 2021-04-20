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

    def test_start_coin_balance(self):
        self.assertEqual(self.ui.coin.get(), 0)

    def test_add_1_coin(self):
        self.ui.add_1_coin()
        self.assertEqual(self.ui.coin.get(), 1)

    def test_add_5_coin(self):
        self.ui.add_5_coin()
        self.assertEqual(self.ui.coin.get(), 5)

    def test_add_10_coin(self):
        self.ui.add_10_coin()
        self.assertEqual(self.ui.coin.get(), 10)

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

import unittest
from tkinter import *
from tkinter.ttk import *
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

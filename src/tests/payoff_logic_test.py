import unittest
from entities.payoff_logic import Payoff


class TestPayoff(unittest.TestCase):
    def setUp(self):
        self.payoff = Payoff()

    def test_check_for_win_true(self):
        self.assertEqual(self.payoff.check_for_win(1, 1, 1), True)

    def test_check_for_win_false(self):
        self.assertEqual(self.payoff.check_for_win(1, 1, 2), False)

    def test_payoff_amount(self):
        wheel = 1
        bet = 5
        self.assertEqual(self.payoff.payoff_amount(wheel, bet), (wheel + 1) * bet)

import unittest
from entities.game_logic import GameLogic


class TestGameLogic(unittest.TestCase):

    def setUp(self):
        self.game_logic = GameLogic()

    def test_start(self):
        self.assertEqual(self.game_logic.bet.get(), 0)
        self.game_logic.start()
        self.assertEqual(self.game_logic.bet.get(), 1)

    def test_play(self):
        self.assertEqual(self.game_logic.play(), False)
        self.game_logic.credits.add_1_credit()
        self.game_logic.raise_bet()
        self.assertEqual(self.game_logic.play(), True)

    def test_raise_bet(self):
        self.assertEqual(self.game_logic.bet.get(), 0)
        self.game_logic.raise_bet()
        self.assertEqual(self.game_logic.bet.get(), 1)
        self.game_logic.raise_bet()
        self.assertEqual(self.game_logic.bet.get(), 2)

    def test_spin_all_wheels(self):
        self.assertEqual(self.game_logic.first_wheel.value, None)
        self.assertEqual(self.game_logic.second_wheel.value, None)
        self.assertEqual(self.game_logic.third_wheel.value, None)
        self.game_logic.spin_all_wheels()
        self.assertNotEqual(self.game_logic.first_wheel.value, None)
        self.assertNotEqual(self.game_logic.second_wheel.value, None)
        self.assertNotEqual(self.game_logic.third_wheel.value, None)

    def test_unlock_all_and_spin(self):
        for wheel in self.game_logic.list_of_wheels:
            wheel.set_locked()
            self.assertEqual(wheel.is_locked, True)

        self.game_logic.unlock_all_and_spin()

        for wheel in self.game_logic.list_of_wheels:
            self.assertEqual(wheel.is_locked, False)

    def test_check_locked_wheels(self):
        self.assertEqual(self.game_logic.check_locked_wheels(), True)
        self.game_logic.list_of_wheels[0].set_locked()
        self.assertEqual(self.game_logic.check_locked_wheels(), True)

        for wheel in self.game_logic.list_of_wheels:
            wheel.set_locked()

        self.assertEqual(self.game_logic.check_locked_wheels(), False)





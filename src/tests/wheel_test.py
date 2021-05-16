import unittest
from entities.wheel import Wheel


class TestWheel(unittest.TestCase):
    def setUp(self):
        self.wheel = Wheel()

    def test_set_value(self):
        self.wheel.value = None
        self.assertEqual(self.wheel.value, None)

    def test_spin(self):
        self.wheel.spin()
        self.assertNotEqual(self.wheel.value, None)

    def test_set_locked(self):
        self.wheel.set_locked()
        self.assertEqual(self.wheel.is_locked, True)

    def test_set_unlocked(self):
        self.wheel.set_unlocked()
        self.assertEqual(self.wheel.is_locked, False)

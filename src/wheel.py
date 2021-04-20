import random


class Wheel:

    def __init__(self):
        self.value = None
        self.is_locked = False

    def spin(self):
        self.value = random.randint(1, 5)

    def set_locked(self):
        self.is_locked = True

    def set_unlocked(self):
        self.is_locked = False

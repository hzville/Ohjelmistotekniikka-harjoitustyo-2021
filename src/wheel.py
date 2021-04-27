import random


class Wheel:

    def __init__(self):
        self.value = None
        self.is_locked = False

    def spin(self):
        if not self.is_locked:
            self.value = random.randint(1, 5)

    def check_if_locked(self):
        if self.value is None:
            pass
        if self.is_locked:
            self.set_unlocked()
        else:
            self.set_locked()

    def set_locked(self):
        self.is_locked = True

    def set_unlocked(self):
        self.is_locked = False

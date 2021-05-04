import random
from tkinter import IntVar


class Wheel:
    """ Luokka jolla voidaan luoda yksittäinen pelilinja

    Attributes:
        value: pelilinjan kuvio
        is_locked: onko pelilinja lukittu
        display_value = käyttöliittymässä näytettävä pelilinjan kuvio
    """

    def __init__(self):
        """Konstruktori joka luo uuden pelilinjan """

        self.value = None
        self.is_locked = False
        self.display_value = IntVar()
        self.display_value.set(0)

    def spin(self):
        """Arpoo pelilinjalle satunnaisen kuvion jos pelilinjaa ei ole lukittu"""

        if not self.is_locked:
            self.value = random.randint(1, 5)
            self.display_value.set(self.value)

    def check_if_locked(self):
        """Tarkistaa onko pelilinja lukittu ja muuttaa sen vastakkaiseksi arvoksi"""

        if self.value is None:
            pass
        if self.is_locked:
            self.set_unlocked()
        else:
            self.set_locked()

    def set_locked(self):
        """Lukitsee pelilinjan"""

        self.is_locked = True

    def set_unlocked(self):
        """Avaa pelilinjan"""

        self.is_locked = False

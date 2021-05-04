from tkinter import IntVar


class Credit:
    """Luokalla tallennetaan ja hallinnoidaan pelivarojen määrää.

    Attributes:
        value = Pelivarojen määrä
    """

    def __init__(self):
        """ Konstruktori joka luo pelivara-olion.
        """

        self.value = IntVar()

    def initialize_variables(self):
        """Asettaa pelivarjoen määräksi 0 pelin alussa"""

        self.value.set(0)

    def add_1_credit(self):
        """Lisää pelivaroihin 1 krediitin"""

        self.value.set(self.value.get() + 1)

    def add_5_credit(self):
        """Lisää pelivaroihin 5 krediittiä"""

        self.value.set(self.value.get() + 5)

    def add_10_credit(self):
        """Lisää pelivaroihin 10 krediittiä"""

        self.value.set(self.value.get() + 10)

    def use_credit(self, bet: int):
        """Vähentää pelivarojen määrää annetun pelipanoksen verran
        Args:
            bet: vähennettävä määrä
            """

        self.value.set(self.value.get() - bet)

    def add_payoff(self, amount: int):
        """Kasvattaa pelivarojen määrää annetun parametrin verran
        Args:
            amount: kasvatettava määrä
            """

        self.value.set(self.value.get() + amount)

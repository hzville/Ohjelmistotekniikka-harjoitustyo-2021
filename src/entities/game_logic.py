from tkinter import IntVar
from entities.wheel import Wheel
from entities.credit import Credit
from entities.payoff_logic import Payoff


class GameLogic:    # pylint: disable=too-many-instance-attributes
    # all instance-attributes are needed to run the show
    """ Luokka toteuttaa pelin toiminnallisuuden ja logiikan, käyttäen apunaan eri olioita.

    Attributes:
        first_wheel = yksittäinen pelilinja, Wheel-olio
        second_wheel = yksittäinen pelilinja, Wheel-olio
        third_wheel = yksittäinen pelilinja, Wheel-olio
        credits = pelivarat, Credit-olio
        bet = pelipanos
        bet_list = lista eri pelipanoksista
        payoff = voittojen laskemiseen käytettävä Payoff-olio
        last_win_amount = viimeisin voiton suuruus
        list_of_wheels = kaikki voittolinjat sisältävä lista
        can_be_locked = käytetään pelilinjoen lukituksen ohitukseen
    """
    def __init__(self):
        """"Konstruktori joka luo pelilogiikan olion.
        """

        self.first_wheel = Wheel()
        self.second_wheel = Wheel()
        self.third_wheel = Wheel()
        self.credits = Credit()
        self.bet = IntVar()
        self.bet_list = [1, 2, 5, 10]
        self.payoff = Payoff()
        self.last_win_amount = IntVar()
        self.last_win_amount.set(0)
        self.list_of_wheels = (self.first_wheel, self.second_wheel, self.third_wheel)
        self.can_be_locked = True

    def start(self):
        """Alustaa pelipanoksen oikeaksi
        """
        self.raise_bet()

    def play(self):
        """Tarkistaa riittävätkö pelivarat pelaamiseen, olivatko aiemmalla kieroksella
        pelilinjat lukittu ja arpoo pelilinjoille uudet arvot"""

        if self.check_credits():
            if not self.can_be_locked:
                self.unlock_all_and_spin()
            else:
                if self.check_locked_wheels():
                    self.use_credit_and_spin()
            return True
        return False

    def check_credits(self):
        """Tarkistaa riittävät pelivarat pelin pelaamiseen"""
        if self.credits.value.get() == 0:
            return False

        if self.credits.value.get() < self.bet.get():
            return False
        return True

    def check_locked_wheels(self):
        """Tarkistaa olivatko osa pelilinjoista lukittu edellisellä kieroksella. """

        locked_wheels = 0
        for wheel in self.list_of_wheels:
            if wheel.is_locked:
                locked_wheels += 1
                self.can_be_locked = False
        if locked_wheels > len(self.list_of_wheels) - 1:
            self.can_be_locked = True
            return False
        return True

    def unlock_all_and_spin(self):
        """Käytetään pelilinjojen lukituksen vapauttamiseen, jos esim. edellisellä kierroksella
        osa linjoista on ollut lukittuna. Jokaisen pelikierroksen jälkeen joka sisältää lukitun
        pelilinja, tulee olla vähintaa yksi kierros jossa kaikki pelilinjat arvotaan uudestaan """

        self.first_wheel.set_unlocked()
        self.second_wheel.set_unlocked()
        self.third_wheel.set_unlocked()
        self.use_credit_and_spin()
        self.can_be_locked = True

    def use_credit_and_spin(self):
        """Toiminnallisuus joka kuluttaa pelivaroja panoksen verran,
        arpoo uudet arvot pelilinjoilla ja tarkistaa tuliko voittoa"""

        self.credits.use_credit(self.bet.get())
        self.spin_all_wheels()
        self.check_for_payoff()

    def check_for_payoff(self):
        """Tarkistaa tuliko kierroksella voittoa"""

        if self.payoff.check_for_win(self.first_wheel.value,
                                     self.second_wheel.value,
                                     self.third_wheel.value):

            payoff_amount = self.payoff.payoff_amount(self.first_wheel.value, self.bet.get())
            self.credits.add_payoff(payoff_amount)
            self.last_win_amount.set(payoff_amount)
            self.can_be_locked = False


    def raise_bet(self):
        """Korottaa pelipanoksen"""

        next_bet = self.bet_list.pop(0)
        self.bet.set(next_bet)
        self.bet_list.append(next_bet)

    def spin_all_wheels(self):
        """Arpoo uudet arvot pelilinjoille jotka eivät ole lukittu"""

        self.first_wheel.spin()
        self.second_wheel.spin()
        self.third_wheel.spin()

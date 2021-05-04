
class Payoff:
    """Luokka joka määrittää voiton ja sen määrän"""

    def check_for_win(self, first: int, second: int, third: int):
        """Tarkistaa voittiko pelaaja

        Args:
            first: ensimmäisen pelilinjan arvo
            second: toisen pelilinjan arvo
            third: kolmannen pelilinjan arvo

        Returns:
            True: jos kaikkien pelilinjojen arvo on sama, muutoin False
        """

        if first == second and second == third:
            return True

        return False

    def payoff_amount(self, wheel: int, bet: int):
        """ Laskee palautettavan voiton määrän

        Args:
            wheel: pelilinjan arvo
            bet: panoksen määrä

        Returns:
            pelilinjan arvo + 1 kerrottuna panoksella

        """

        return (wheel + 1) * bet

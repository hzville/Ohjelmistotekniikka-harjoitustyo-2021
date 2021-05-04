from tkinter import IntVar
from tkinter.ttk import Label, Button
from wheel import Wheel
from credit import Credit
from payoff_logic import Payoff

class UI:  # pylint: disable=too-many-instance-attributes
    # all instance-attributes are needed to run the show

    def __init__(self, root):
        self.root = root
        self.bet = IntVar()
        self.last_win_amount = IntVar()
        self.last_win_amount.set(0)
        self.bet_list = [1, 2, 5, 10]
        self.credits = Credit()
        self.payoff = Payoff()
        self.first_wheel = Wheel()
        self.second_wheel = Wheel()
        self.third_wheel = Wheel()


    def start(self):
        self.create_labels()
        self.create_buttons()
        self.raise_bet()

    def create_labels(self):
        main_label = Label(master=self.root, text="Fruity Slots", relief="ridge")
        add_credits_label = Label(master=self.root, text="Add credits:", relief="ridge")
        balance_label = Label(master=self.root, text="Balance:", relief="ridge")
        credits_label = Label(master=self.root, textvariable=self.credits.value, relief="ridge")
        bet_label = Label(master=self.root, text="Bet:", relief="ridge")
        bet_amount_label = Label(master=self.root, textvariable=self.bet, relief="ridge")
        last_win_label = Label(master=self.root, text="Last win:", relief="ridge")
        last_win_amount_label = Label(master=self.root, textvariable=self.last_win_amount,
                                      relief="ridge")

        first_wheel_label = Label(
            master=self.root, textvariable=self.first_wheel.display_value,
            anchor="center", relief="ridge")
        second_wheel_label = Label(
            master=self.root, textvariable=self.second_wheel.display_value,
            anchor="center", relief="ridge")
        third_wheel_label = Label(
            master=self.root, textvariable=self.third_wheel.display_value,
            anchor="center", relief="ridge")

        main_label.grid(row=0, column=3, pady=15)
        balance_label.grid(row=1, column=0)
        credits_label.grid(row=1, column=1)
        bet_label.grid(row=2, column=2)
        bet_amount_label.grid(row=2, column=3)
        last_win_label.grid(row=2, column=0)
        last_win_amount_label.grid(row=2, column=1)
        add_credits_label.grid(row=1, column=2)
        first_wheel_label.grid(row=4, column=0, ipadx=15, ipady=15, pady=15)
        second_wheel_label.grid(row=4, column=1, ipadx=15, ipady=15, pady=15)
        third_wheel_label.grid(row=4, column=2, ipadx=15, ipady=15, pady=15)

    def create_buttons(self):
        add_1_credits = Button(master=self.root, text="1€",
                               command=self.credits.add_1_credit)
        add_5_credits = Button(master=self.root, text="5€",
                               command=self.credits.add_5_credit)
        add_10_credits = Button(master=self.root, text="10€",
                                command=self.credits.add_10_credit)

        play_button = Button(master=self.root, text="Play",
                             command=self.play)
        raise_bet_button = Button(master=self.root, text="Raise Bet",
                                  command=self.raise_bet)

        lock_wheel_1_button = Button(master=self.root, text="Lock",
                                     command=self.first_wheel.check_if_locked)
        lock_wheel_2_button = Button(master=self.root, text="Lock",
                                     command=self.second_wheel.check_if_locked)
        lock_wheel_3_button = Button(master=self.root, text="Lock",
                                     command=self.third_wheel.check_if_locked)

        add_1_credits.grid(row=1, column=3)
        add_5_credits.grid(row=1, column=4)
        add_10_credits.grid(row=1, column=5)

        play_button.grid(row=6, column=1)
        raise_bet_button.grid(row=6, column=2)

        lock_wheel_1_button.grid(row=5, column=0)
        lock_wheel_2_button.grid(row=5, column=1)
        lock_wheel_3_button.grid(row=5, column=2)

    def spin_all_wheels(self):
        self.first_wheel.spin()
        self.second_wheel.spin()
        self.third_wheel.spin()

    def raise_bet(self):
        next_bet = self.bet_list.pop(0)
        self.bet.set(next_bet)
        self.bet_list.append(next_bet)

    def play(self):
        if self.credits.value.get() < self.bet.get():
            return False

        self.credits.use_credit(self.bet.get())
        self.spin_all_wheels()
        self.check_for_payoff()
        return True

    def check_for_payoff(self):
        if self.payoff.check_for_win(self.first_wheel.value,
                                     self.second_wheel.value,
                                     self.third_wheel.value):

            payoff_amount = self.payoff.payoff_amount(self.first_wheel.value, self.bet.get())
            self.credits.add_payoff(payoff_amount)
            self.last_win_amount.set(payoff_amount)

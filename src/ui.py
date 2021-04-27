from tkinter import IntVar
from tkinter.ttk import Label, Button
from wheel import Wheel


class UI:  # pylint: disable=too-many-instance-attributes
    # all instance-attributes are needed to run the show

    def __init__(self, root):
        self.root = root
        self.credits = None
        self.bet = None
        self.bet_list = [2, 5, 10, 1]
        self.first_wheel = Wheel()
        self.second_wheel = Wheel()
        self.third_wheel = Wheel()
        self.first_wheel_display_value = IntVar()
        self.second_wheel_display_value = IntVar()
        self.third_wheel_display_value = IntVar()

    def start(self):
        self.initialize_variables()
        self.create_labels()
        self.create_buttons()

    def initialize_variables(self):
        self.credits = IntVar()
        self.credits.set(0)
        self.bet = IntVar()
        self.bet.set(1)
        self.first_wheel_display_value.set(0)
        self.second_wheel_display_value.set(0)
        self.third_wheel_display_value.set(0)

    def create_labels(self):
        main_label = Label(master=self.root, text="Fruity Slots", relief="ridge")
        add_credits_label = Label(master=self.root, text="Add credits:", relief="ridge")
        balance_label = Label(master=self.root, text="Balance:", relief="ridge")
        credits_label = Label(master=self.root, textvariable=self.credits, relief="ridge")
        bet_label = Label(master=self.root, text="Bet:", relief="ridge")
        bet_amount_label = Label(master=self.root, textvariable=self.bet, relief="ridge")

        first_wheel_label = Label(
            master=self.root, textvariable=self.first_wheel_display_value,
            anchor="center", relief="ridge")
        second_wheel_label = Label(
            master=self.root, textvariable=self.second_wheel_display_value,
            anchor="center", relief="ridge")
        third_wheel_label = Label(
            master=self.root, textvariable=self.third_wheel_display_value,
            anchor="center", relief="ridge")

        main_label.grid(row=0, column=3, pady=15)
        balance_label.grid(row=1, column=0)
        credits_label.grid(row=1, column=1)
        bet_label.grid(row=2, column=0)
        bet_amount_label.grid(row=2, column=1)
        add_credits_label.grid(row=1, column=2)
        first_wheel_label.grid(row=3, column=0, ipadx=15, ipady=15, pady=15)
        second_wheel_label.grid(row=3, column=1, ipadx=15, ipady=15, pady=15)
        third_wheel_label.grid(row=3, column=2, ipadx=15, ipady=15, pady=15)

    def create_buttons(self):
        add_1_credits = Button(master=self.root, text="1€",
                               command=self.add_1_credits)
        add_5_credits = Button(master=self.root, text="5€",
                               command=self.add_5_credits)
        add_10_credits = Button(master=self.root, text="10€",
                                command=self.add_10_credits)

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

        play_button.grid(row=5, column=1)
        raise_bet_button.grid(row=5, column=2)

        lock_wheel_1_button.grid(row=4, column=0)
        lock_wheel_2_button.grid(row=4, column=1)
        lock_wheel_3_button.grid(row=4, column=2)

    def add_1_credits(self):
        self.credits.set(self.credits.get() + 1)

    def add_5_credits(self):
        self.credits.set(self.credits.get() + 5)

    def add_10_credits(self):
        self.credits.set(self.credits.get() + 10)

    def use_credits(self, bet: int):
        self.credits.set(self.credits.get() - bet)

    def spin_all_wheels(self):
        self.first_wheel.spin()
        self.second_wheel.spin()
        self.third_wheel.spin()
        self.first_wheel_display_value.set(self.first_wheel.value)
        self.second_wheel_display_value.set(self.second_wheel.value)
        self.third_wheel_display_value.set(self.third_wheel.value)

    def raise_bet(self):
        next_bet = self.bet_list.pop(0)
        self.bet.set(next_bet)
        self.bet_list.append(next_bet)

    def play(self):
        if self.credits.get() < self.bet.get():
            return False

        self.use_credits(self.bet.get())
        self.spin_all_wheels()
        return True

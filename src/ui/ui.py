from tkinter.ttk import Label, Button
from entities.game_logic import GameLogic


class UI:

    def __init__(self, root):
        self.root = root
        self.game_logic = GameLogic()

    def start(self):
        self.create_labels()
        self.create_buttons()
        self.game_logic.start()

    def create_labels(self):
        main_label = Label(master=self.root, text="Fruity Slots", relief="ridge")
        add_credits_label = Label(master=self.root, text="Add credits:", relief="ridge")
        balance_label = Label(master=self.root, text="Balance:", relief="ridge")
        credits_label = Label(master=self.root, textvariable=self.game_logic.credits.value,
                              relief="ridge")
        bet_label = Label(master=self.root, text="Bet:", relief="ridge")
        bet_amount_label = Label(master=self.root, textvariable=self.game_logic.bet,
                                 relief="ridge")
        last_win_label = Label(master=self.root, text="Last win:", relief="ridge")
        last_win_amount_label = Label(master=self.root,
                                      textvariable=self.game_logic.last_win_amount, relief="ridge")

        first_wheel_label = Label(
            master=self.root, textvariable=self.game_logic.first_wheel.display_value,
            anchor="center", relief="ridge")
        second_wheel_label = Label(
            master=self.root, textvariable=self.game_logic.second_wheel.display_value,
            anchor="center", relief="ridge")
        third_wheel_label = Label(
            master=self.root, textvariable=self.game_logic.third_wheel.display_value,
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
                               command=self.game_logic.credits.add_1_credit)
        add_5_credits = Button(master=self.root, text="5€",
                               command=self.game_logic.credits.add_5_credit)
        add_10_credits = Button(master=self.root, text="10€",
                                command=self.game_logic.credits.add_10_credit)

        play_button = Button(master=self.root, text="Play",
                             command=self.game_logic.play)
        raise_bet_button = Button(master=self.root, text="Raise Bet",
                                  command=self.game_logic.raise_bet)
        lock_wheel_1_button = Button(master=self.root, text="Lock",
                                     command=self.game_logic.first_wheel.check_if_locked)
        lock_wheel_2_button = Button(master=self.root, text="Lock",
                                     command=self.game_logic.second_wheel.check_if_locked)
        lock_wheel_3_button = Button(master=self.root, text="Lock",
                                     command=self.game_logic.third_wheel.check_if_locked)

        add_1_credits.grid(row=1, column=3)
        add_5_credits.grid(row=1, column=4)
        add_10_credits.grid(row=1, column=5)

        play_button.grid(row=6, column=1)
        raise_bet_button.grid(row=6, column=2)

        lock_wheel_1_button.grid(row=5, column=0)
        lock_wheel_2_button.grid(row=5, column=1)
        lock_wheel_3_button.grid(row=5, column=2)

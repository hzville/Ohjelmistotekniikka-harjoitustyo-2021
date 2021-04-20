from tkinter import Tk, IntVar, W, E
from tkinter.ttk import Button, Label
from wheel import Wheel


class UI:

    def __init__(self, root):
        self.root = root
        self.coin = None
        self.first_wheel = Wheel()
        self.first_wheel_display_value = None
        self.second_wheel = Wheel()
        self.second_wheel_display_value = None
        self.third_wheel = Wheel()
        self.third_wheel_display_value = None

    def start(self):
        self.initialize_variables()
        self.create_labels()
        self.create_buttons()
        self.root.grid_columnconfigure(0, weight=1)

    def create_labels(self):
        main_label = Label(master=self.root, text="Fruity Slots")
        add_coin_label = Label(master=self.root, text="Add coins:")
        balance_label = Label(master=self.root, text="Balance:")
        coin_label = Label(master=self.root, textvariable=self.coin)
        first_wheel_label = Label(
            master=self.root, textvariable=self.first_wheel_display_value)
        second_wheel_label = Label(
            master=self.root, textvariable=self.second_wheel_display_value)
        third_wheel_label = Label(
            master=self.root, textvariable=self.third_wheel_display_value)

        main_label.grid(row=0, column=0, sticky=E)
        balance_label.grid(row=1, column=0, sticky=W)
        coin_label.grid(row=1, column=1, sticky=W)
        add_coin_label.grid(row=1, column=2, sticky=E)
        first_wheel_label.grid(row=2, column=0)
        second_wheel_label.grid(row=2, column=1)
        third_wheel_label.grid(row=2, column=2)

    def create_buttons(self):
        add_1_coin = Button(master=self.root, text="1€",
                            command=self.add_1_coin)
        add_5_coin = Button(master=self.root, text="5€",
                            command=self.add_5_coin)
        add_10_coin = Button(master=self.root, text="10€",
                             command=self.add_10_coin)
        play_button = Button(master=self.root, text="Play!",
                             command=self.spin_all_wheels)
        add_1_coin.grid(row=1, column=3, sticky=E)
        add_5_coin.grid(row=1, column=4, sticky=E)
        add_10_coin.grid(row=1, column=5, sticky=E)
        play_button.grid(row=3, column=1, sticky=E)

    def initialize_variables(self):
        self.coin = IntVar()
        self.coin.set(0)
        self.first_wheel_display_value = IntVar()
        self.first_wheel_display_value.set(0)
        self.second_wheel_display_value = IntVar()
        self.second_wheel_display_value.set(0)
        self.third_wheel_display_value = IntVar()
        self.third_wheel_display_value.set(0)

    def add_1_coin(self):
        self.coin.set(self.coin.get() + 1)

    def add_5_coin(self):
        self.coin.set(self.coin.get() + 5)

    def add_10_coin(self):
        self.coin.set(self.coin.get() + 10)

    def spin_all_wheels(self):
        self.first_wheel.spin()
        self.second_wheel.spin()
        self.third_wheel.spin()
        self.first_wheel_display_value.set(self.first_wheel.value)
        self.second_wheel_display_value.set(self.second_wheel.value)
        self.third_wheel_display_value.set(self.third_wheel.value)


if __name__ == "__main__":
    window = Tk()
    window.geometry("500x500")
    window.title("SlotsGame")
    ui = UI(window)
    ui.start()
    window.mainloop()

from tkinter import *
from tkinter.ttk import *


class UI:

    def __init__(self, root):
        self.root = root
        self.coin = None

    def start(self):
        self.coin = IntVar()
        self.coin.set(0)

        main_label = Label(master=self.root, text="Fruity Slots")
        add_coin_label = Label(master=self.root, text="Add coins:")
        balance_label = Label(master=self.root, text="Balance:")
        coin_label = Label(master=self.root, textvariable=self.coin)
        add_1_coin = Button(master=self.root, text="1€", command=self.add_1_coin)
        add_5_coin = Button(master=self.root, text="5€", command=self.add_5_coin)
        add_10_coin = Button(master=self.root, text="10€", command=self.add_10_coin)
        play_button = Button(master=self.root, text="Play!")

        main_label.grid(row=0, column=0, sticky=E)
        balance_label.grid(row=1, column=0, sticky=W)
        coin_label.grid(row=1, column=1, sticky=W)
        add_coin_label.grid(row=1, column=2, sticky=E)
        add_1_coin.grid(row=1, column=3, sticky=E)
        add_5_coin.grid(row=1, column=4, sticky=E)
        add_10_coin.grid(row=1, column=5, sticky=E)
        play_button.grid(row=2, column=1, sticky=E)
        self.root.grid_columnconfigure(0, weight=1)

    def add_1_coin(self):
        self.coin.set(self.coin.get() + 1)

    def add_5_coin(self):
        self.coin.set(self.coin.get() + 5)

    def add_10_coin(self):
        self.coin.set(self.coin.get() + 10)


if __name__ == "__main__":
    window = Tk()
    window.geometry("500x500")
    window.title("SlotsGame")
    ui = UI(window)
    ui.start()
    window.mainloop()


from tkinter import Tk
from ui import UI


def main():
    window = Tk()
    window.geometry("450x400")
    window.title("Fruity Slots")
    ui = UI(window)     # pylint: disable=invalid-name
    ui.start()
    window.mainloop()


if __name__ == "__main__":
    main()

from tkinter import *
from tkinter.messagebox import *

root = Tk()
root.geometry('230x300+0+0')

empty_grid = ["", "", "", "", "", "", "", "", ""]
step = 1


class Field:
    def __init__(self, value):
        self.values = value
        self.btn1 = Button(root, width=8, height=4, text=self.values[0], command=lambda: self.action(0))
        self.btn1.grid(row=0, column=0, padx=5, pady=5)
        self.btn2 = Button(root, width=8, height=4, text=self.values[1], command=lambda: self.action(1))
        self.btn2.grid(row=0, column=1, padx=5, pady=5)
        self.btn3 = Button(root, width=8, height=4, text=self.values[2], command=lambda: self.action(2))
        self.btn3.grid(row=0, column=2, padx=5, pady=5)

        self.btn4 = Button(root, width=8, height=4, text=self.values[3], command=lambda: self.action(3))
        self.btn4.grid(row=1, column=0, padx=5, pady=5)
        self.btn5 = Button(root, width=8, height=4, text=self.values[4], command=lambda: self.action(4))
        self.btn5.grid(row=1, column=1, padx=5, pady=5)
        self.btn6 = Button(root, width=8, height=4, text=self.values[5], command=lambda: self.action(5))
        self.btn6.grid(row=1, column=2, padx=5, pady=5)

        self.btn7 = Button(root, width=8, height=4, text=self.values[6], command=lambda: self.action(6))
        self.btn7.grid(row=2, column=0, padx=5, pady=5)
        self.btn8 = Button(root, width=8, height=4, text=self.values[7], command=lambda: self.action(7))
        self.btn8.grid(row=2, column=1, padx=5, pady=5)
        self.btn9 = Button(root, width=8, height=4, text=self.values[8], command=lambda: self.action(8))
        self.btn9.grid(row=2, column=2, padx=5, pady=5)

    def action(self, number):
        if self.values[number] != "":
            Field(self.values)
        else:
            global step
            if step == 1:
                self.values[number] = "X"
                step = 2
            elif step == 2:
                self.values[number] = "0"
                step = 1

            Field(self.values)
            win = self.check(self.values)
            if win != 0:
                if win == 3:
                    showinfo("Game Over", "DRAW")
                else:
                    showinfo("Game Over", "Player %d win" % win)
                step = 1
                Field(["", "", "", "", "", "", "", "", ""])

    def check(self, values):
        if values[0] == values[1] == values[2] == "X" or values[3] == values[4] == values[5] == "X" \
                or values[6] == values[7] == values[8] == "X" or values[0] == values[3] == values[6] == "X"\
                or values[1] == values[4] == values[7] == "X" or values[2] == values[5] == values[8] == "X"\
                or values[0] == values[4] == values[8] == "X" or values[2] == values[4] == values[6] == "X":
            return 1
        if values[0] == values[1] == values[2] == "0" or values[3] == values[4] == values[5] == "0" \
                or values[6] == values[7] == values[8] == "0" or values[0] == values[3] == values[6] == "0"\
                or values[1] == values[4] == values[7] == "0" or values[2] == values[5] == values[8] == "0"\
                or values[0] == values[4] == values[8] == "0" or values[2] == values[4] == values[6] == "0":
            return 2
        if "" not in values:
            return 3
        return 0


if __name__ == "__main__":
    Field(empty_grid)

root.mainloop()

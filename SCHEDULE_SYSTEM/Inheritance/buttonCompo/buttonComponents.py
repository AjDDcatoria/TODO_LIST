from tkinter import*

class Buttons:
    def __init__(self, root, ButtonLabel, buttonCommand, buttonx, buttony):
        self.mylabels = Button(root, text = ButtonLabel , command = buttonCommand)
        self.mylabels.place(x = buttonx, y = buttony)
        
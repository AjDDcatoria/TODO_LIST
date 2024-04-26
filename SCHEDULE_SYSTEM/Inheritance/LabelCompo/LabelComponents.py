from tkinter import*

class Labels:
    def __init__(self, root, textLabel, Labelx, Labely, Labelbg):
        self.mylabels = Label(root, text = textLabel, bg=Labelbg)
        self.mylabels.place(x = Labelx, y = Labely)
        
        

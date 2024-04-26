from tkinter import*
from tkinter.ttk import Combobox

class Entries:
    def __init__(self, root, entryWidth, entryx, entryY):
        self.myEntry = Entry(root, width=entryWidth)
        self.myEntry.place(x=entryx, y=entryY)
        
    # def get(self):
    #     return self.myEntry.get()
        
class comboBoxes:
    def __init__(self, root, comboValues, comboWidth, combox, comboy):
        self.myComboBox = Combobox(root, values = comboValues, width=comboWidth)       
        self.myComboBox.place(x=combox, y=comboy)
        self.myComboBox.set("Select")
        
    def get(self):
        return self.myComboBox.get()
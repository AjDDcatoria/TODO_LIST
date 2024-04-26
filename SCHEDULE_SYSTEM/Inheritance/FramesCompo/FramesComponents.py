from tkinter import*

class ExternalFrames:
    
    def __init__(self, root, frameWidth, frameHeight, frameRow, frameColumn, frameBg):
        
        self.exFrames = Frame(root, width = frameWidth, height = frameHeight, bg=frameBg)
        self.exFrames.grid(row=frameRow, column=frameColumn)
          
        
class InternalFrames:
    def __init__(self, exFrames, frameText, frameWidth, frameHeight, framex, framey, frameBg):
        self.myFrames = LabelFrame(exFrames, text = frameText, width = frameWidth, height = frameHeight, bg = frameBg)
        self.myFrames.place(x=framex, y=framey)
        
class frame2Components:
    def __init__(self, myFrames, listWidth, listHeight, listPadx, listPady):
        self.mylist = Listbox(myFrames, width=listWidth, height=listHeight)
        self.mylist.place(x=listPadx, y=listPady)
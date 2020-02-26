import tkinter as tk
from tkinter import *

root = tk.Tk()

root.geometry('800x730+0+0')
root.title('Photo Viewer')


class ImageViewer(Frame):
    def __init__(self, master):
        Frame.__init__(self,master)
        self.master = master

        self.ViewerFrame = Frame(self.master, bd = 0, bg = 'gray10', height = 670)
        self.ViewerFrame.pack(side = TOP, fill = BOTH, expand = True)

        self.NextButton = Button(self.master, bd = 0, text = '>', font = ('impact',25),activeforeground = 'black',fg = 'white',bg = 'gray15')
        self.NextButton.pack(side = RIGHT, expand = True, fill = X)
        #self.NextButton.bind('<Button-1>', self.nextButton)

        self.Zoom = Button(self.master, bd = 0, text = '+', font = ('impact',25), activeforeground = 'black',fg = 'white',bg = 'gray15')
        self.Zoom.pack(side = RIGHT, expand = True, fill = X)
        #self.Zoom.bind('<Button-1>', self.zoomButton)

        self.PrevButton = Button(self.master, bd = 0, text = '<', font = ('impact',25), activeforeground = 'black',fg = 'white', bg = 'gray15')
        self.PrevButton.pack(side = RIGHT, expand = True, fill = X)
        #self.PrevButton.bind('<Button-1>',self.prevButton)

    def nextButton(self,evt):
        pass

    def zoomButton(self,evt):
        pass

    def prevButton(self,evt):
        pass

app = ImageViewer(root).pack()

root.mainloop()

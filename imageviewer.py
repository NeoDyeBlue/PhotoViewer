import tkinter as tk
from tkinter import *
import os

root = tk.Tk()

root.geometry('800x730+0+0')
root.title('Photo Viewer')
root.config(bg = 'gray10')


class ImageViewer(Frame):
    def __init__(self, master):
        Frame.__init__(self,master)
        self.master = master

        self.Folderchoose = Frame(self.master, bg = 'gray25', height = 50, width = 400)
        self.Folderchoose.pack(side = TOP, fill = X)

        self.foldr = Button(self.Folderchoose, text = ' 🗀', font = ('impact', 20), fg = 'white', bg = 'gray25',
                            activeforeground = 'black', activebackground = 'gray', borderwidth = 0, anchor = W)
        self.foldr.pack(side = LEFT, fill = X, expand = True)

        self.FileName = Frame(self.Folderchoose, bg = 'gray15', height = 50, width = 1000)
        self.FileName.place(x = 400, y = 0)

        self.ViewerFrame = Frame(self.master, bd = 0, bg = 'gray5', height = 700)
        self.ViewerFrame.pack(side = TOP, fill = BOTH, expand = True)

        self.Thumbnails = Frame(self.ViewerFrame, bd = 0, bg = 'gray10')
        self.Thumbnails.pack(side = TOP, fill = BOTH, expand = True)

        self.ThumbSB = Scrollbar(self.Thumbnails, orient = VERTICAL)
        self.ThumbSB.pack(side = RIGHT, fill = Y)

        self.NextButton = Button(self.master, bd = 0, text = '>', font = ('impact',25),activeforeground = 'black',
                                 fg = 'gray',bg = 'gray15', activebackground = 'gray20')
        self.NextButton.pack(side = RIGHT, expand = True, fill = X)

        self.Zoom = Button(self.master, bd = 0, text = '+', font = ('impact',25), activeforeground = 'black',
                           fg = 'gray',bg = 'gray15', activebackground = 'gray20')
        self.Zoom.pack(side = RIGHT, expand = True, fill = X)

        self.PrevButton = Button(self.master, bd = 0, text = '<', font = ('impact',25), activeforeground = 'black',
                                 fg = 'gray', bg = 'gray15', activebackground = 'gray20')
        self.PrevButton.pack(side = RIGHT, expand = True, fill = X)

    def nextButton(self):
        pass

    def zoomButton(self):
        pass

    def prevButton(self):
        pass

app = ImageViewer(root).pack()

root.mainloop()

import tkinter as tk
from tkinter import *
from tkinter import filedialog
from PIL import ImageTk, Image
import os

root = tk.Tk()

root.geometry('800x730+0+0')
root.title('Photo Viewer')
root.config(bg = 'gray10')

class ImageViewer(Frame):
    def __init__(self, master):
        Frame.__init__(self,master)
        self.master = master
        self.filetypes = ('.jpg','.jpeg','.png','.gif')
        self.images = list()

        self.ROW = 0
        self.COL = 0
        self.BUTTONCOUNT = 0

        self.ViewerFrame = Frame(self.master, bd = 0, bg = 'gray5', height = 700)
        self.ViewerFrame.pack(side = TOP, fill = BOTH, expand = True)

        self.Thumbnails = Frame(self.ViewerFrame, bd = 0, bg = 'gray10')
        self.Thumbnails.pack(side = TOP, fill = BOTH, expand = True)

        self.Folderchoose = Frame(self.master, bg = 'gray25', height = 50, width = 400)
        self.Folderchoose.pack(side = TOP, fill = X)

        self.foldr = Button(self.Folderchoose, text = '                    🗀', font = ('calibri', 20), fg = 'white', 
                            bg = 'gray25',activeforeground = 'black', activebackground = 'gray40', borderwidth = 0, anchor = W,
                            command = self.FolderOpen)
        self.foldr.pack(side = LEFT, fill = X, expand = True)

        self.FileName = Frame(self.Folderchoose,bd = 0, bg = 'gray5', height = 50, width = 1120)
        self.FileName.place(x = 280, y = 5)

        self.NextButton = Button(self.master, bd = 0, text = '>', font = ('impact',18),activeforeground = 'white',
                                 fg = 'gray',bg = 'gray15', activebackground = 'gray15')
        self.NextButton.pack(side = RIGHT, expand = True, fill = X)


        self.PrevButton = Button(self.master, bd = 0, text = '<', font = ('impact',18), activeforeground = 'white',
                                 fg = 'gray', bg = 'gray15', activebackground = 'gray15')
        self.PrevButton.pack(side = RIGHT, expand = True, fill = X)

    def FolderOpen(self):
        self.FolderOP = filedialog.askdirectory()

    def nextButton(self):
        pass

    def zoomButton(self):
        pass

    def prevButton(self):
        pass

app = ImageViewer(root).pack()

root.mainloop()

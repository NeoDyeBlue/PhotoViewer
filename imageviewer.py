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
        self.w = 0
        self.h = 0
        self.resolution = None

        self.Imageviewer = Frame(self.master, bd = 0, bg = 'gray', height = 640)
        self.Imageviewer.pack(side = TOP, fill = BOTH, expand = True)

        self.FileName = Frame(self.master,bd = 0, bg = 'gray5', height = 50, width = 1120)
        self.FileName.pack(side = TOP, fill = BOTH, expand = True)

        self.FilenameLabel = Label(self.FileName, text = '     File name: ', bg = 'gray5', fg = 'gray', font = ('calibri',11),
                                   anchor = W)
        self.FilenameLabel.pack(side = LEFT,fill = X, expand = True)

        self.foldr = Button(self.master, text = '🗀', font = ('calibri', 20), fg = 'white', 
                            bg = 'gray10',activeforeground = 'black', activebackground = 'lightgray', borderwidth = 0,
                            command = self.FolderOpen)
        self.foldr.pack(side = LEFT, fill = X, expand = True)

        self.NextButton = Button(self.master, bd = 0, text = '>', font = ('impact',20),activeforeground = 'white',
                                 fg = 'gray',bg = 'gray15', activebackground = 'gray15')
        self.NextButton.pack(side = RIGHT, expand = True, fill = X)


        self.PrevButton = Button(self.master, bd = 0, text = '<', font = ('impact',20), activeforeground = 'white',
                                 fg = 'gray', bg = 'gray15', activebackground = 'gray15')
        self.PrevButton.pack(side = RIGHT, expand = True, fill = X)

    def FolderOpen(self):
        self.FolderOP = filedialog.askdirectory()

        for i in os.listdir(self.FolderOP):
            if i.endswith(self.filetypes):
                self.images.append(i)

        self.firstimg = ("{0}/{1}".format(self.FolderOP, self.images[0]))
        self.img = Image.open(self.firstimg)
        self.w,self.h = self.img.size

        if self.w == self.h:
            self.resolution = (640,640)
        elif self.w > self.h:
            self.resolution = (1150,640)
        elif self.w < self.h:
            self.resolution = (440,640)

        self.img = self.img.resize(self.resolution, Image.ANTIALIAS)

        self.img = ImageTk.PhotoImage(self.img)

        self.imgview = Label(self.Imageviewer, image = self.img, bg = 'gray') 
      
        self.imgview.image = self.img 
        self.imgview.pack(side = TOP, fill = BOTH, expand = True)

        self.FilenameLabel.config(text = '     File Name: {0}'.format(self.images[0]))        

    def nextButton(self):
        pass

    def prevButton(self):
        pass

app = ImageViewer(root).pack()

root.mainloop()

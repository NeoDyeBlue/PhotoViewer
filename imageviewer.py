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
        self.BUTTONS = list()
        self.filetypes = ('.jpg','.jpeg','.png','.gif')
        self.images = list()
        self.w = 0
        self.h = 0
        self.imgindex = 0
        self.resolution = None
        self.imgview = Label()

        self.Imageviewer = Frame(self.master, bd = 0, bg = 'gray', height = 635)
        self.Imageviewer.pack(side = TOP, fill = BOTH, expand = True)

        self.Showhow = Label(self.Imageviewer, bg = 'gray',fg = 'white', text = 'Please choose a folder first to view its image files.',
                             font =('calibri', 11), height = 35, justify = CENTER)
        self.Showhow.pack(fill = BOTH, expand = True)

        self.FileName = Frame(self.master,bd = 0, bg = 'gray5', height = 50, width = 1120)
        self.FileName.pack(side = TOP, fill = BOTH, expand = True)

        self.FilenameLabel = Label(self.FileName, bg = 'gray5', fg = 'gray', font = ('calibri',11),
                                   anchor = W)
        self.FilenameLabel.pack(side = LEFT,fill = X, expand = True)

        self.foldr = Button(self.master, text = '🗀', font = ('calibri', 20), fg = 'white', 
                            bg = 'gray10',activeforeground = 'black', activebackground = 'gray20', borderwidth = 0,
                            command = self.FolderOpen)
        self.foldr.pack(side = LEFT, fill = X, expand = True)

        self.NextButton = Button(self.master, bd = 0, text = '>', font = ('impact',20),activeforeground = 'white',
                                 fg = 'gray',bg = 'gray15', activebackground = 'gray15', command = self.nextButton,
                                 state = DISABLED)
        self.NextButton.pack(side = RIGHT, expand = True, fill = X)


        self.PrevButton = Button(self.master, bd = 0, text = '<', font = ('impact',20), activeforeground = 'white',
                                 fg = 'gray', bg = 'gray15', activebackground = 'gray15', command = self.prevButton,
                                 state = DISABLED)
        self.PrevButton.pack(side = RIGHT, expand = True, fill = X)

        self.BUTTONS.append(self.PrevButton)
        self.BUTTONS.append(self.NextButton)

    def Viewimages(self):
        if self.imgindex == len(self.images):
            self.imgindex = 0
        elif self.imgindex == -1:
            self.imgindex += len(self.images)

        self.Showhow.pack_forget()
        self.view_img = ("{0}/{1}".format(self.FolderOP, self.images[self.imgindex]))
        self.img = Image.open(self.view_img)
        self.w,self.h = self.img.size

        if self.w == self.h:
            self.resolution = (633,633)
        elif self.w > self.h:
            self.resolution = (1137,633)
        elif self.w < self.h:
            self.resolution = (437,633)

        self.img = self.img.resize(self.resolution, Image.ANTIALIAS)

        self.img = ImageTk.PhotoImage(self.img)

        self.imgview = Label(self.Imageviewer, image = self.img, bg = 'gray') 
      
        self.imgview.image = self.img 
        self.imgview.pack(side = TOP, fill = BOTH, expand = True)

        self.FilenameLabel.config(text = '     {0}'.format(self.images[self.imgindex]))        

    def nextButton(self):
        self.imgview.pack_forget()
        self.imgindex += 1
        self.Viewimages()

    def nextEvent(self, event):
        self.imgview.pack_forget()
        self.imgindex += 1
        self.Viewimages()

    def prevButton(self):
        self.imgview.pack_forget()
        self.imgindex -= 1
        self.Viewimages()

    def prevEvent(self, event):
        self.imgview.pack_forget()
        self.imgindex -= 1
        self.Viewimages()

    def FolderOpen(self):
        self.imgindex = 0
        self.images.clear()
        self.imgview.pack_forget()
        self.FilenameLabel.config(text = '')
        self.FolderOP = filedialog.askdirectory()

        if not self.FolderOP:
            self.Showhow.config(text = 'Please choose a folder first to view its image files.')
            self.Showhow.pack(fill = BOTH, expand = True)
            self.foldr.config(fg = 'white')
            self.master.unbind('<Right>')
            self.master.unbind('<Left>')
            for y in self.BUTTONS:
                y.config(state = DISABLED)
        else:
            for i in os.listdir(self.FolderOP):
                if i.endswith(self.filetypes):
                    self.foldr.config(fg = 'cyan')
                    self.images.append(i)

            if len(self.images) == 0:
                self.Showhow.config(text = ('{0}\nFolder does not contain any valid image files.'.format(self.FolderOP)))
                self.Showhow.pack(fill = BOTH, expand = True)
                self.foldr.config(fg = 'white')
                self.master.unbind('<Right>')
                self.master.unbind('<Left>')
                for y in self.BUTTONS:
                    y.config(state = DISABLED)
            else:
                self.master.bind('<Right>', self.nextEvent)
                self.master.bind('<Left>', self.prevEvent)
                for y in self.BUTTONS:
                    y.config(state = NORMAL)
                self.Viewimages()

app = ImageViewer(root).pack()

root.mainloop()

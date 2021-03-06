#! /usr/bin/env python
# -*- coding: utf-8 -*-
import os
import shutil
from Tkinter import *
import tkFileDialog as filedialog
import tkMessageBox as mb

class Block:
    def __init__(self, master):
        self.e = Button(master, text="Choose build directory")
        self.b = Button(master, text="Copy build files")
        self.t = Text(master, width=50, height=30, bg="white", fg='black', wrap=WORD)
        self.e.pack()
        self.b.pack()
        self.t.pack()


    def setFunc(self, func_B, func_E):
        self.b['command'] = eval('self.' + func_B)
        self.e['command'] = eval('self.' + func_E)

    def modal(self):
        answer = mb.askyesno(title="Папка выбрана правильно?", message="Копировать билд из директории?")
        if answer == True:
            self.copy()

    def builddirchoose(self):
        self.builddir = filedialog.askdirectory(initialdir = "E:/Downloads/111")
        self.t.insert(END, 'Choosen build directory: ' + self.builddir + '\n')

    def copy(self):
        builddir = self.builddir.replace("\\", "/")
        newdir = builddir.replace(r'E:/Downloads/111/', '')
        newdir = newdir.replace('by_Freeman_Gordon', '_pkg')
        copydir = r'E:/builds/'
        createdir = os.path.join(copydir, newdir)
        os.mkdir(createdir)
        while len(os.listdir(createdir)) != 7:
            for file in os.listdir(builddir):
                currentFile = os.path.join(builddir, file)
                if file.endswith(".mp4") and os.path.getsize(currentFile) > 65000000 \
                    or file.endswith(".pdf") and os.path.getsize(currentFile) > 200000 \
                    or file.endswith(".jpg") and os.path.getsize(currentFile) > 800000:
                        if os.path.exists(createdir + file) == 0:
                            self.t.insert(END, 'Copyng ' + file + '\n')
                            shutil.copy(currentFile, createdir)
                            self.t.insert(END, file + ' copyed!' + '\n')

        else:
            self.t.insert(END, 'Build and exe are copyed!' + '\n')

root = Tk()
root.title("Builder Copy")

first_block = Block(root)
first_block.setFunc('modal', 'builddirchoose')

root.mainloop()

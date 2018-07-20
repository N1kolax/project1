#! /usr/bin/env python
# -*- coding: utf-8 -*-
import os
import shutil
from Tkinter import *
import tkFileDialog as filedialog
import tkMessageBox as mb
import ttk
import time


class Block:
    def __init__(self, master):
        self.chm = Button(master, text="Сhoose build manual")
        self.sflbps4 = Button(master, text="Search for a last PS4 build")
        self.sflbxbox = Button(master, text="Search for a last XBOX build")
        self.ctl = Button(master, text="Copy build to local")
        self.stu = Button(master, text="Share build to U")
        self.t = Text(master, bg="white", fg='black', wrap=WORD)
        self.progressVar = IntVar()
        self.pb = ttk.Progressbar(length=250, variable=self.progressVar, maximum=100)
        self.sflbps4.grid(row=0, column=1)
        self.chm.grid(row=0, column=2, pady=10)
        self.sflbxbox.grid(row=0, column=3)
        self.ctl.grid(row=1, column=1)
        self.pb.grid(row=1, column=2, pady=10)
        self.stu.grid(row=1, column=3)
        self.t.grid(row=2, rowspan=4, column=1, columnspan=3)

    def setFunc(self, func_chm, func_sflbps4, func_sflbxbox, func_ctl, func_stu):
        self.chm['command'] = eval('self.' + func_chm)
        self.sflbps4['command'] = eval('self.' + func_sflbps4)
        self.sflbxbox['command'] = eval('self.' + func_sflbxbox)
        self.ctl['command'] = eval('self.' + func_ctl)
        self.stu['command'] = eval('self.' + func_stu)

    def builddirchoose(self):
        self.builddir = filedialog.askdirectory(initialdir="E:/Downloads/111")
        self.t.insert(END, 'Choosen build directory: ' + self.builddir + '\n')

    def search_for_last_ps4(self):
        path = r'E:\Downloads\builds_ps4_and_xbox\PS4'
        self.scan_for_new_build(path)

    def search_for_last_xbox(self):
        path = r'E:\Downloads\builds_ps4_and_xbox\XBOX'
        self.scan_for_new_build(path)

    def scan_for_new_build(self, path):
        build_list = [os.path.join(path, x) for x in os.listdir(path)]
        if build_list:
            date_list = [[x, os.path.getmtime(x)] for x in build_list]
            sort_date_list = sorted(date_list, key=lambda x: x[1], reverse=True)
            self.builddir = (sort_date_list[0][0])
            self.t.insert(END, 'Choosen build directory: ' + self.builddir + '\n')

    def modal(self):
        answer = mb.askyesno(title="Is the folder selected correctly?", message="Copy build to local disk?")
        if answer == True:
            self.copy_to_local()

    def copy_to_local(self):
        src = self.builddir
        dst = self.builddir.split('\\')[4]
        dst = os.path.join(r'E:\builds', dst)
        self.copy_function(src, dst)
        self.t.insert(END, 'Build copyed! Time to wrap up this shit!' + '\n')
        self.dst = dst

    def share_to_U(self):
        newname = self.builddir.split('\\')[4]
        newname = newname.split('_Dark')[0]
        newnamedir = os.path.join('D:\\buildsPKG', newname)
        path = self.dst
        self.scan_for_new_build(path)
        src = self.builddir
        newlastdir = self.builddir.split('\\')[3]
        dst = os.path.join(newnamedir, newlastdir)
        if not os.path.exists(dst):
            os.makedirs(dst)
        self.copy_function(src, dst)
        self.t.insert(END, 'Build shared to U!' + '\n')

    def copy_function(self, src, dst):
        countFiles = 0
        for path, dirs, filenames in os.walk(src):
            countFiles = countFiles + len(filenames)
        self.pb['maximum'] = countFiles
        self.progressVar.set(0)
        for path, dirs, filenames in os.walk(src):
            for directory in dirs:
                srcPath = os.path.join(path, directory)
                dstPath = srcPath.replace(src, dst)
                if not os.path.exists(dstPath):
                    os.makedirs(dstPath)
            for fileName in filenames:
                srcPath = os.path.join(path, fileName)
                dstPath = srcPath.replace(src, dst)
                if not os.path.exists(dstPath):
                    self.t.insert(END, 'Copyng ' + fileName + '\n')
                    shutil.copy(srcPath, dstPath)
                self.incPB()

    def incPB(self):
        self.progressVar.set(self.progressVar.get() + 1)
        self.pb.update()

root = Tk()
root.title("Builder Copy")

first_block = Block(root)
first_block.setFunc('builddirchoose', 'search_for_last_ps4', 'search_for_last_xbox', 'modal', 'share_to_U')

root.mainloop()

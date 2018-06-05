#! /usr/bin/env python
# -*- coding: utf-8 -*-
import os
import shutil
import sys

builddir = sys.argv[1]
copydir = sys.argv[2]
newdir = str(builddir.replace('by_Freeman_Gordon', 'pkg'))
newdir = str(newdir.replace('E:\Downloads', ''))
os.mkdir(copydir + newdir)

def check():
    for file in os.listdir(builddir):
        currentFile = os.path.join(builddir, file)
        if file.endswith(".mp4") and os.path.getsize(currentFile) > 65000000\
        or file.endswith(".pdf") and os.path.getsize(currentFile) > 200000\
        or file.endswith(".jpg") and os.path.getsize(currentFile) > 16000000:
            if os.path.exists(copydir + str(newdir) + '/' + file == 0):
                shutil.copy(currentFile, copydir + str(newdir))

while len(os.listdir(copydir + newdir)) != 6:
    check()
else:
    print('Билдец и exe скопировались, работаем!')
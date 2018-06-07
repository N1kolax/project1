#GoodJob
#! /usr/bin/env python
# -*- coding: utf-8 -*-
import os
import shutil
import sys

builddir =  sys.argv[1].replace("\\", "/")
copydir = r'E:/builds/'
newdir = builddir.replace(r'E:/Downloads/', '')
newdir = newdir.replace('by_Freeman_Gordon', '_pkg')
createdir = os.path.join(copydir, newdir)
os.mkdir(createdir)

def check():
    for file in os.listdir(builddir):
        currentFile = os.path.join(builddir, file)
        if file.endswith(".mp4") and os.path.getsize(currentFile) > 65000000\
        or file.endswith(".pdf") and os.path.getsize(currentFile) > 200000\
        or file.endswith(".jpg") and os.path.getsize(currentFile) > 16000000:
            if os.path.exists(createdir + file) == 0:
                print('Copyng ' + file)
                shutil.copy(currentFile, createdir)
                print(file + ' copyed!')

while len(os.listdir(createdir)) != 6:
    check()
else:
    print('Build and exe are copyed!')
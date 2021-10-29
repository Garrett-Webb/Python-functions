import os
from os import listdir, walk
from os.path import isfile, join
from tkinter import Tk
from tkinter.filedialog import askdirectory

numlines = 0
file_extensions = [".c", ".cpp", ".h", ".rc"]

def rawcount(f):
    lines = 0
    buf_size = 1024 * 1024
    read_f = f.raw.read
    buf = read_f(buf_size)
    while buf:
        lines += buf.count(b'\n')
        buf = read_f(buf_size)
    return lines


path = askdirectory(title='Select Folder') # shows dialog box and return the path
print(path)

onlyfiles = [f for f in listdir(path) if isfile(join(path, f))]
#print(onlyfiles)
for root, dirs, files in os.walk(path):
    for file in files:
        split_tup = os.path.splitext(file)
        if (split_tup[1] in file_extensions):
            with open(os.path.join(root, file), "rb") as auto:
            #with open(os.path.join(path, file), "rb") as auto:
            #print(file)
                lines = rawcount(auto)
                numlines += lines
                print("lines in",file, ":", lines)

print("Total lines :", numlines)


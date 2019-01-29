#!usr/bin/python3
import sys

def isWhiteLine(x):
    return x.isspace()

file = sys.argv[0]
f_obj = open(file, "r")
for i in f_obj:
    if (isWhiteLine(i) == False):
        print(str(i).strip())
f_obj.close()
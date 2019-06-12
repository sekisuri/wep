#!/usr/local/bin/python3
import sys
import re
import os

def rename_file():
    for filename in os.listdir("."):
        if filename.endswith("mkv"):
            newname = filename.replace("Keroro Gunso ","")
            os.rename(filename,newname)
            #print(newname)


if __name__ == "__main__":
    rename_file()

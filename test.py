#!/usr/bin/python
from os.path import expanduser
from Tkinter import *

import os
import time

window = Tk()
window.title("ASTRO PI4 SETUP")
window.geometry('350x200')
lbl = Label(window, text="STEP1")
lbl.grid(column=0, row=1)

def click_1():
    time.sleep(2)
    b1["state"] = "disabled"
    if b1["state"] == "disabled":
            os.system('sudo apt update')
            os.system('sudo apt install indi-full kstars-bleeding -y')
            os.system('sudo apt install gsc -y')
            os.system('sudo apt install notepad-plus-plus -y')          
            b1.configure(text="Compeleted !!")
    else:
        b1["state"] = "normal"
    
b1 = Button(window, text="Install KSTARS/INDI", command=click_1)
b1.grid(column=3, row=1)
 
lbl2 = Label(window, text="STEP2")
lbl2.grid(column=0, row=2)

def click_2():
    time.sleep(2)
    b2["state"] = "disabled"
    if b2["state"] == "disabled":
            os.system('sudo apt update')
            os.system('sudo apt install indi-full kstars-bleeding -y')
            os.system('sudo apt install gsc -y')
            os.system('sudo apt install notepad-plus-plus -y')          
            b2.configure(text="Compeleted !!")
    else:
        b2["state"] = "normal"
    
b2 = Button(window, text="Install ASTROMETRY", command=click_2)
b2.grid(column=3, row=2)

b10 = Button(window, text= "Exit", command=window.destroy)
b10.grid(column=0, row=3)

window.mainloop()

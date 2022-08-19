import energy_dissipation as e
import acceleration as a
import matplotlib.pyplot as plt
import numpy as np
import os
from tkinter import *


def set_value(value):
    global savefig
    savefig = value

savefig = False

gui = Tk(className= 'Save plots as PDF?')
gui.geometry("300x190")
pixelVirtual = PhotoImage(width=1, height=1)

Button(gui, text='Save all plots',command=lambda *args: set_value(True), bg='#9BFF75', fg='black', image=pixelVirtual, width=200, height=50, compound="c").pack()
Button(gui, text='Do not save',command=lambda *args: set_value(False), bg='#FF8E75', fg='black', image=pixelVirtual, width=200, height=50, compound="c") .pack()
Button(gui, text='Confirm (default is no)',command=gui.destroy, image=pixelVirtual, width=200, height=50, compound="c").pack()

mainloop()




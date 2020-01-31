import pyfirmata
import time
from tkinter import *
from tkinter.ttk import *
board = pyfirmata.Arduino("/dev/cu.usbmodem14201")

DIR_PIN = 2
STEP_PIN = 3

window = Tk()

window.title("Stepper Control")

window.geometry('350x200')

selected = IntVar()

rad1 = Radiobutton(window,text='Clockwise', value=0, variable=selected)

rad2 = Radiobutton(window,text='Counterclockwise', value=1, variable=selected)

def clicked():
   direction = selected.get()
   board.digital[DIR_PIN].write(direction)
   laps = 1600*int(combo.get())
   for i in range(0,laps):
       board.digital[STEP_PIN].write(1)
       time.sleep(1*10**-12)
       board.digital[STEP_PIN].write(0)
       time.sleep(1*10**-12)

btn = Button(window, text="Rotate", command=clicked)

rad1.grid(column=0, row=0)

rad2.grid(column=1, row=0)

combo = Combobox(window)

combo['values']= (1, 2, 3, 4, 5)

combo.current(1) #set the selected item

combo.grid(column=2, row=0)

btn.grid(column=3, row=0)

window.mainloop()

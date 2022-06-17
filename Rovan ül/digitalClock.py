from tkinter import Tk # impordib tkinteris Tk
from tkinter import Label # impordib tkinteris Label
import time # impordib time
import sys # impordib sys

master = Tk() # Teeb akna
master.title("Digital Clock") # Paneb aknale nime

def get_time(): # Teeb funktsiooni mis võtab aja
    timeVar = time.strftime("%I:%M:%S %p") # paneb timeVar väärtuse mis on praegune kellaeg
    clock.config(text=timeVar) # Paneb kellale praeguse kella
    clock.after(200,get_time) # clocile paneb aja väärtuse

Label(master,font=("Arial",30),text="Digital Clock",fg="white",bg="black").pack() # teeb teksti "Digital clock"
clock = Label(master, font=("Arial",100),bg="black",fg="white") # paneb kella sisse
clock.pack() # Defineerib clocki

get_time() # Käivitab funktsiooni

master.mainloop() # Paneb programmi tööle
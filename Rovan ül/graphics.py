from tkinter import * # Impordib tkinter

def run(): # teeb funktsiooni
    name = name_storage.get() # võtab kirja mis sisetad välja
    print(name) # Prindib sisestatud kirja

screen = Tk() # Teeb ekraani
screen.title("My first graphics program") # Paneb aknale nime
screen.geometry("500x500") # Seab akna suuruse

welcome_text = Label(text = "Welcome to our first graphics program ", fg = "red", bg = "yellow") # Teeb welcome teksti, kollase taustaga ja punase tekstiga
welcome_text.pack()

click_me = Button(text = "Click me", fg = "red", bg = "yellow", command = run) # Teeb click me nupu, kollase taustaga ja punase tekstiga
click_me.place(x = 10, y = 20) # Paneb nuppu asukoha

name_storage = StringVar() # Teeb stringiks
name = Entry(textvariable = name_storage) # Võtab sisestatud teksti
name.pack()
screen.mainloop() # Paneb programmi tööle
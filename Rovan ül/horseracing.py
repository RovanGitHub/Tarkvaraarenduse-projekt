from tkinter import * # impordib tkinteri
import time # impordib time
import random # impordib randomi

winner      = False # Teeb muutuja winner
red_horse_x = 0 # Teeb muutuja hobuse x asukoha
red_horse_y = 20 # Teeb muutuja hobuse y asukoha

blue_horse_x = -28 # Teeb muutuja hobuse x asukoha
blue_horse_y = 110 # Teeb muutuja hobuse y asukoha

def start_game(): # Teeb funktsiooni mis alustab mängu
    global blue_horse_x # teeb sinise hobuse igalpool kättesaadavaks
    global red_horse_x  # teeb punase hobuse igalpool kättesaadavaks
    global winner # teeb winneri igalpool kättesaadavaks

    while winner == False: # Paneb loopi programmi kui keegi pole võitnud
        time.sleep(0.05) # Paneb programmi pausile 0.05sekundiks
        random_move_blue_horse = random.randint(0,20) # Paneb sinisele hobusele 0-20 suvaka väärtuse
        random_move_red_horse  = random.randint(0,20) # Paneb punasele hobusele 0-20 suvaka väärtuse

        blue_horse_x += random_move_blue_horse # Värskendab hobuse asukohta
        red_horse_x  += random_move_red_horse # Värskendab hobuse asukohta

        move_horses(random_move_red_horse,random_move_blue_horse) # Käivitab funktsiooni
        main_screen.update() # Värskendab main_screeni
        winner = check_winner() # Käivitab funktsiooni

    if winner == "Tie": # Kui võitja võrdub "Tie"
        Label(main_screen,text=winner,font=('calibri',20),fg="green").place(x=200,y=450) # Teeb teksti ja paigutab selle
    else: # Else
        Label(main_screen,text=winner+" Wins !!",font=('calibri',20),fg="green").place(x=200,y=450) # Teeb teksti ja paigutab selle


def move_horses(red_horse_random_move,blue_horse_random_move): # Teeb funktsiooni hobuse liikumine
    canvas.move(red_horse,red_horse_random_move,0) # Teeb punasele hobusele liikumise
    canvas.move(blue_horse,blue_horse_random_move,0) # Teeb sinisele hobusele liikumise

def check_winner(): # Funktsioon mis vaatab kes võidab
    if blue_horse_x >= 550 and red_horse_x >= 550: # Kui mõlemad jõuavad lõppu siis
        return "Tie" # On jäid viiki
    if blue_horse_x >= 550: # Kui sinise hobune jõab ennem siis
        return "Blue Horse" # Ta võidab
    if red_horse_x >= 550: # Kui punanse houbne jõuab ennem siis
        return "Red Horse" # Ta võidab
    return False # Returnib False

# Seab ekraani seaded nagu aken ise, akna tiitel, akna suurus ja akna taustavärv
main_screen = Tk()
main_screen.title('Horse Racing')
main_screen.geometry('600x500')
main_screen.config(background='white')


canvas = Canvas(main_screen,width=600,height=200,bg="white") # Teeb canvasi
canvas.pack(pady=20) # # Teeb canvasi

# Toob pildid sisse
red_horse_img = PhotoImage(file="red-horse.png")
blue_horse_img = PhotoImage(file="blue-horse.png")

# Muudab hobuste pildite suurused
red_horse_img = red_horse_img.zoom(15) # Defineerib red_horse_img
red_horse_img = red_horse_img.subsample(50) # Defineerib red_horse_img
blue_horse_img = blue_horse_img.zoom(15) # Defineerib blue_horse_img
blue_horse_img = blue_horse_img.subsample(90) # Defineerib blue_horse_img

# Lisab pildid canvasele
red_horse = canvas.create_image(red_horse_x,red_horse_y,anchor=NW,image=red_horse_img) # Defineerib red_horse
blue_horse = canvas.create_image(blue_horse_x,blue_horse_y,anchor=NW,image=blue_horse_img) # Defineerib blue_horse

# Toob tekstid ekraanile kui kutsutakse
l1 = Label(main_screen,text='Select your horse',font=('calibri',20),bg="white")
l1.place(x=230,y=280)
l2 = Label(main_screen,text='Click play when ready!',font=('calibri',20),bg='white')
l2.place(x=200,y=330)

b1 = Button(main_screen,text='Play!',height=2,width=15,bg='white',font=('calibri',10),command=start_game) # Teeb nupu
b1.place(x=250,y=390) # Seab nupu asukoha

main_screen.mainloop() # Paneb programmi tööle
from tkinter import * # Importib tkniteri
import os

# Minu GitHub: https://github.com/RovanGitHub/Tarkvaraarenduse-projekt/tree/main/Rovan%20%C3%BCl

def delete2(): # Kustutab login väljundi
    screen3.destroy() # Kustutab login väljundi

def delete3(): # Kustutab login väljundi
    screen4.destroy() # Kustutab login väljundi

def delete4(): # Kustutab login väljundi
    screen5.destroy() # Kustutab login väljundi

def register_user(): # Teeb funktsiooni register_user
    username_info = username.get() # Kasutajanimi väärtus on sisestatud kasutaja nimi
    password_info = password.get() # Parooli väärtus on sisestatud parooli väärtus

    file=open(username_info + ".txt", "w") # Teeb uue .txt kasutajanime nimega
    file.write(username_info+"\n") # Lisab esimesele reale kasutajanime
    file.write(password_info) # Lisab teisele reale parooli väärtuse
    file.close() # Paneb faili kinni

    username_entry.delete(0, END) # Kustutab registreerimis väljast sisestatud nime
    password_entry.delete(0, END) # Kustutab registreerimis väljast sisestatud parooli

    Label(screen1, text = "Registration Sucess", fg= "green", font = ("Calibiri", 11)).pack() # Kui registreerimine õnnestus kirjutab rohelise teksti et õnnestus

def register(): # Teeb funktsiooni register
    global screen1 # Teeb globaalse muutuja screen1
    screen1 = Toplevel(screen) # screen1 väärtus on Toplevel(screen) mis tuleb tkinter'ist
    screen1.title("Register") # Seab akna nimeks register
    screen1.geometry("300x250") # Seab akna suuruse 300x250

    global username # Teeb globaalse muutuja username
    global password # Teeb globaalse muutuja password
    global username_entry # Teeb globaalse muutuja username_entry
    global password_entry # Teeb globaalse muutuja password_entry
    username = StringVar() # StringVar on klass, mis pakub abifunktsioone selliste muutujate otseseks loomiseks ja juurdepääsemiseks selles tõlgis
    password = StringVar() # StringVar on klass, mis pakub abifunktsioone selliste muutujate otseseks loomiseks ja juurdepääsemiseks selles tõlgis

    Label(screen1, text = "Please enter details below").pack() # Teeb uue teksti et lisa oma detailid
    Label(screen1, text = "").pack() # # Teeb lahtri tühjaks
    Label(screen1, text = "Username * ").pack() # Teeb uue teksti lahtri jaoks Username

    username_entry = Entry(screen1, textvariable = username) # Võtab kasutajanime
    username_entry.pack() # Pack asutatakse selleks, et vidin täidaks kogu kaadri
    Label(screen1, text = "Password * ").pack() # Teeb uue teksti lahtri jaoks password
    password_entry = Entry(screen1, textvariable = password) # Võtab parooli
    password_entry.pack() # Pack asutatakse selleks, et vidin täidaks kogu kaadri
    Label(screen1, text = "").pack() # Teeb lahtri tühjaks
    Button(screen1, text = "Register", width = 10, height = 1, command = register_user).pack() #

def login_verify(): # loob uue funktsiooni

    username1 = username_verify.get() # võtab kasutaja nime
    password1 = password_verify.get() # võtabk kasutaja parooli
    username_entry1.delete(0, END) # kustutab kasutajanime väljast
    password_entry1.delete(0, END) # kustutab parooli väljast

    list_of_files = os.listdir() # võtab kataloogist failid
    if username1 in list_of_files: # kontrollib kas kasutajanimi on olemas
        file1 = open(username1, "r") # avab faili
        verify = file1.read().splitlines() # loob faili sisestuseks
        if password1 in verify: # kontrollib kas parool on olemas
            login_sucess() # kutsub sisse funktsiooni login_sucess
            print("Login success") # prindib teksti
        else: # kui parooli pole
            print("Password has no been recognised") # prindib teksti
    else: # kui kasutajat pole
        print("User not found") # prindib teksti

def login_sucess(): # Eduka sisselogimise funktsioon
    global screen3 # Muudab login väljundi
    screen3 = Toplevel(screen) # Muudab login väljundi
    screen3.title("Success") # Määrab akna tiiteltektsi
    screen3.geometry("150x100") # Määrab akna suuruse
    Label(screen3, text="Login Sucess").pack() # Määrab login väljundi
    Button(screen3, text="OK", command=delete2).pack() # Määrab login väljundi

def password_not_recognised(): # Eduka sisselogimise funktsioon
    global screen4 # Muudab login väljundi
    screen4 = Toplevel(screen) # Muudab login väljundi
    screen4.title("Success") # Määrab akna tiiteltektsi
    screen4.geometry("150x100") # Määrab akna suuruse
    Label(screen4, text="Password Error").pack() # Määrab login väljundi
    Button(screen4, text="OK", command=delete3).pack() # Määrab login väljundi

def user_not_found(): # Eduka sisselogimise funktsioon
    global screen5 # Muudab login väljundi
    screen5 = Toplevel(screen) # Muudab login väljundi
    screen5.title("Success") # Määrab akna tiiteltektsi
    screen5.geometry("150x100") # Määrab akna suuruse
    Label(screen5, text="User Not Found").pack() # Määrab login väljundi
    Button(screen5, text="OK", command=delete4).pack() # Määrab login väljundi

def login(): # Eduka sisselogimise funktsioon
    global screen2 # Muudab login väljundi
    screen2 = Toplevel(screen) # Muudab login väljundi
    screen2.title("Login") # Määrab akna tiiteltektsi
    screen2.geometry("300x250") # Määrab akna suuruse
    Label(screen2, text="Please enter details below to login").pack() # Määrab login väljundi
    Label(screen2, text="").pack() # Määrab login väljundi

    global username_verify # Muudab login väljundi
    global password_verify # Muudab login väljundi

    username_verify = StringVar() # Muudab login väljundi
    password_verify = StringVar() # Muudab login väljundi

    global username_entry1 # Muudab login väljundi
    global password_entry1 # Muudab login väljundi

    Label(screen2, text="Username * ").pack() # Määrab login väljundi
    username_entry1 = Entry(screen2, textvariable=username_verify) # Määrab login väljundi
    username_entry1.pack() # Määrab login väljundi
    Label(screen2, text="").pack() # Määrab login väljundi
    Label(screen2, text="Password * ").pack() # Määrab login väljundi
    password_entry1 = Entry(screen2, textvariable=password_verify) # Määrab login väljundi
    password_entry1.pack() # Määrab login väljundi
    Label(screen2, text="").pack() # Määrab login väljundi
    Button(screen2, text="Login", width=10, height=1, command=login_verify).pack() # Määrab login väljundi

def main_screen(): # Teeb uue funktsiooni main_screen
    global screen # Teeb globaalse muutuja screen
    screen = Tk() # Tk eksemplari loomine initsialiseerib selle interpretaatori ja loob juurakna
    screen.geometry("300x250") # Seab suuruseks 300x250
    screen.title("Notes 1.0") # Paneb akna nimeks Notes 1.0
    Label(text = "Notes 1.0", bg = "gray", width = "300", height = "2", font = ("Calibri", 13)).pack()# Teeb teksti Notes.10, halli värviga ja seab suuruse ja fondi
    Label(text = "").pack() # Teeb lahtri tühjaks
    Button(text="Login", height="2", width="30", command=login).pack() # Teeb logimis nupu
    Label(text= "").pack() # Teeb tühja lahtri
    Button(text = "Register", height = "2", width = "30", command = register).pack() # Teeb nupu register

    screen.mainloop() # Käsib aknal oodata, kuni kasutaja midagi teeb

main_screen() # Käivitab funktsiooni main_screen

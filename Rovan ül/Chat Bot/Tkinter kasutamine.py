from tkinter import * # Impordib tkinter

# Minu GitHub: https://github.com/RovanGitHub/Tarkvaraarenduse-projekt/tree/main/Rovan%20%C3%BCl

def save_info(): # Teeb funktsiooni save_info
    firstname_info = firstname.get() # paneb firstname_infole first name väärtuse
    lastname_info = lastname.get() # paneb lastname_infole last name väärtuse
    age_info = age.get() # paneb age_infole age väärtuse
    age_info = str(age_info) # Muudab age_info stringiks
    print(firstname_info, lastname_info, age_info) # Prindib nimed ja vanuse

    file = open("user.txt", "w") # Teeb faili "user"
    file.write(firstname_info) # Kirjutab eesnime faili
    file.write(lastname_info) # Kirjutab perekonnanime faili
    file.write(age_info) # Kirjutab vanuse faili
    file.close() # Lõpetab failiga tegelemise
    print("User ", firstname_info, " has been registered successfully") # prindib teksti

screen = Tk() # Teeb akna
screen.geometry("500x500") # Seab akna suuruse
screen.title("Python form") # Paneb akna nime
heading= Label(text = "Python Form", bg="grey", fg="black", width="500", height="3") # Teeb Värvid taustale, tekstile jne

firstname_text = Label(text = "firstname * ",) # Teeb firstname teksti lahtri
lastname_text = Label(text = "lastname * ",) # Teeb lastname teksti lahtri
age_text = Label(text = "Age * ",) # Teeb age teksti lahtri
firstname_text.place(x=15, y=70) # Paigutab firstname teksti
lastname_text.place(x=15, y=140) # Paigutab lastname teksti
age_text.place(x=15, y=210) # Paigutab age teksti

firstname = StringVar() # Saab hoida stringe
lastname = StringVar() # Saab hoide stringe
age = IntVar() # Saab hoida inte

firstname_entry = Entry(textvariable=firstname, width="300") # Teeb lahtri ja selle suuruse
lastname_entry = Entry(textvariable=lastname, width="30") # Teeb lahtri ja selle suuruse
age_entry = Entry(textvariable= age, width="30") # Teeb lahtri ja selle suuruse

firstname_entry.place(x=15, y=100) # Paigutab lahtri asukoha
lastname_entry.place(x=15, y=180) # Paigutab lahtri asukoha
age_entry.place(x=15, y=240) # Paigutab lahtri asukoha

register = Button(screen,text = "Register", width="30", height="2", command = save_info, bg="gray") # Teeb nuppu, selle asukoha ja värvid ja funktsiooni
register.place(x=15, y=290) # Paigutab register nuppu asukoha

screen.mainloop() # Käivitab ekraani

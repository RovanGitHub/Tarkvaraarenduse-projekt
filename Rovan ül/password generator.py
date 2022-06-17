import random # Impordib randomi

chars = "QWERTYUIOPLKJHGFDSAZXCVBNMmnbvcxasdfghjklpoiuytrewq1234567890" # Tähed ja numbrid mida password generator kasutab

while 1: # teeb loopi
    password_len = int(input("What lenght would you like your password to be: ")) # Küsib kui pikka passwordi tahad
    password_count = int(input("How many passwords would you like: ")) # Küsib kui palju paroole tahad
    for x in range(0, password_count): # nii palju kordab kui palju passworde tahad genereerida
        password = "" # Teeb tühja muutuja
        for x in range(0, password_len): # kordab niipalju kui passwordi pikkus on
            password_chars = random.choice(chars) # Suvakate tähtedega teeb parooli
            password    = password + password_chars
        print("Here is your password : ", password) # Prindib su paroolid
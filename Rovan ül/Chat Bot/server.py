import socket # Importib socketi
import sys # Importib sys
import time # Importib time

# Minu GitHub: https://github.com/RovanGitHub/Tarkvaraarenduse-projekt/tree/main/Rovan%20%C3%BCl

s = socket.socket() # Viis võrgu kahe sõlme ühendamiseks üksteisega suhtlemiseks
host = socket.gethostname() # Võtab aruti hostname
print("Server käivitub hostis: ", host) # Prindib arvuti host nime
port = 8080 # Seab pordiks 8080
s.bind((host, port)) # Seob pordi ja hosti
print("") # Teeb tühja rea
print("Server on hosti ja pordiga edukalt sidunud") # Prindib teksti
print("") # Teeb rühja rea
print("Server ootab sissetulevaid ühendusi") # Prindib teksti
print("") # Teeb rühja rea
s.listen(1) # Ootab ühendusi
conn, addr = s.accept() # Võtab ühenduse vastu
print(addr, "On serveriga ühenduses ja on nüüd võrgus...") # Prindib teksti
print("") # Teeb rühja rea
while 1: # Kasutatakse lõpmatu tsükli jaoks
    message = input(str(">>")) # Küsib sõnumit mida saata tahad
    message = message.encode() # Koodeerib teksti
    conn.send(message) # Saadab teksti
    print("Sõnum saadeti...") # Prindib teksti
    print("") # Teeb tühja rea
    incoming_message = conn.recv(1024) # Loeb maksimaalselt 1024 baiti, blokeerib, kui lugemist ei oota andmed
    incoming_message = incoming_message.decode() # Dekodeerib sõnumi
    print(" Client: ", incoming_message) # Prindib kliendi sõnumi
    print("") # Teeb rühja rea
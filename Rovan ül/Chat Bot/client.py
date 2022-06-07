import socket # Importib socketi
import sys # Importib sys
import time # Importib time

# Minu GitHub: https://github.com/RovanGitHub/Tarkvaraarenduse-projekt/tree/main/Rovan%20%C3%BCl

s = socket.socket() # Viis võrgu kahe sõlme ühendamiseks üksteisega suhtlemiseks
host = input(str("Sisestage serveri hostinimi:")) # Küsib serveri nime
port = 8080 # Seab pordiks 8080
s.connect((host, port)) # Ühendub pordi ja hostname
print("Ühendatud vestlusserveriga") # Prindib teksti
while 1: # Kasutatakse lõpmatu tsükli jaoks
    incoming_message = s.recv(1024) # # Loeb maksimaalselt 1024 baiti, blokeerib, kui lugemist ei oota andmed
    incoming_message = incoming_message.decode() # Dekodeerib teksti
    print(" Server: ", incoming_message) # Prindib serveri saadetud teksti
    print("") # Teeb tühja rea
    message = input(str(">>")) # Küsib sõnumit mida saata tahad kilendi poolt
    message = message.encode() # Kodeerib sõunumi
    s.send(message) # Saadab sõnumi
    print("Sõnum saadeti...") # Prindib teksti
    print("") # Teeb tühja rea
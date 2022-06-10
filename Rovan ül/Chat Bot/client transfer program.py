import socket # Impordib socketi

s = socket.socket() # seab socketile klassi
host = input(str("Please enter the host address of the sender: ")) # Prindib teksti
port = 8080 # Seab pordi
s.connect((host, port)) # ühendab pordi ja hostnime
print("Connected...") # Prindib teksti

filename = input(str("Please enter a filename for the incoming file: ")) # Küsib failinime
file = open(filename, 'wb') # Avab faili
file_data = s.recv(1024) # Loeb maksimaalselt 1024 baiti, blokeerib, kui lugemist ei oota andmed
file.write(file_data) # Kirjutab selle faili uute kohta
file.close() # Paneb faili kinni
print("File has been received successfully.") # Kirjutab teksti
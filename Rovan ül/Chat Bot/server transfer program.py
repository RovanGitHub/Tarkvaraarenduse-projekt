import socket # Impordib socketi

s = socket.socket() # seab socketile klassi
host = socket.gethostname() # Otsib arvuti hostnime
port = 8080 # Seab pordi
s.bind((host, port)) # Ühendab hosti pordiga
s.listen(1) # Jääb kuulama connectioni
print(host) # Prindib arvuti hostnime
print("Waiting for any incoming connections...") # prindib teksti
conn, addr = s.accept() # Võtab ühenduse vastu
print(addr, "Has connected to server") # Prindi teksti

filename = input(str("Please enter the filename of the file: ")) # Küsib failinime
file = open(filename, 'rb') # Avab faili
file_data = file.read(1024) # Loeb maksimaalselt 1024 baiti, blokeerib, kui lugemist ei oota andmed
conn.send(file_data) # Saadab faili
print("Data has been transmitted successfully") # Prindib teksti
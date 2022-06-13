import smtplib # impordib smtplib

sender_email = "vikk.opilane@outlook.com" # kes saadab meili
rec_email = "rovan.kutt@vikk.ee" # kellele saadab meili
password = input(str("Please enter your password: ")) # küsib meili parooli
message = "Hey, this was sent using python" # seab teksti mis saadab

server = smtplib.SMTP('smtp-mail.outlook.com', 587) # sisestab emaili
server.starttls() # alustab starttlsi
server.login(sender_email, password) # logib sisse emaili
print("Login success") # prindib et logisid sisse
server.sendmail(sender_email, rec_email, message) # saadab meili
print("Email has been sent to ", rec_email) # prindib et meil on saadetud

import requests # Impordib requests

def download_files(url): # Defineerib funktsiooni
    local_filename = url.split('/')[-1] # Defineerib local_filename
    with requests.get(url, stream=True) as r: # Defineerib r
        print("Downloading...") # Printib "Downloading..."
        with open("C:/Users/Johan Godinho/Desktop/"+local_filename, 'wb') as f: # Defineerib f
            print("Writing data to file") # Prindib teksti
            for chunk in r.iter_content(chunk_size=8192): # Defineerib chunk
                f.write(chunk) # Defineerib f.write funktsiooni parameeter
    f.close() # Sulgeb faili
    print("Download complete") # Prindib et pild on laetud
    print("File saved as "+ local_filename) # Printib et fail on salvestatud

while 1: # Korduv while loop
    print("Welcome to the image downloader") # Printib et teretulemast
    image_url = input(str("Image url : ")) # Küsib pildi linki
    download_files(image_url) # Käivitab funktsiooni
    print("") # Printib tühja teksti
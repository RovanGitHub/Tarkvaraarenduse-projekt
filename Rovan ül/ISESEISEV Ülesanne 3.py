import pygame
import sys
import random
pygame.init()

#värvid
lGreen = [153, 255, 153] # teeb rohelise värvi
#lBlue = [153, 204, 255] # teeb sinise värvi
#red = [255, 0, 0] # teeb punase värvi

#ekraani seaded
screen=pygame.display.set_mode([640,480]) # seab akna suuruseks 640x480
pygame.display.set_caption("Ülesanne 3 harjutamine") # seab akna nimeks harjutamine
screen.fill(lGreen) # täidab tausta rohelise värviga

#gameover = False # seab et mäng ei ole läbi

#while not gameover: # nii kaua kui mäng pole läbi

    #Lisame pildid
#    youWin = pygame.image.load("img/youwin.png") # toob sisse youwin.png pildi
#    youWin = pygame.transform.scale(youWin, [300, 120]) # muudab pildi suurust
#    screen.blit(youWin,[180,100]) # toob pildi sisse ja muudab asjukohta

#    pygame.display.flip() # värskendab ekraani

    #mängu sulgemine ristist
#    for i in pygame.event.get():
#       if i.type == pygame.QUIT:
#           sys.exit()

#for i in range (1,10): #
#    x = random.randint(0, 620) # nullist 620ni suvakas koht horisontaalselt
#    y = random.randint(0, 460) # nullist 460ni suvakas koht vertikaalselt
#    pygame.draw.rect(screen, red, [x, y, 20, 20]) # teeb punase ruudu

def drawHouse(x, y, width, height, screen, color):
    points = [(x, y - ((3 / 4.0) * height)), (x, y), (x + width, y), (x + width, y - (3 / 4.0) * height),
              (x, y - ((3 / 4.0) * height)), (x + width / 2.0, y - height), (x + width, y - (3 / 4.0) * height)]
    lineThickness = 2
    pygame.draw.lines(screen, color, False, points, lineThickness)

# teeb erinevad värvid
red = [255, 0, 0]
green = [0, 255, 0]
blue = [0, 0, 255]
pink = [255, 153, 255]
lGreen = [153, 255, 153]

# teeb funktsiooni drawHouse mis joonistab maja
def drawHouse(x, y, width, height, screen, color):
    points = [(x, y - ((3 / 4.0) * height)), (x, y), (x + width, y), (x + width, y - (3 / 4.0) * height),
              (x, y - ((3 / 4.0) * height)), (x + width / 2.0, y - height), (x + width, y - (3 / 4.0) * height)]
    lineThickness = 2 # joone paksuseks paneb kaks
    pygame.draw.lines(screen, color, False, points, lineThickness)

# kutsub funktsiioni drawHouse'i välja
drawHouse(100, 400, 300, 200, screen, red) # seab maja asukoha ja suuruse

pygame.display.flip() # värskendab ekraani

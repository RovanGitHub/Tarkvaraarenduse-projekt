import pygame # impordib pygame
pygame.init() # käivitab pygame


#screen=pygame.display.set_mode([640,480]) # teeb akna 640x480
#pygame.display.set_caption("Harjutamine") # seab akna pealkirja
#screen.fill([204, 255, 204]) # värvib akna tausta

#font = pygame.font.Font(None, 30) # teeb fondi suurusega 30
#text = font.render("Hello PyGame", True, [0,0,0]) # lisab teksti "Hello Pygame" musta värviga
#screen.blit(text, [200,200]) # toob teksti välja ja määrab asukoha

#font = pygame.font.SysFont("Tahoma", 50) # ise saab ka fonti lisada None'i asemel fondi nime jutumärkides kirjutades

#font = pygame.font.Font(pygame.font.match_font('arial'), 50) # teeb fondi arial suurusega 50
#text = font.render("Hello PyGame", True, [0,0,0]) # teeb teskti "Hello Pygame" musta värviga

#text_width = text.get_rect().width # tesksti paigutamiseks laius
#text_height = text.get_rect().height # teksti paigutamiseks kõrgus

#screen.blit(text, [320,240]) # toob teskti välja kindla asukohaga
#font.set_underline(True) # saab tekstile panna joone alla

#bg = pygame.image.load("img/bg.jpg") # lisab pildi kaustast kus see sama fail asub, faili laiendi peab ka kirjutama
#screen.blit(bg,[0,0]) # toob pildi välja ja määrab asukoha

#youWin = pygame.image.load("img/youwin.png") # lisab pildi youwin.png
#youWin = pygame.transform.scale(youWin, [300, 120]) # puudab pildi kõrgus ja laiust
#screen.blit(youWin,[180,100]) # toob pildi välja ja muudab asukohta

pygame.display.flip()
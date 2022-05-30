import pygame # importib pygame
pygame.init() # käivtab pygame

screen=pygame.display.set_mode([640,480]) #teeb 640x480 akna
#pygame.display.set_caption("My Screen") paneb aknale nime
#screen=pygame.display.set_mode([640,480],pygame.RESIZABLE) teeb nii et akna suuruks saaks ise muuta
#screen.fill([204, 255, 255] #muudab taustavärvi
#pygame.draw.line(screen, [255,0,0], [100,100], [200,200], 2) # teeb joone, sulgudes tähendab (screen, värv, algus, lõpp, paksus)
#pygame.draw.rect(screen, [0, 225, 0], [50, 80, 200, 300], 2) # teeb ristküliku, sulgudes tähendab (screen, värv, [asukoht, suurus], joone paksus)
#pygame.draw.circle(screen, [0, 0, 255], [150,200], 100, 1) # teeb ringi, sulgudes tähendab (screen, värv, [ringi keskpunkt, raadius], joone paksus)
#pygame.draw.polygon(screen, [255, 0, 255], [[50,50],[100,50],[100,150],[250,50],[350,250],[50,250]], 2) # teeb hulknurga, sulgudes tähendab (screen, värv, koordinaatide loend, joone_paksus)'
#pygame.draw.ellipse(screen, [0, 225, 0], [50, 80, 2000, 300], 2) # teeb ovaali, sulgudes tähendab (screen, värv, [asukoht, suurus], joone paksus)
#pygame.draw.arc(screen,[0,0,0], [100,100,250,200], 0, 3.14*1.5, 1) # teeb kaare, sulgudes tähendab (screen, värv, ristküliku koordinaadid, algus nurk, lõpp nurk, joone paksus)
pygame.display.flip() #värskendab ekraani









running = True
while running:
  for event in pygame.event.get():
    if event.type == pygame.QUIT:
      running = False
    if running == False:
      pygame.quit()
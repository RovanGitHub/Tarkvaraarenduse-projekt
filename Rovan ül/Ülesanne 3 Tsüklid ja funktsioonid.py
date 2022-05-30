import pygame # importib pygame
pygame.init() # käivitab pygame

# https://github.com/RovanGitHub/Tarkvaraarenduse-projekt

roh = [153, 255, 102] # roheline värv

screen = pygame.display.set_mode([640,480]) # akana suurus
pygame.display.set_caption("Ülesanne 3 - Rovan Kütt") # akna nimi

screen.fill(roh) # teeb ekraani tausta roheliseks

jonvarv = [255, 0, 0] # teeb joone värvi

hor = 0 # horisontaalne

rida = 50 # read

rutver = 0 # ruut vertikaalselt

verarv = 50 # veergude arv

for i in range (rida):
  pygame.draw.line(screen, jonvarv, [hor, 0], [hor, 480], 2) # teeb read


  hor += 19 # muuda arv suuremaks et teha ruut horisontaalselt suuremaks

for i in range (verarv):
  pygame.draw.line(screen, jonvarv, [0, rutver], [640, rutver], 2) # teeb veerud

  rutver += 19 # muuda arv suuremaks et teha ruut vertikaalselt suuremaks

pygame.display.flip() # värskendab ekraani

# Selle jaoks, et ekraani saaks kinni panna.
running = True
while running:
  for event in pygame.event.get():
    if event.type == pygame.QUIT:
      running = False
    if running == False:
      pygame.quit()

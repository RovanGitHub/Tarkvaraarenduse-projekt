import pygame  # Impordib pygame

pygame.init()  # Käivitab pygame mooduli

screen = pygame.display.set_mode([300, 300])  # Teeb 300x300 ekraani

pygame.display.set_caption("Lumemees - Torren Tamm")  # Nimetab ekraani nimeliseks

pygame.draw.circle(screen, [255, 255, 255], [150, 85], 30, 0)  # Teeb lumememme pea
pygame.draw.circle(screen, [0, 0, 0], [138, 82], 5, 0)  # Teeb lumememme vasaku silma
pygame.draw.circle(screen, [0, 0, 0], [162, 82], 5, 0)  # Teeb lumememme parema silma
pygame.draw.polygon(screen, [255, 0, 0], [[145, 90], [155, 90], [150, 105]], 0)  # Teeb lumememme nina
pygame.draw.circle(screen, [255, 255, 255], [150,150], 40, 0)  # Teeb lumememme keskmise palli
pygame.draw.circle(screen, [255, 255, 255], [150, 235], 50, 0)  # Teeb lumememme alumise palli

pygame.display.flip()  # Värskendab ekraani

# Selle jaoks, et ekraani saaks kinni panna.
running = True
while running:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False
        if running == False:
            pygame.quit()
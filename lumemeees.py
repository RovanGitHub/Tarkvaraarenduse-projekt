import pygame  # Importeerib pygame

pygame.init()  # Käivitab pygame mooduli

screen = pygame.display.set_mode([300, 500])  # Teeb 300x500 ekraani

pygame.display.set_caption("Lumemees - Rovan Kütt")  # Paneb akna nimeks Rovan Kütt

pygame.draw.circle(screen, [255, 255, 255], [150, 85], 30, 0)  # Teeb valge lumememme pea
pygame.draw.circle(screen, [0, 0, 0], [138, 82], 5, 0)  # Teeb musta lumememme vasaku silma
pygame.draw.circle(screen, [0, 0, 0], [162, 82], 5, 0)  # Teeb musta lumememme parema silma
pygame.draw.polygon(screen, [255, 0, 0], [[145, 90], [155, 90], [150, 105]], 0)  # Teeb punase lumememme nina
pygame.draw.circle(screen, [255, 255, 255], [150,150], 40, 0)  # Teeb valge lumememme keskmise palli
pygame.draw.circle(screen, [255, 255, 255], [150, 235], 50, 0)  # Teeb valge lumememme alumise palli
pygame.draw.line(screen, [165, 42, 42], [120,120], [50,110], 4) # vasak käsi
pygame.draw.line(screen, [165, 42, 42], [180,120], [240,115], 4) # parem käsi
pygame.draw.line(screen, [165, 42, 42], [260,78], [240,117], 4) # parem üleval käe oks
pygame.draw.line(screen, [165, 42, 42], [240,117], [266,150], 4)# parem all käe oks
pygame.draw.line(screen, [165, 42, 42], [51,110], [38,76], 4) # vasak üleval käe oks
pygame.draw.line(screen, [165, 42, 42], [51,110], [36,140], 4) # vasak all käe oks
pygame.draw.circle(screen, [0, 0, 0], [151, 130], 5, 0) # ülemine nööp
pygame.draw.circle(screen, [0, 0, 0], [151, 145], 5, 0) # keskmine nööp
pygame.draw.circle(screen, [0, 0, 0], [151, 160], 5, 0) # alumine nööp

pygame.display.flip()  # Värskendab ekraani

for i in range(9999):
    x,y = pygame.mouse.get_pos()
    print(x, y)

# Internetist võetud, et akent kinni panna.
running = True
while running:
    ev = pygame.event.get()

    for event in ev:

        if event.type == pygame.MOUSEBUTTONUP:
            x, y = pygame.mouse.get_pos()
            print(x, y)
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False
        if running == False:
            pygame.quit()

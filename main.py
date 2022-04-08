import pygame
pygame.init()

#ekraani seaded
screen=pygame.display.set_mode([640,480])
pygame.display.set_caption("Harjutus 2")
screen.fill([204, 255, 204])

bg = pygame.image.load("bg_shop.jpg")
screen.blit(bg,[0,0])

seller = pygame.image.load("seller.jpg")
seller = pygame.transform.scale(seller, [250, 300])
screen.blit(seller,[100,160])

mull = pygame.image.load("chat.jpg")
mull = pygame.transform.scale(mull, [260, 205])
screen.blit(mull,[244,60])

#lisame teksti
font = pygame.font.Font(pygame.font.match_font('arial'), 30)
text = font.render("Tere, olen Rovan Kütt", True, [255,255,255])
screen.blit(text, [267,130])


pygame.display.flip()


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
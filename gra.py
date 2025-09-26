import pygame

from Platforma import Platforma

pygame.init()
 
SCREEN_WIDTH = 1024
SCREEN_HEIGHT = 800
 
screen_surface = pygame.display.set_mode((SCREEN_WIDTH, SCREEN_HEIGHT))
 
pygame.display.set_caption("Gra")
 
clock = pygame.time.Clock()
 
status = True

obraz_tla = pygame.image.load("images_arkanoid/background.png")

platforma = Platforma()


while status:
    events = pygame.event.get()
    for event in events:
        if event.type == pygame.QUIT:
            status = False
            pass
    

    wcisniete_klawisze = pygame.key.get_pressed()
    if wcisniete_klawisze[pygame.K_RIGHT]:
        platforma.ruszaj_platforma(1)
    if wcisniete_klawisze[pygame.K_LEFT]:
        platforma.ruszaj_platforma(-1)

    screen_surface.blit(obraz_tla, (0,0))
    screen_surface.blit(platforma.obraz, platforma.rect)

    pygame.display.flip()
    clock.tick(60)
    pass
 
pygame.quit()
quit()
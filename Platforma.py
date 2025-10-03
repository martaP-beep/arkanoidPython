import pygame


SCREEN_WIDTH = 1024
SCREEN_HEIGHT = 800

class Platforma(pygame.sprite.Sprite):
    def __init__(self):
        super(Platforma, self).__init__()
        self.obraz = pygame.image.load("images_arkanoid/pad.png")
        self.zresetuj_pozycje()
        self.porusza_sie = 0

    def zresetuj_pozycje(self):
        self.rect = pygame.Rect(SCREEN_WIDTH / 2 - 70, SCREEN_HEIGHT - 100, 140, 30)

    def ruszaj_platforma(self, kierunek):
        self.porusza_sie = kierunek
        self.rect.move_ip(kierunek * 10, 0)
        if self.rect.left <= 0:
            self.rect.x = 0
        if self.rect.right >= SCREEN_WIDTH:
            self.rect.x = SCREEN_WIDTH - 140

    def aktulizuj(self):
        self.porusza_sie = 0

    pass
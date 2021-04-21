
import pygame,sys
from pygame.locals import *
width = 900
high = 600
class SpaceShip(pygame.sprite.Sprite):
    "Class ships"
    def __init__(self):
        pygame.sprite.Sprite.__init__(self)
        self.imagen_ship = pygame.image.load("image/25129-4-spaceship-file.png")
        
        self.rect = self.imagen_ship.get_rect()
        self.rect.centerx = width/2
        self.rect.centery = high-30
        
        self.list_shoot = []
        self.life = True
        
        self.velocity = 2
    def movement(self):
        if self.life == True:
            if  self.rect.left <0:
                self.rect.left = 0
            elif self.rect.right > width:
                self.rect.right = width
            elif self.rect.top <0:
                self.rect.top = 0
            elif self.rect.bottom > high:
                self.rect.bottom = high
                
    def shoot(self):
        print("SHOOOOT---")
    def draw(self,surface):
        surface.blit(self.imagen_ship, self.rect)
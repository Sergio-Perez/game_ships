import pygame,sys
from pygame.locals import *


class Missile(pygame.sprite.Sprite):
    def __init__(self,pos_x, pos_y, route, character):
        pygame.sprite.Sprite.__init__(self)
        
        self.imagen_missile = pygame.image.load(route)
        
        self.rect = self.imagen_missile.get_rect()
        self.velocity_shoot = 3
        
        self.rect.top  = pos_y
        self.rect.left = pos_x

        self.shoot_character = character
    def trajectory (self):
        if self.shoot_character == True:
            self.rect.top = self.rect.top - self.velocity_shoot
        else:
            self.rect.top = self.rect.top + self.velocity_shoot

    def draw(self, surface):
        surface.blit(self.imagen_missile, self.rect)
        
        
        
        
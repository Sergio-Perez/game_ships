import pygame,sys
from pygame.locals import *


class Missile(pygame.sprite.Sprite):
    def __init__(self,pos_x, pos_y):
        pygame.sprite.Sprite.__init__(self)
        
        self.imagen_missile = pygame.image.load('image/48243-3-missile-png-file-hd(1).png')
        
        self.rect = self.imagen_missile.get_rect()
        self.velocity_shoot = 0.1
        
        self.rect.top  = pos_y
        self.rect.left = pos_x
    
    def trajectory (self):
        self.rect.top = self.rect.top - self.velocity_shoot
        
    def draw(self, surface):
        surface.blit(self.imagen_missile, self.rect)
        
        
        
        
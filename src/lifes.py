
import pygame
from pygame.locals import *
width = 900

class Lifes(pygame.sprite.Sprite):
    "Lifes"
    def __init__ (self, pos_x,pos_y):
        pygame.sprite.Sprite.__init__(self)
        
        self.imagen_life =  pygame.image.load("image/heart.png")
        
        self.rect = self.imagen_life.get_rect()
        self.list_life = []
        self.rect.top = pos_y
        self.rect.left = pos_x  
        
        
        
    def draw(self, surface):
        surface.blit(self.imagen_life, self.rect)



            
def draw_all_lifes(numbers, pos_x,pos_y):
    list_life = []
    positions = range(35,100,30)
    for number, position in zip(range(0,numbers),positions):
        life = Lifes(pos_x- position, pos_y)
        list_life.append(life)
    return list_life
        
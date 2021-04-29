import pygame,sys
from pygame.locals import *
from random import randint
from . import missile, conf

print(conf.width)
class Ufo(pygame.sprite.Sprite):
    def __init__(self, pos_x, pos_y,distance, imagen_one,velocity=1):
        pygame.sprite.Sprite.__init__(self)
        
        self.ufo = pygame.image.load(imagen_one)
        #self.ufo2 = pygame.image.load(imagen_two)

        
        self.rect = self.ufo.get_rect()
        
        self.list_shoot = []
        self.velocity = velocity
        
        self.rect.top = pos_y
        self.rect.left = pos_x  
        
        self.range_shoot = 5
        self.timeChange = 1
        
        self.right= True
        self.count = 0
        self.max_down = self.rect.top - 40    
        self.limit_right = pos_x + distance
        self.limit_left = pos_x - distance
        
        self.wins = False
        
    def behaviour(self,time):
        if self.wins ==False:
            self.__movement()

            if self.timeChange == time:
                self.__attack()
                self.timeChange += 1
                
    def __movement(self):
        if self.count < 3 :
            self.__movement_lateral()
        else:
            self.__movement_down()
            
    def __movement_down(self):
        if self.max_down  <= self.rect.top: 
            self.count = 0 
            self.max_down = self.rect.top  + 40
        
        else: 
            self.rect.top += 1   
    def __movement_lateral(self):
        if self.right == True:
            self.rect.left = self.rect.left + self.velocity
            if self.rect.left > conf.width -100:
    
                self.right =  False
                self.count += 1
        else:
            self.rect.left = self.rect.left - self.velocity
            if self.rect.left <0:
                self.right = True

                    
    def draw(self, surface):
        surface.blit(self.ufo, self.rect)
    
    def __attack(self):
        if (randint(0,2500)< self.range_shoot):
            self.__shoot()
    
    def __shoot(self):
        x, y = self.rect.center
        my_missile = missile.Missile(x, y, "image/missile-down-png-file-hd.png", False)
        self.list_shoot.append(my_missile)
        
        
        
            
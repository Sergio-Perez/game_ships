
import pygame,sys
from pygame.locals import *
from . import missile
width = 900
high = 600
class SpaceShip(pygame.sprite.Sprite):
    "Class space ships"
    def __init__(self):
        pygame.sprite.Sprite.__init__(self)
        self.imagen_ship = pygame.image.load("image/25129-4-spaceship-file.png")
        self.imagen_explosion = pygame.image.load('image/31577-4-atomic-explosion-photos(1)(1).png')
        self.rect = self.imagen_ship.get_rect()
        self.rect.centerx = width/2
        self.rect.centery = high-30
        
        self.list_shoot = []
        self.life = True
        
        self.velocity = 3
        self.sound_shoot = pygame.mixer.Sound('sound/efects/GunShotSnglFireIn.wav')
        self.sound_explosion = pygame.mixer.Sound('sound/efects/Explosion_my_ship.wav')
        self.destruction = False
    def move_left(self):
        self.rect.left -= self.velocity
        self.__movement()
    
    def move_right(self):
        self.rect.right += self.velocity
        self.__movement()
    def move_up(self):
        self.rect.top -= self.velocity
        self.__movement()
    def move_bottom(self):
        self.rect.bottom += self.velocity
        self.__movement()
    
    def __movement(self):
        
        if self.life == True:
            if  self.rect.left <0:
                self.rect.left = 0
            elif self.rect.right > width:
                self.rect.right = width
            elif self.rect.top <0:
                self.rect.top = 0
            elif self.rect.bottom > high:
                self.rect.bottom = high
                
    def shoot(self,x,y):
        my_missile = missile.Missile(x,y,'image/48243-3-missile-png-file-hd(1).png',True)
        self.list_shoot.append(my_missile)
        self.sound_shoot.play()
    
    def destructions(self):
        
        self.sound_explosion.play()
        self.life = False
        self.velocity = 0
        self.imagen_ship = self.imagen_explosion
        
    def draw(self,surface):
        surface.blit(self.imagen_ship, self.rect)
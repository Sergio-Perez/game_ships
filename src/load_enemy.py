import pygame,sys
from . import ufo

def load_enemy_equal_character(width,heigh):
    list_enemy = []
    for zone in (range(0,width,150)):# 128 7 columns 150 6 columns
        enemy = ufo.Ufo(zone  ,heigh ,110, 'image/ufo2-spaceship-photos.png')
        list_enemy.append(enemy)
    return list_enemy
    
def load_enemy_diferent():
    list_enemy = []
    
    for columns in range(0,700,300):
    
        for pos_y in ((range(0,300,100))):
            enemy  = ufo.Ufo(columns    , pos_y,40,'image/ufo-spaceship-picture.png')
            enemy2 = ufo.Ufo(columns+100, pos_y,40,'image/ufo2-spaceship-photos.png')
            enemy3 = ufo.Ufo(columns+200, pos_y,40,'image/ufo3_spaceship_transparent.png')
            list_enemy.append( enemy) 
            list_enemy.append (enemy2)
            list_enemy.append(enemy3)



    return list_enemy
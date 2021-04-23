import pygame


def game_over(list_enemy):
    
    for enemy in list_enemy:
        for shoot in enemy.list_shoot:
            enemy.list_shoot.remove(shoot)
        
        enemy.wins = True 
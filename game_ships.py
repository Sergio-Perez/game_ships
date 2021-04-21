import pygame,sys
from pygame.locals import *
from src import spaceship, missile
# Widht an high screen
width = 900
high = 600
color_black=(0,0,0)


def run_game ():
        
    pygame.init()
    window = pygame.display.set_mode((width,high))
    pygame.display.set_caption("Space ships")

    #imagen_background = pygame.image.load('image/fondo/space_level1.jpeg')
    player = spaceship.SpaceShip()
    
    shoot = missile.Missile(width/2, high-30)
    
    in_play = True
    while True:
        player.movement()
        window.fill(color_black)
        time= round(pygame.time.get_ticks()/1000,0)    
        
        movement = pygame.key.get_pressed()
        shoot.trajectory()
        if in_play == True:
            if movement[pygame.K_RIGHT] :              
                player.rect.right += player.velocity
                
            if movement[pygame.K_LEFT]:                    
                player.rect.left -= player.velocity                

            if movement[pygame.K_UP]:                            
                player.rect.top -= player.velocity  
                                    
            if movement[pygame.K_DOWN]:              
                player.rect.bottom += player.velocity  
                    
            if movement[pygame.K_SPACE]:
                player.shoot()
        
        
    
        

        for event in pygame.event.get():
            if event.type == QUIT:
                pygame.quit()
                sys.exit()
            
            
        
        #window.blit(imagen_background,(0,0))
        shoot.draw(window)          

        player.draw(window)          
        pygame.display.update()
run_game()
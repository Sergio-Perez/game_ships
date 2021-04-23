import pygame,sys
from pygame.locals import *
from src import spaceship, missile, ufo,load_enemy, game_over
# Widht an high screen
width = 900
high = 600
color_black=(0,0,0)




        
def run_game ():
        
    pygame.init()
    pygame.mixer.init()
    window = pygame.display.set_mode((width,high))
    pygame.display.set_caption("Space ships")
    my_font_sistem = pygame.font.SysFont("Arial",30)
    text_fin_game =  my_font_sistem.render("GAME OVER",0 ,(240,30,50))
    list_enemy = []

    player = spaceship.SpaceShip()
    #for e in range(0,100,40):
    #     list_enemy += load_enemy.load_enemy_equal_character(width,e)
    #load_enemy_diferent()
    
    list_enemy += load_enemy.load_enemy_diferent()
    
    # Music
    pygame.mixer.music.load("sound/classic_intension.ogg")
    pygame.mixer.music.play(3)
    
    clock = pygame.time.Clock()
    in_play = True
    while True:
        clock.tick(250)
        window.fill(color_black)
        time= round(pygame.time.get_ticks()/1000,0)    
        
        movement = pygame.key.get_pressed()
        if in_play == True:
            if movement[pygame.K_RIGHT] :              
                player.move_right()
                
            if movement[pygame.K_LEFT]:                    
                player.move_left()               

            if movement[pygame.K_UP]:                            
                player.move_up() 
                                    
            if movement[pygame.K_DOWN]:              
                player.move_bottom()  
                                 

        for event in pygame.event.get():
            if event.type == QUIT:
                pygame.quit()
                sys.exit()
            if event.type == pygame.KEYDOWN:
                if event.key == K_SPACE:
                    x,y = player.rect.center
                    player.shoot(x,y)
                
            
            
        
        #window.blit(imagen_background,(0,0))
             
        player.draw(window)
        # shoot player
        if len(player.list_shoot)>0: 
           for  shoot in player.list_shoot:
                shoot.draw(window)
                shoot.trajectory()
                
                if shoot.rect.top ==0:
                    player.list_shoot.remove(shoot)
                else:
                    for enemy in list_enemy:
                        if shoot.rect.colliderect(enemy.rect):
                            list_enemy.remove(enemy)
                            player.list_shoot.remove(shoot)
                            pygame.mixer.music.load("sound/efects/Explosion+1.wav")
                            pygame.mixer.music.play()
                        
                    
        if len(list_enemy)>0:
            for enemy in list_enemy:
                enemy.behaviour(int(time))
                enemy.draw(window)                   
                if enemy.rect.colliderect(player.rect):
                    in_play= False
                    game_over.game_over(list_enemy)
                    player.destructions()

                    
            # shoot enemy 
                if len(enemy.list_shoot)>0: 
                    for  shoot in enemy.list_shoot:
                        shoot.draw(window)
                        shoot.trajectory()
                        
                        if shoot.rect.colliderect(player.rect):
                            enemy.list_shoot.remove(shoot)                            
                            in_play= False
                            game_over.game_over(list_enemy)
                            player.destructions()

                               
                        if shoot.rect.top >width:
                            enemy.list_shoot.remove(shoot)
                        else:
                            for shoot_player in player.list_shoot:
                                if shoot.rect.colliderect(shoot_player.rect):
                                    player.list_shoot.remove(shoot_player)
                                    enemy.list_shoot.remove(shoot)
                                    
        if in_play == False:
            pygame.mixer.music.fadeout(3000)
            window.blit(text_fin_game,(width/2-100,high/2))                
            
        pygame.display.update()
run_game()
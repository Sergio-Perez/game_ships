import pygame,sys
from pygame.locals import *
import time
from src import spaceship, load_enemy, game_over,lifes, conf

# Widht an conf.high screen





       
def run_game (life_player,level_run):
        
    pygame.init()
    pygame.mixer.init()
    window = pygame.display.set_mode((conf.width,conf.high))
    pygame.display.set_caption("Space ships")
    
    my_font_sistem = pygame.font.SysFont("Arial",30)
    text_fin_game =  my_font_sistem.render("GAME OVER",0 ,(240,30,50))
    list_enemy = []
    
    #score
    scores=0
    my_font_score = pygame.font.SysFont("Arial",10)
    score = my_font_score.render(f"Score : {scores}",0,(245,25,7))
    

    # load heart
    life_window = []
    life_window +=  lifes.draw_all_lifes(numbers = life_player,
                                         pos_x= conf.width,
                                         pos_y =0)

    # load my player
    player = spaceship.SpaceShip()    
    velocity_enemy = 1
    # enemies
    list_enemy += load_enemy.load_enemy_diferent(velocity_enemy)

    # level 
    level = level_run

    
    # Music
    pygame.mixer.music.load("sound/classic_intension.ogg")
    pygame.mixer.music.play(-1)
     
  
    
    clock = pygame.time.Clock()
    in_play = True
    while True:
        levels_window = my_font_score.render(f"Level: {level}",0,(245,25,7))


        clock.tick(250)
        window.fill(conf.color_black)
        timer= round(pygame.time.get_ticks()/1000,0)    
        
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
                in_play = False

                pygame.quit()
                sys.exit()
                
            if event.type == pygame.KEYDOWN:
                if event.key == K_SPACE:
                    x,y = player.rect.center
                    player.shoot(x,y)
                
            
            
        
        #window.blit(imagen_background,(0,0))
       
        player.draw(window)
        if len(life_window)>0:
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
                                try:
                                    player.list_shoot.remove(shoot)
                                except:
                                    pass
                                scores +=5
                                score = my_font_score.render(f"Score : {scores}",0,(245,25,7))

                                window.blit(score,(0,0))



                                pygame.mixer.music.load("sound/efects/Explosion+1.wav")
                                pygame.mixer.music.play()
                                pygame.display.flip()    

                            
                        
            if len(list_enemy)>0:
                for enemy in list_enemy:
                    enemy.behaviour(int(timer))
                    enemy.timeChange = timer

                    enemy.draw(window)                   
                    if enemy.rect.colliderect(player.rect):
                        in_play= False
                        game_over.game_over(list_enemy)               
                        player.destructions()
                        del  life_window[-1]
                        pygame.display.flip()
                        life_player -=1
                        time.sleep(3)
                        timer = 0
                        if life_player>0:
                            run_game(life_player,level_run)     
                        else :
                            in_play == False            

         
                        
                # shoot enemy 
                    if len(enemy.list_shoot)>0: 
                        for  shoot in enemy.list_shoot:
                            shoot.draw(window)
                            shoot.trajectory()
                            
                            if shoot.rect.colliderect(player.rect):
                                enemy.list_shoot.remove(shoot)  
                                timer = 0
                          
                                in_play= False
                                game_over.game_over(list_enemy)
                                player.list_shoot=[]                        
                                del life_window[-1]
                                player.destructions()
                                pygame.display.flip()
                                life_player -=1
                                time.sleep(2)

                                if life_player>0:
                                     run_game(life_player,level_run)     
                                else :
                                    in_play == False     

                                    


                                
                            if shoot.rect.top >conf.width:
                                enemy.list_shoot.remove(shoot)
                            else:
                                for shoot_player in player.list_shoot:
                                    if shoot.rect.colliderect(shoot_player.rect):
                                        player.list_shoot.remove(shoot_player)
                                        enemy.list_shoot.remove(shoot)

                               
            elif len(list_enemy) == 0:
                
                end_game = my_font_sistem.render(f"Finish level {level}",0,(245,25,7))

                window.blit(end_game,(conf.width/2-100,conf.high/2)) 
                level += 1

                pygame.display.flip()

                time.sleep(3)
                player.rect.top = conf.high
                player.rect.left = conf.width/2 -100
                
                list_enemy += load_enemy.load_enemy_diferent(level/2)                  


                  
                      
        if in_play == False :
            pygame.mixer.music.fadeout(3000)
            player.rect.centerx = conf.width/2
            player.rect.centery = conf.high-30
            window.blit(text_fin_game,(conf.width/2-100,conf.high-2*(conf.high/3)))                
        
        window.blit(score,(0,0))
        window.blit(levels_window,(conf.width/2,0)) 
       
        if len(life_window)>0 :
            for live in life_window:                
                live.draw(window)  

        pygame.display.update()
        
        
        
run_game(conf.life_player,conf.level)
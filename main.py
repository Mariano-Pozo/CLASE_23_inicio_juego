import pygame
from pygame.locals import *
import sys
from constantes import *
from player import Player
from enemigo import Enemy
from plataforma import Plataform
from botin import Coins

flags = DOUBLEBUF

screen = pygame.display.set_mode((ANCHO_VENTANA,ALTO_VENTANA), flags, 16)
pygame.init()
clock = pygame.time.Clock()

imagen_fondo = pygame.image.load("images/background/image (3).png").convert()


imagen_fondo = pygame.transform.scale(imagen_fondo,(ANCHO_VENTANA,ALTO_VENTANA))

player_1 = Player(x=0,y=400,speed_walk=10,speed_run=12,gravity=14,jump_power=35,frame_rate_ms=75,move_rate_ms=50,jump_height=140,p_scale=3,interval_time_jump=300)

enemy_list = []
enemy_list.append(Enemy(x=500,y=400,speed_walk=4,speed_run=4,gravity=8,frame_rate_ms=85,move_rate_ms=50,jump_power=30,jump_height=140,p_scale=3))
enemy_list.append(Enemy(x=900,y=400,speed_walk=4,speed_run=4,gravity=8,frame_rate_ms=85,move_rate_ms=50,jump_power=30,jump_height=140,p_scale=3))
coin_list = []
coin_list.append(Coins(xx=300 , yy=422, width=8, height=8, type=1))
coin_list.append(Coins(xx=300 , yy=322, width=8, height=8, type=1))
coin_list.append(Coins(xx=300 , yy=388, width=8, height=8, type=1))
coin_list.append(Coins(xx=300 , yy=400, width=8, height=8, type=1))

plataform_list = []
# plataform_list.append(Plataform(x=400,y=580,width=50,height=50,type=0))
# plataform_list.append(Plataform(x=450,y=580,width=50,height=50,type=1))
# plataform_list.append(Plataform(x=500,y=580,width=50,height=50,type=2))
# plataform_list.append(Plataform(x=600,y=550,width=50,height=50,type=12))
# plataform_list.append(Plataform(x=650,y=550,width=50,height=50,type=14))
# plataform_list.append(Plataform(x=750,y=480,width=50,height=50,type=12))
# plataform_list.append(Plataform(x=800,y=480,width=50,height=50,type=13))
# plataform_list.append(Plataform(x=850,y=480,width=50,height=50,type=13))
# plataform_list.append(Plataform(x=900,y=480,width=50,height=50,type=14))
# plataform_list.append(Plataform(x=950,y=480,width=50,height=50,type=15))
         
while True:     
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            pygame.quit()
            sys.exit()

    keys = pygame.key.get_pressed()


    delta_ms = clock.tick(FPS)
    screen.blit(imagen_fondo,imagen_fondo.get_rect())

    for plataforma in plataform_list:
        plataforma.draw(screen)

    for enemy_element in enemy_list:
        enemy_element.update(delta_ms,plataform_list)
        enemy_element.draw(screen)

    for coin in coin_list:
        coin.draw(screen)
    
        
    
    player_1.events(delta_ms,keys)
    player_1.update(delta_ms,plataform_list,coin_list)
    player_1.draw(screen)
    



    #print(delta_ms)
    # enemigos update
    # player dibujarlo
    # dibujar todo el nivel

    pygame.display.flip()
    
    #print(delta_ms)



    


  




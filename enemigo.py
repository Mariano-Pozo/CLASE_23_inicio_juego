import pygame
from player import *
from constantes import *
from auxiliar import Auxiliar


class Enemy():
    
    def __init__(self,x,y,speed_walk,speed_run,gravity,jump_power,frame_rate_ms,move_rate_ms,jump_height,p_scale=1,interval_time_jump=100) -> None:
        
        self.walk_r = Auxiliar.getSurfaceFromSeparateFiles("images\caracters\enemies\ork_sword\IDLE\enemyrangewalking ({}).png",1,4,scale=p_scale)
        self.walk_l = Auxiliar.getSurfaceFromSeparateFiles("images\caracters\enemies\ork_sword\IDLE\enemyrangewalking ({}).png",1,4,flip=True,scale=p_scale)
        self.stay_r = Auxiliar.getSurfaceFromSeparateFiles("images\caracters\enemies\ork_sword\IDLE\enemyrangestay (1).png",1,1,scale=p_scale)
        self.stay_l = Auxiliar.getSurfaceFromSeparateFiles("images\caracters\enemies\ork_sword\IDLE\enemyrangestay (1).png",1,1,flip=True,scale=p_scale)
        self.hit_r = Auxiliar.getSurfaceFromSeparateFiles("images\caracters\enemies\ork_sword\IDLE\enemyrangeashot ({}).png",1,5,scale=p_scale)
        self.hit_l = Auxiliar.getSurfaceFromSeparateFiles("images\caracters\enemies\ork_sword\IDLE\enemyrangeashot ({}).png",1,5,scale=p_scale)

        self.ultimo_disparo=0
        self.contador = 0
        self.frame = 0
        self.lives = 5
        self.score = 0
        self.move_x = 0
        self.move_y = 0
        self.speed_walk =  speed_walk
        self.speed_run =  speed_run
        self.gravity = gravity
        self.jump_power = jump_power
        self.animation = self.stay_r
        self.direction = DIRECTION_R
        self.image = self.animation[self.frame]
        self.rect = self.image.get_rect()
        self.rect.x = x
        self.rect.y = y
        self.collition_rect = pygame.Rect(x+self.rect.width/3,y,self.rect.width/3,self.rect.height)
        self.ground_collition_rect = pygame.Rect(self.collition_rect)
        self.ground_collition_rect.height = GROUND_COLLIDE_H
        self.ground_collition_rect.y = y + self.rect.height - GROUND_COLLIDE_H

        self.is_jump = False
        self.is_fall = False
        self.is_shoot = False
        self.is_knife = False

        self.tiempo_transcurrido_animation = 0
        self.frame_rate_ms = frame_rate_ms 
        self.tiempo_transcurrido_move = 0
        self.move_rate_ms = move_rate_ms
        self.y_start_jump = 0
        self.jump_height = jump_height

        self.tiempo_transcurrido = 0
        self.tiempo_last_jump = 0 # en base al tiempo transcurrido general
        self.interval_time_jump = interval_time_jump
   
    def change_x(self,delta_x):
        self.rect.x += delta_x
        self.collition_rect.x += delta_x
        self.ground_collition_rect.x += delta_x

    def change_y(self,delta_y):
        self.rect.y += delta_y
        self.collition_rect.y += delta_y
        self.ground_collition_rect.y += delta_y

    def do_movement(self,delta_ms,plataform_list):
        self.tiempo_transcurrido_move += delta_ms
        if(self.tiempo_transcurrido_move >= self.move_rate_ms):
            self.tiempo_transcurrido_move = 0

            if(not self.is_on_plataform(plataform_list)):
                if(self.move_y == 0):
                    self.is_fall = True
                    self.change_y(self.gravity)
            else:
                self.is_fall = False
                self.change_x(self.move_x)
                if self.contador <= 50:
                    self.move_x = -self.speed_walk
                    self.animation = self.walk_l
                    self.contador += 1 
                    self.direction = DIRECTION_L
                elif self.contador <= 100:
                    self.move_x = self.speed_walk
                    self.animation = self.walk_r
                    self.contador += 1
                    self.direction = DIRECTION_R

                else:
                    self.contador = 0
    
    def is_on_plataform(self,plataform_list):# aqui tendria que ir la colision del enemigo con la bala del jugador
        retorno = False
        
        if(self.ground_collition_rect.bottom >= GROUND_LEVEL):
            retorno = True     
        else:
            for plataforma in  plataform_list:
                if(self.ground_collition_rect.colliderect(plataforma.ground_collition_rect)):
                    retorno = True
                    break       
        return retorno
    def is_on_player(self,enemy_list):
        retorno = False
        
        if(self.ground_collition_rect.bottom >= GROUND_LEVEL):
            retorno = True     
        else:
            for plataforma in  enemy_list:
                if(self.ground_collition_rect.colliderect(plataforma.ground_collition_rect)):
                    retorno = True
                    break       
        return retorno          

    def do_animation(self,delta_ms):
        self.tiempo_transcurrido_animation += delta_ms
        if(self.tiempo_transcurrido_animation >= self.frame_rate_ms):
            self.tiempo_transcurrido_animation = 0
            if(self.frame < len(self.animation) - 1):
                self.frame += 1 
                #print(self.frame)
            else: 
                self.frame = 0

    def can_shoot(self):
        contador_disparo = pygame.time.get_ticks() 
        if contador_disparo - self.ultimo_disparo > 2000:
            self.ultimo_disparo = contador_disparo
            return True
        else:
            return False


    def puede_golpear_jugador(self,jugador):
        return self.collition_rect.colliderect(jugador.rect_disparos) and self.can_shoot() and jugador.lives > 0 and self.lives >0


    def automatic_shoot(self,jugador,lista):
        self.contador_cd = pygame.time.get_ticks() 
        if self.puede_golpear_jugador(jugador):
            if self.direction == DIRECTION_R:
                lista.append(Bullet(self, self.rect.right, self.rect.centery, 1800, self.rect.centery, 5, path="images/caracters/enemies/ork_sword/IDLE/bullet (1).png", frame_rate_ms=50, move_rate_ms=20, width=8, height=10))
               
                
            elif self.direction != DIRECTION_R:
                lista.append(Bullet(self, self.rect.left, self.rect.centery, 0, self.rect.centery, 5, path="images/caracters/enemies/ork_sword/IDLE/bullet (1).png", frame_rate_ms=50, move_rate_ms=20, width=8, height=10))
            
    def do_knife(self,jugador):
        if self.collition_rect.colliderect(jugador.collition_rect) and self.can_shoot():
            self.melee_attack(jugador)


    def melee_attack(self,jugador):  
        
        if(self.is_jump == False and self.is_fall == False):
            if(self.animation != self.hit_r and self.animation != self.hit_l):
                self.frame = 0
                if(self.direction == DIRECTION_R):
                    self.animation = self.hit_r
                else:
                    self.animation = self.hit_l      
                jugador.receive_shoot()
        


    def update(self,delta_ms,plataform_list,jugador,lista):
        self.do_movement(delta_ms,plataform_list)
        self.do_animation(delta_ms)
        self.automatic_shoot(jugador,lista)
        self.do_knife(jugador)
        

    def draw(self,screen):
        
        if(DEBUG):
            pygame.draw.rect(screen,color=(255,0 ,0),rect=self.collition_rect)
            pygame.draw.rect(screen,color=(255,255,0),rect=self.ground_collition_rect)
        
        self.image = self.animation[self.frame]
        screen.blit(self.image,self.rect)

    def receive_shoot(self):
        self.lives -= 1

    

    def kill_enemy(self):
        self.lives -= 1
        if self.lives <= 0:
            Player.score += 1000

    
    



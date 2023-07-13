import pygame
import time
from auxiliar import Auxiliar
from pygame.locals import *
from constantes import *
from gui_form import Form
from gui_button import Button
from gui_textbox import TextBox
from gui_progressbar import ProgressBar
from player import Player
from enemigo import Enemy
from plataforma import Plataform
from background import Background
from bullet import Bullet
from botin import Coins
from trap import Fire
from boss import Boss


class FormGameLevel3(Form):
    def __init__(self,name,master_surface,x,y,w,h,color_background,color_border,active):
        super().__init__(name,master_surface,x,y,w,h,color_background,color_border,active)

        # --- GUI WIDGET --- 
        self.boton1 = Button(master=self,x=0,y=0,w=140,h=50,color_background=None,color_border=None,
                             image_background="images/gui/set_gui_01/Comic_Border/Buttons/Button_M_02.png",
                             on_click=self.on_click_boton1,on_click_param="form_menu_levels",text="BACK",font="Verdana",
                             font_size=30,font_color=C_WHITE)
        self.boton2 = Button(master=self,x=200,y=0,w=140,h=50,color_background=None,color_border=None,
                             image_background="images/gui/set_gui_01/Comic_Border/Buttons/Button_M_02.png",
                             on_click=self.on_click_boton1,on_click_param="form_menu_B",text="PAUSE",font="Verdana",
                             font_size=30,font_color=C_WHITE)
        #self.boton_shoot = Button(master=self,x=400,y=0,w=140,h=50,color_background=None,color_border=None,image_background="images/gui/set_gui_01/Comic_Border/Buttons/Button_M_02.png",on_click=self.on_click_shoot,on_click_param="form_menu_B",text="SHOOT",font="Verdana",font_size=30,font_color=C_WHITE)
       
        self.pb_lives = ProgressBar(master=self,x=500,y=50,w=240,h=50,color_background=None,color_border=None,image_background="images/gui/set_gui_01/Comic_Border/Bars/Bar_Background01.png",image_progress="images/gui/set_gui_01/Comic_Border/Bars/Bar_Segment05.png",value = 5, value_max=5)
        self.widget_list = [self.boton1,self.boton2,self.pb_lives]#self.boton_shoot

        # --- GAME ELEMNTS --- 
        self.static_background = Background(x=0,y=0,width=w,height=h,path="images/background/image (3).png")
        # data extraida del json
        datos_extraidos = Auxiliar.leer_json("config.json")

        self.player_1 = Player(x=0,y=400,speed_walk=10,speed_run=12,gravity=14,jump_power=35,frame_rate_ms=100,move_rate_ms=50,jump_height=140,p_scale=3,interval_time_jump=300)
        self.boss = Boss(x=1050,y=500,speed_walk=0,speed_run=0,gravity=18,frame_rate_ms=100,move_rate_ms=50,jump_power=30,jump_height=150,p_scale=3)
    
        self.trap_list = []
        for Traps in datos_extraidos["niveles"]["nivel_3"]["config_trap"]:
            x,y,w,h= Traps
            self.trap_list.append(Fire(x,y,w,h))

        self.enemy_list = []
        for Enemigos in datos_extraidos["niveles"]["nivel_3"]["config_enemigos"]:
            x,y,speed_walk,speed_run,gravity,frame_rate_ms,move_rate_ms,jump_power,jump_height,p_scale = Enemigos
            self.enemy_list.append(Enemy(x,y,speed_walk,speed_run,gravity,frame_rate_ms,move_rate_ms,jump_power,jump_height,p_scale))
           
        self.enemy_list.append(self.boss)
        
        
        self.plataform_list = []
        for Plataforma in datos_extraidos["niveles"]["nivel_3"]["config_plataformas"]:
            x,y,w,h,tipo= Plataforma
            self.plataform_list.append(Plataform(x,y,w,h,tipo))
            
        ##listas coin
        self.coin_list = []
        for Coin in datos_extraidos["niveles"]["nivel_3"]["config_coins"]:
            xx,yy,width,height,tipo= Coin
            self.coin_list.append(Coins(xx,yy,width,height,tipo))

        ##disparos
        self.bullet_list = []

        #Timer
        self.is_paused = False
        self.start_time = 0
        self.elapsed_time = 0
        self.player_moved = False

        #imgtimer
        self.clock_background = pygame.image.load("images/gui/set_gui_01/Comic_Border/Buttons/Button_M_02.png").convert_alpha()
        self.clock_background = pygame.transform.scale(self.clock_background, (100, 50))

        #scoreimg
        self.score_image = pygame.image.load("images/gui/set_gui_01/Comic_Border/Buttons/Button_M_02.png").convert_alpha()
        self.score_image = pygame.transform.scale(self.score_image, (200, 50))

        #--img g over
        self.game_over_image = pygame.image.load("images\caracters\enemies\ork_sword\IDLE\gameover.png").convert_alpha()
        self.game_over_image = pygame.transform.scale(self.game_over_image,(400,150)).convert_alpha()
        self.game_over_image_rect = self.game_over_image.get_rect(center=(self.master_surface.get_width() // 2, self.master_surface.get_height() // 2))

        # IMG WINNER
        self.winner_image = pygame.image.load("images/background/mision completee.png" ).convert_alpha()
        self.winner_image = pygame.transform.scale(self.winner_image,(400,150)).convert_alpha()
        self.winner_image_rect = self.winner_image.get_rect(center=(self.master_surface.get_width() // 2, self.master_surface.get_height() // 4))

        # CD Shoot
        self.can_shoot = True
        self.can_shoot_player = True
        self.shoot_cooldown = 1000
        self.last_shoot_time = 0   

    def on_click_boton1(self, parametro):
        self.set_active(parametro)

    def update(self, lista_eventos,keys,delta_ms):
        for trap_element in self.trap_list:
            trap_element.loop()
            trap_element.update(delta_ms,self.plataform_list)
            trap_element.check_colision(self.player_1)

        for aux_widget in self.widget_list:
            aux_widget.update(lista_eventos)

        for bullet_element in self.bullet_list:
            bullet_element.update(delta_ms,self.plataform_list,self.enemy_list,self.player_1)

        for enemy_element in self.enemy_list:
            enemy_element.update(delta_ms,self.plataform_list,self.player_1,self.bullet_list)

        for enemy in self.enemy_list:
            
            if pygame.key.get_pressed()[pygame.K_a] and self.player_1.rect.colliderect(enemy.rect) and self.player_1.rect.top < enemy.rect.bottom:

                enemy.lives -= 1
                if enemy.lives <= 0 :
                    self.enemy_list.remove(enemy)
                    self.player_1.score += 10
                    self.pb_lives.value = self.player_1.lives

                break  # Termina el bucle una vez que se encuentra el enemigo correspondiente
            

        if not self.player_moved:
            if keys[K_LEFT] or keys[K_RIGHT]:
                self.player_moved = True
                self.start_time = time.time()
                pygame.mixer.music.load("soundtracks\Megaman Zero 3_ Trail on Powdery Snow (320 kbps).mp3")
                pygame.mixer.music.play(-1)


        
        self.player_1.events(delta_ms,keys,self.bullet_list,self.enemy_list)
        self.player_1.update(delta_ms,self.plataform_list,self.coin_list)
        if self.player_1.lives <= 0:
            self.surface.blit(self.game_over_image, self.game_over_image_rect)
            self.is_paused = True

        if len(self.enemy_list) == 0:
            self.surface.blit(self.winner_image, self.winner_image_rect)
            self.is_paused = True
            self.on_click_boton1("form_menu_levels")
        
        self.pb_lives.value = self.player_1.lives 
    
    def draw(self): 
        super().draw()
        self.static_background.draw(self.surface)
        self.player_1.draw(self.surface)
        

        for aux_widget in self.widget_list:    
            aux_widget.draw()

        for plataforma in self.plataform_list:
            plataforma.draw(self.surface)

        for enemy_element in self.enemy_list:
            enemy_element.draw(self.surface)

        for bullet_element in self.bullet_list:
            bullet_element.draw(self.surface)

        for coin in self.coin_list:
            coin.draw(self.surface)

        for trampa in self.trap_list:
            trampa.draw(self.surface)

        #SCORE
        self.surface.blit(self.score_image, (170, 0))
        score_font = pygame.font.SysFont("Verdana", 30)  # Fuente para el texto del score
        score_text = score_font.render("SCORE: " + str(self.player_1.score * 100), True, (255, 255, 255))  # Renderiza el texto del score
        self.surface.blit(score_text, (200, 15))

        # timer
        if not self.is_paused and self.player_moved:
            current_time = int(time.time() - self.start_time + self.elapsed_time)
            minutes = current_time // 60
            seconds = current_time % 60
            clock_rect = self.clock_background.get_rect(topright=(self.master_surface.get_width() - 200, 50))
            self.surface.blit(self.clock_background, clock_rect)
            clock_text = pygame.font.SysFont("Verdana", 30).render(f"{minutes:02d}:{seconds:02d}", True, (255, 255, 255))
            clock_text_rect = clock_text.get_rect(center=clock_rect.center)
            self.surface.blit(clock_text, clock_text_rect)
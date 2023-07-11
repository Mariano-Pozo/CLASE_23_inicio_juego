import pygame
import pygame.mixer
from pygame.locals import *
from gui_form import Form
from gui_button import Button
from constantes import *

class FormMenuSettings(Form):
    def __init__(self,name,master_surface,x,y,w,h,color_background,color_border,active):
        super().__init__(name,master_surface,x,y,w,h,color_background,color_border,active)
        # Inicializar el motor de sonido
        pygame.mixer.init()
        # Cargar el sonido de fondo
        pygame.mixer.music.load("soundtracks/Megaman Zero 1_ Zero Theme. (320 kbps).mp3")
        # Iniciar la reproducción del sonido 
        pygame.mixer.music.play(-1)
        # BACK
        self.boton1 = Button(master = self, x = 20, y = 180, w = 180, h = 80,
            color_background = None, color_border = None,image_background = "images\gui\set_gui_01\Comic_Border\Buttons\Button_XL_06.png",
            on_click = self.on_click_boton1,on_click_param = "form_game_L1",text = "BACK",font = "Times",font_size = 30,font_color = C_BLACK)
        # vol+
        self.boton2 = Button(master = self, x = 20, y = 20, w = 180, h = 80, color_background = None,
            color_border = None, image_background = "images/gui/set_gui_01/Comic_Border/Buttons/Button_XL_06.png", 
            on_click = self.on_click_boton2,on_click_param = "settings",text = "VOL+",font = "Times",font_size = 30,font_color = C_BLACK)
        # vol-
        self.boton3 = Button(master = self, x = 20, y = 100, w = 180, h = 80, 
            color_background = None, color_border = None, image_background = "images\gui\set_gui_01\Comic_Border\Buttons\Button_XL_06.png", 
            on_click = self.on_click_boton3,on_click_param = "settings",text = "VOL-",font = "Times",font_size = 30,font_color = C_BLACK)
        # MUTE
        self.boton4 = Button(master = self, x = 20, y = 260, w = 180, h = 80, 
            color_background = None, color_border = None, image_background = "images\gui\set_gui_01\Comic_Border\Buttons\Button_XL_06.png", 
            on_click = self.on_click_boton4,on_click_param = "settings",text = "MUTE",font = "Times",font_size = 30,font_color = C_BLACK)

        self.lista_widget = [self.boton1,self.boton2,self.boton3,self.boton4]

    def on_click_boton1(self, parametro):
        self.set_active(parametro)
    
    def on_click_boton2(self, parametro):
        pygame.mixer.music.set_volume(1)

    def on_click_boton3(self,parametro):
        pygame.mixer.music.set_volume(0.2)  # Reducir el volumen a la mitad (0.0 - 1.0)
    
    def on_click_boton4(self,parametro):
        pygame.mixer.music.set_volume(0)

    

    def update(self, lista_eventos, keys, delta_ms):
        for aux_widget in self.lista_widget:
            aux_widget.update(lista_eventos)

    def draw(self): 
        super().draw()

        for aux_widget in self.lista_widget:
            aux_widget.draw()



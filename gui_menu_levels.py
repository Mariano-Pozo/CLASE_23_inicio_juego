import pygame
import pygame.mixer
from pygame.locals import *
from constantes import *
from gui_form import Form
from gui_button import Button


class FormMenuLevels(Form):
    def __init__(self,name,master_surface,x,y,w,h,color_background,color_border,active):
        super().__init__(name,master_surface,x,y,w,h,color_background,color_border,active)
        # Imagen del fondo del menu principal
        screen = pygame.display.set_mode((ANCHO_VENTANA,ALTO_VENTANA))
        imagen_fondo = pygame.image.load("images\gui\set_gui_01\Standard\Buttons\Button_S_07.png")
        imagen_fondo = pygame.transform.scale(imagen_fondo, (ANCHO_VENTANA,ALTO_VENTANA))
        pygame.display.set_caption("zero")
        screen.blit(imagen_fondo,imagen_fondo.get_rect())
        # Imagen fondo de los botones
        imagen_fondo_botones = pygame.image.load("images\gui\set_gui_01\Standard\Buttons\Button_L_05.png")
        imagen_fondo_botones = pygame.transform.scale(imagen_fondo_botones, (420, 420))
        imagen_fondo_botones_rect = imagen_fondo_botones.get_rect()
        imagen_fondo_botones_rect.center = (screen.get_width() // 2, screen.get_height() // 2 + 50)
        screen.blit(imagen_fondo_botones, imagen_fondo_botones_rect)

        # LEVEL 1
        self.boton1 = Button(master = self, x = 100, y = 0, w = 180, h = 60, color_background = None, color_border = None, image_background = "images\gui\set_gui_01\Standard\Buttons\Button_S_07.png", on_click = self.on_click_boton2, on_click_param = "form_game_L1", text = "LEVEL 1", font = "Times", font_size = 30, font_color = C_BLACK)
        # LEVEL 2
        self.boton2 = Button(master = self, x = 80, y = 60, w = 220, h = 60, color_background = None, color_border = None, image_background = "images\gui\set_gui_01\Standard\Buttons\Button_S_07.png", on_click = self.on_click_boton2, on_click_param = "form_game_L2", text = "LEVEL 2", font = "Times", font_size = 30, font_color = C_BLACK)
        # LEVEL 3
        self.boton3 = Button(master = self, x = 80, y = 120, w = 220, h = 60, color_background = None, color_border = None, image_background = "images\gui\set_gui_01\Standard\Buttons\Button_S_07.png", on_click = self.on_click_boton2, on_click_param = "form_game_L3", text = "LEVEL 3", font = "Times", font_size = 30, font_color = C_BLACK)
        # LEVEL 4
        self.boton4 = Button(master = self, x = 110, y = 180, w = 160, h = 60, color_background = None, color_border = None, image_background = "images\gui\set_gui_01\Standard\Buttons\Button_S_07.png", on_click = self.on_click_boton2, on_click_param = "form_menu_B", text = "Settings", font = "Times", font_size = 30, font_color = C_BLACK)

        # BACK
        self.boton5 = Button(master = self, x = 100, y = 240, w = 180, h = 60, color_background = None, color_border = None, image_background = "images\gui\set_gui_01\Standard\Buttons\Button_S_07.png", on_click = self.on_click_boton1, on_click_param = "form_menu_principal", text = "BACK", font = "Times", font_size = 30, font_color = C_BLACK)


        #Lista de botones que van a aparecer en nuestro menu principal
        self.lista_widget = [self.boton1, self.boton2, self.boton3, self.boton4, self.boton5]

    def on_click_boton1(self, parametro):
        self.set_active(parametro)
    
    def on_click_boton2(self, parametro):
        self.set_active(parametro)
        pygame.mixer.music.stop()

    def update(self, lista_eventos,keys,delta_ms):
        for aux_widget in self.lista_widget:
            aux_widget.update(lista_eventos)

    def draw(self): 
        super().draw()

        for aux_widget in self.lista_widget:    
            aux_widget.draw()
import pygame

from auxiliar import Auxiliar

def landed(self):
    self.fall_count =0
    self.y_vel = 0
    self.jump_count = 0
    
def hit_head(self):
    self.count = 0
    self.y_vel *= -1

def handle_vertical_collision(player,objects,dy):
    collided_objects = []
    for obj in objects:
        if pygame.sprite.collide_mask(player,obj):
            if dy > 0:
                player.rect.bottom = obj.rect.top
                player.landed()
            elif dy < 0 :
                player.rect.top = obj.rect.bottom
                player.hit_head()

        collided_objects.append(obj)

    return collided_objects


class Object(pygame.sprite.Sprite):
    def __init__(self,x,y,w,h,name=None):
        super().__init__()
        self.rect = pygame.Rect(x,y,w,h)
        self.image = pygame.Surface((w,h),pygame.SRCALPHA)
        self.width = w
        self.height = h
        self.name = name

class Block(Object):
    def __init__(self,x,y,size):
        super().__init__(x, y,size,size)
        Block = load_block(size)
        self.image.blit(lock,(b0,0))
        self.mask = pygame.mask.from_surface(self.image)
# ----------------------  ---------------------------
# clase para aplicar trampas
class Fire(Object):
    ANIMATION_DELAY = 3

    def __init__(self, x, y, width, height):
        super().__init__(x, y, width, height, "fire")
        self.fire = Auxiliar.getSurfaceFromSeparateFiles("images/caracters/enemies/ork_sword/IDLE/trap_1 (4).png", 1, 8, step=1,scale=2.5, w=width, h=height)
        self.image = self.fire[0]
        self.mask = pygame.mask.from_surface(self.image)
        self.animation_count = 0
        self.animation_name = "off"

    def on(self):
        self.animation_name = "on"

    def off(self):
        self.animation_name = "off"

    def loop(self):
        self.animation_count += 1

        self.rect = self.image.get_rect(topleft=(self.rect.x, self.rect.y))
        self.mask = pygame.mask.from_surface(self.image)

        if self.animation_count // self.ANIMATION_DELAY > len(self.fire) - 1:
            self.animation_count = 0
    
    def draw(self, surface):
        sprites = self.fire
        sprite_index = (self.animation_count // self.ANIMATION_DELAY) % len(sprites)
        self.image = sprites[sprite_index]

        surface.blit(self.image, self.rect)


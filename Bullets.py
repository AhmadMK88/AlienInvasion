import pygame 
from pygame.sprite import Sprite 

class Bullet ( Sprite ) :
   
   def __init__ (self,gsettings,screen,ship) :
        super(Bullet,self).__init__()
        self.screen = screen 
        self.rect = pygame.Rect( 0 , 0 , gsettings.bullet_width , gsettings.bullet_height )
        self.rect.centerx = ship.rect.centerx 
        self.rect.top = ship.rect.top
        self.y = float(self.rect.y)
        self.color = gsettings.bullet_color 
        self.speed_factor = gsettings.bullet_speed_factor
   
   def update(self) :
        self.y -= self.speed_factor
        self.rect.y = self.y 

   def draw_bullet(self) :
        pygame.draw.rect(self.screen,self.color, self.rect)
import pygame, sys
from pygame.locals import *
all_rss = pygame.sprite.Group()


class Resource(pygame.sprite.Sprite):
    def __init__(self, image, type, startX, startY):
        pygame.sprite.Sprite.__init__(self)
        self.image = image.convert_alpha()  # transparent image
        self.rect = self.image.get_rect().move(startX, startY)  # rect is for blitting
        self.selected = False
        pygame.sprite.Sprite.__init__(self, all_rss)
    
    def update(self):
        if self.selected:
            self.image.set_alpha(0)
        else:
            self.image.set_alpha(255)
        
        #print(self.image.get_alpha())
        
    def updatePos(self, loc):
        if self.selected:
            self.rect = self.rect.move((-0.5*self.rect.width - self.rect.left,-0.5*self.rect.height - self.rect.top))
            self.rect = self.rect.move(loc)
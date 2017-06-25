import pygame, sys, random, time, pygame.mixer, pygame.font
from pygame.locals import *
from pygame.font import *

from Resources import *

SCREEN_WIDTH = 600
SCREEN_HEIGHT = 450

size = SCREEN_WIDTH, SCREEN_HEIGHT
screen = pygame.display.set_mode(size)


background = pygame.image.load('background.png')
mine = pygame.image.load('Mine.png')

mtest = Resource(mine, 'A', 100, 100)

time = 0

while True:
    screen.blit(background, (0, 0))
    all_rss.draw(screen)
    
    for event in pygame.event.get():
        
        if event.type == pygame.QUIT:
            sys.exit()
            
        if event.type == MOUSEBUTTONDOWN:
            for rsc in  all_rss:
                print(pygame.mouse.get_pos())
                print(rsc.image.get_rect())
                if rsc.rect.collidepoint(pygame.mouse.get_pos()):
                    rsc.selected = True;
                else:
                    rsc.selected = False;
        else:
            for rsc in all_rss:
                if rsc.selected:
                    if rsc.rect.collidepoint(pygame.mouse.get_pos()) and pygame.mouse.get_pressed()[0]:
                        rsc.updatePos(pygame.mouse.get_pos())
                    else:
                        rsc.selected = False
    
    key = pygame.key.get_pressed()
    
    for rsc in all_rss:
        rsc.update();
    
    if key[K_ESCAPE]:
        sys.exit()
            
        
    pygame.display.update()
    pygame.event.pump()
        
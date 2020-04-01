#!/usr/bin/env python3
# -*- coding: utf-8 -*-

from labyrinthe import *
import time

import pygame
from pygame.locals import *

pygame.init()

"""defaut settings"""

window_resolution = (676, 676)
screen_surface = pygame.display.set_mode(window_resolution)
window_rect = pygame.Rect((20, 0), window_resolution)
pygame.display.set_caption('McGyver Escape Game')

FOND      = (100, 100, 125)

x = 322
y = 315

                
# Main Loop

continuer = 1
while continuer:    
    for event in pygame.event.get():
        if event.type == KEYDOWN or event.type == QUIT:
            continuer = 0
    screen_surface.fill(FOND)        
    draw_maze(screen_surface, level)
    screen_surface.blit(macgyver, (x, y))
    pygame.display.flip()       

pygame.quit()
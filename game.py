#!/usr/bin/env python3
# -*- coding: utf-8 -*-

from fonctions import *
from constantes import *
from labyrinthe import *
import time

import pygame
from pygame.locals import *

pygame.init()

""" game defaut settings """

# window settings
side_sprite_number = 15
sprite_size = 45
window_size = side_sprite_number * sprite_size

#window title
window_title = "MacGyver escape game"
screen = pygame.display.set_mode((window_size, window_size))

# police settings for welcome and end screens
text_size = 45
text_col = [255,255,255]
myfont = pygame.font.Font(None, text_size)
text = myfont.render("Bravo, vous avez trouvé la sortie!", True, text_col)

ether_sprite = pygame.image.load("ether.png").convert_alpha()
ether_sprite = pygame.transform.scale(ether_sprite, (40, 40))
tube_sprite = pygame.image.load("tube.png").convert_alpha()
tube_sprite = pygame.transform.scale(tube_sprite, (40, 40))
needle_sprite = pygame.image.load("needle.png").convert_alpha()
needle_sprite = pygame.transform.scale(needle_sprite, (40, 40))
syringue_sprite = pygame.image.load("syringue.png").convert_alpha()
syringue_sprite = pygame.transform.scale(syringue_sprite, (40, 40))
# character initialization
macgyver = MacGyver("macgyver.png")

# object initialization
tube = Item("tube.png")
needle = Item("needle.png")
ether = Item("ether.png")

# initialization of the maze
maze = Maze(level)

FOND = (10, 10, 10)

# Main Loop

run = 1
while run:
    
    for event in pygame.event.get():
        if not event.type == KEYDOWN:
            maze.draw_maze(screen) 
                                    
            
        if event.type == QUIT:
            run = 0
        if event.type == KEYDOWN:

        
            # checking for boundaries of the labyrinth so the 
            # hero won't go out of bounds
                
            if event.key == K_UP:
                macgyver.moves("up")
                    
            elif event.key == K_DOWN:
                macgyver.moves("down")
                    
            elif event.key == K_RIGHT:
                macgyver.moves("right")                  
                                        
            elif event.key == K_LEFT:
                macgyver.moves("left")
            
        screen.fill(FOND)                      
        maze.draw_maze(screen)                                  # setting maze
        screen.blit(macgyver.sprite, (macgyver.x, macgyver.y))  # refreshing of macgyver position
        screen.blit(tube_sprite, (tube.x, tube.y))
        screen.blit(needle_sprite, (needle.x, needle.y))
        screen.blit(ether_sprite, (ether.x, ether.y))
        pygame.display.flip()
        
    if macgyver.x > 600 and macgyver.y > 600:
            
        screen.fill(FOND)
        screen.blit(text, (90, 280))
        pygame.display.flip()

pygame.quit()
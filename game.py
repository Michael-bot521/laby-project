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
SCREEN_WIDTH = 676
SCREEN_HEIGHT = 676
pygame.display.set_caption('McGyver Escape Game')
macgyver = pygame.image.load("macgyver.png").convert_alpha()
macgyver_block = macgyver.get_rect()
macgyver_block.x = 323
macgyver_block.y = 315

espace = pygame.image.load("espace.jpg").convert_alpha()
espace = pygame.transform.scale(espace, (800, 600))
font = pygame.font.Font(None, 36)
text = font.render("Character moves Crash Test",30,(255,255,255))
accueil_text = font.render("Press Space tab to go space,"
                           " or C to continue", 50, (255, 255, 255))
                           
FOND      = (5, 10, 12)

# Main Loop

run = 1
while run:
    for event in pygame.event.get():
        if not event.type == KEYDOWN:
            screen_surface.blit(accueil_text, (75, 60))
            pygame.display.flip()
        if event.type == QUIT:
            run = 0
        if event.type == KEYDOWN:
            if event.key == K_SPACE:
                print("Espace")
                screen_surface.blit(espace, (0, 0))
                pygame.display.flip()
            if event.key == K_c:
                draw_maze(screen_surface, level)
                screen_surface.blit(text, (240, 440))
                screen_surface.blit(macgyver, macgyver_block)
                pygame.display.flip()                
            if event.key == K_UP:
                for y in range(45):
                    time.sleep(.012)
                    macgyver_block.y -= 1
                    draw_maze(screen_surface, level)
                    screen_surface.blit(macgyver, macgyver_block)
                    pygame.display.flip()
            if event.key == K_DOWN:
                for y in range(45):
                    time.sleep(.012)
                    macgyver_block.y += 1
                    draw_maze(screen_surface, level)
                    screen_surface.blit(macgyver, macgyver_block)
                    pygame.display.flip()
            if event.key == K_RIGHT:
                for x in range(45):
                    time.sleep(.012)
                    macgyver_block.x += 1
                    draw_maze(screen_surface, level)
                    screen_surface.blit(macgyver, macgyver_block)
                    pygame.display.flip()    
            if event.key == K_LEFT:
                for x in range(45):
                    time.sleep(.012)
                    macgyver_block.x -= 1
                    draw_maze(screen_surface, level)
                    screen_surface.blit(macgyver, macgyver_block)
                    pygame.display.flip()
             
    pygame.display.flip()       

pygame.quit()
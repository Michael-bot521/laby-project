#!/usr/bin/env python3
# -*- coding: utf-8 -*-

import pygame
from pygame.locals import *
pygame.init()

window_resolution = (676, 676)
screen_surface = pygame.display.set_mode(window_resolution)
window_rect = pygame.Rect((20, 0), window_resolution)
pygame.display.set_caption('McGyver Escape Game')

FOND      = (100, 100, 125)

""" Converting and scaling pictures if necessary """

macgyver = pygame.image.load("macgyver.png").convert_alpha()
macgyver_block = macgyver.get_rect()
wall = pygame.image.load("wall_sprite.png").convert_alpha()
wall = pygame.transform.scale(wall, (45, 45))
floor = pygame.image.load("floor_sprite.png").convert_alpha()
floor = pygame.transform.scale(floor, (45, 45))
sentinelle = pygame.image.load("sentinelle.png").convert_alpha()
start = pygame.image.load("start_sprite.png").convert_alpha()
start = pygame.transform.scale(start, (45, 45))

""" Maze architecture """

level = [
    [0, 0, 0, 1, 4, 1, 0, 0, 0, 1, 0, 0, 0, 0, 1],
    [0, 1, 0, 1, 0, 1, 0, 1, 0, 0, 0, 0, 1, 0, 0],
    [0, 1, 0, 0, 0, 1, 1, 0, 0, 0, 0, 0, 1, 1, 0],
    [0, 0, 1, 1, 0, 0, 0, 0, 1, 0, 0, 0, 1, 1, 0],
    [1, 0, 1, 0, 0, 1, 0, 0, 1, 0, 0, 1, 0, 0, 0],
    [1, 0, 0, 1, 0, 1, 1, 1, 1, 1, 0, 0, 1, 1, 1],
    [1, 1, 0, 0, 0, 1, 0, 0, 0, 1, 1, 0, 0, 0, 0],
    [1, 0, 0, 0, 0, 1, 0, 0, 0, 1, 1, 0, 0, 1, 0],
    [1, 0, 1, 0, 0, 1, 1, 1, 1, 1, 1, 0, 0, 1, 0],
    [1, 0, 1, 0, 0, 0, 0, 0, 1, 0, 0, 0, 0, 1, 0],
    [0, 0, 1, 0, 0, 0, 0, 0, 1, 1, 0, 1, 0, 1, 1],
    [0, 1, 1, 0, 0, 0, 1, 1, 1, 0, 0, 1, 0, 1, 1],
    [0, 1, 0, 0, 0, 0, 0, 0, 1, 0, 0, 1, 0, 0, 0],
    [0, 0, 1, 1, 0, 0, 0, 1, 1, 1, 0, 1, 1, 1, 1],
    [1, 0, 0, 1, 1, 1, 1, 1, 1, 1, 0, 0, 0, 0, 7],
    ]
 
def draw_maze(surface, level):
    """drawing the maze.
 
    Use surface "wall" to draw sprites with value == 1
    and surface "floor" for sprites with value == 0  """

    for j, line in enumerate(level):
        for i, case in enumerate(line):
            if case == 1:
                surface.blit(wall, (i*45, j*45))
            elif case == 0:
                surface.blit(floor, (i*45, j*45))
            elif case == 4:
                surface.blit(start, (i*45, j*45))
            elif case == 7:
                surface.blit(sentinelle, (i*45, j*45))
                
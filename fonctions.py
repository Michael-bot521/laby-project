#!/usr/bin/env python3
# -*- coding: utf-8 -*-

""" Classes and methods for the game Macgyver """

import pygame
from pygame.locals import *
from constantes import *
from labyrinthe import *
from random import *
import time

side_sprite_number = 15
sprite_size = 45
window_size = side_sprite_number * sprite_size

screen = pygame.display.set_mode((window_size, window_size)) 


class Maze:
    """class that build the maze"""
    def __init__(self, level):
        self.level = level
        
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
        
    
    def draw_maze(self, screen):
        """drawing the maze"""

        """Use surface "wall" to draw sprites with value == 1
        and surface "floor" for sprites with value == 0""" 

        for j, line in enumerate(level):
            for i, sprite in enumerate(line):
                if sprite == 1:
                    screen.blit(wall, (i*45, j*45))
                elif sprite == 0:
                    screen.blit(floor, (i*45, j*45))
                elif sprite == 4:
                    screen.blit(start, (i*45, j*45))
                elif sprite == 7:
                    screen.blit(sentinelle, (i*45, j*45))
                    
"""   
    def macgyver_tracker():
        check if macgyver next move is not on wall
    
    def macgyver_end():
        check if macgyver meet the guard
        check if macgyver has found 3 items when showing to the guard"""
      

class MacGyver:
    "class which creates main character"
    def __init__(self, sprite):
        # Character Sprites
        self.sprite = pygame.image.load(sprite).convert_alpha()
        # start position       
        self.x = 188
        self.y = 0
        # Default direction side
        
        
    def moves(self, direction):
        

        # Move to the right
        if direction == "right":
            # Check for not going out of bounds
            # Move on next sprite

            self.x += 45

        elif direction == "left":
                # Check for not going out of bounds
                # Move on next sprite
            self.x -= 45

        elif direction == "down":
                    # Check for not going out of bounds
                    # Move on next sprite

            self.y += 45

        elif direction == "up":
                        # Check for not going out of bounds
                        # move on next sprite
            self.y -= 45
            
        
class Item:
    def __init__(self, picture):
        self.picture = pygame.image.load(picture).convert_alpha()
        self.x = (randint(1, 15) * 45 + 2)
        self.y = (randint(1, 15) * 45 + 2)
        
        
        
class Guard:
    def __init__(self, sprite, position):
        sprite
        position

#!/usr/bin/python3
# -*- coding: Utf-8 -*

"""
Donkey Kong maze game
Move DK in the maze without touching the walls and reach the bananas to win

Python Script that will use the following files:
dkmaze.py, constants.py, classes.py, functions.py
"""

# Libraries imports
import pygame
from pygame.locals import *

# Local imports
from constants import *
from classes import *


# We initialize the pygame module
pygame.init()

# Pygame game window creation as a square of 750 px in order to have 15 squares of 50px per line
gameWindow = pygame.display.set_mode((window_size, window_size))

# Setting up the game icon
gameIcon = pygame.image.load(icon_image)
pygame.display.set_icon(gameIcon)

# Setting the title of the game on the Pygame window
pygame.display.set_caption(window_title)


# Loads the background image and
# Adds the background texture to our game window
background = pygame.image.load(background_img).convert()
gameWindow.blit(background, (0, 0))

# Menu & Game loops
is_game_active = False
has_game_started = False
is_game_over = False
while not is_game_active:
    # Loading the game landing page
    home = pygame.image.load(home_img).convert()
    gameWindow.blit(home, (0, 0))

    # Refresh the page
    pygame.display.flip()

    # Resetting variables until game menu is on
    has_game_started = False
    is_game_over = False

    # Game menu loop
    while not has_game_started:
        # Refresh rate limitation
        pygame.time.Clock().tick(30)

        for event in pygame.event.get():

            # If user quits, we set variables hasGameStart and isGameOver
            # back to false so we do not enter them and close the window
            if event.type == QUIT or event.type == KEYDOWN and event.key == K_ESCAPE:
                is_game_active = False
                has_game_started = False
                is_game_over = False
                # Variable to handle game level choice
                level_choice = 0

            elif event.type == KEYDOWN:
                # game level 1 handler
                if event.key == K_F1:
                    # We are now leaving the menu as the game started
                    has_game_started = True
                    level_choice = 'n1'
                # game level 2 handler
                if event.key == K_F2:
                    # We are now leaving the menu as the game started
                    has_game_started = True
                    level_choice = 'n2'

    # Now we check that the player has properly chose a game level
    if level_choice != 0:
        # Loading game's background
        background = pygame.image.load(background_img).convert()

        # Level generation based of level file
        level = Level(level_choice)
        level.generate()
        level.display(gameWindow)

        # DK character creation
        dk = Character('images/dk_right.png', 'images/dk_left.png', 'images/dk_up.png', 'images/dk_down.png', level)

    # Game loop
    while not is_game_over:
        # Refresh rate limitation
        pygame.time.Clock().tick(30)

        for event in pygame.event.get():

            # If the user quits, resets the is_game_active
            # and has_game_started variables to False
            if event.type == QUIT:
                is_game_active = False
                has_game_started = False
            elif event.type == KEYDOWN:
                if event.key == K_ESCAPE:
                    is_game_active = False

                elif event.key == K_RIGHT:
                    dk.move('right')
                elif event.key == K_LEFT:
                    dk.move('left')
                elif event.key == K_UP:
                    dk.move('up')
                elif event.key == K_DOWN:
                    dk.move('down')

        # Displays DK at the new coordinates
        gameWindow.blit(background, (0, 0))
        level.display(gameWindow)
        gameWindow.blit(dk.direction, (dk.x, dk.y))
        pygame.display.flip()

        if level.structure[dk.square_y][dk.square_x] == 'e':
            is_game_over = True


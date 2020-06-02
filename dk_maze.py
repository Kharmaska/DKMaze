"""
This Python Project is a training project for my OpenClassRooms degree in Python development
"""
# Libraries imports
import pygame

pygame.init()

# Creation of the Pygame window
maze = pygame.display.set_mode((640, 480))

# Loads the background image and
# Adds the background texture to our game window
background = pygame.image.load('background.jpg').convert()
maze.blit(background, (0, 0))

mushroom = pygame.image.load('shroom.png').convert()
maze.blit(mushroom, (200, 300))

# Updates the display of the game
pygame.display.flip()


# infinite loop for now
is_game_over = False
while not is_game_over:
    pass

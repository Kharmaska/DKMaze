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

mushroom = pygame.image.load('shroom.png').convert_alpha()
mushroom_x = 0
mushroom_y = 0
maze.blit(mushroom, (mushroom_x, mushroom_y))

# Updates the display of the game
pygame.display.flip()

# Main Game loop
is_game_over = False
pygame.key.set_repeat(400, 30)
while not is_game_over:
    # Awaiting events
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            is_game_over = True
        if event.type == pygame.MOUSEMOTION:
            mushroom_x = event.pos[0]
            mushroom_y = event.pos[1]
        if event.type == pygame.MOUSEBUTTONDOWN and event.button == 3 and event.pos[1] < 100:
            print("Zone dangereuse")

    maze.blit(background, (0, 0))
    maze.blit(mushroom, (mushroom_x, mushroom_y))
    pygame.display.flip()

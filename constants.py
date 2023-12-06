import pygame
# Screen dimensions
SCREEN_WIDTH = 400
SCREEN_HEIGHT = 600

# Bird dimensions
BIRD_WIDTH = 55
BIRD_HEIGHT = 40

# Pipe dimensions
PIPE_WIDTH = 60
PIPE_HEIGHT = 400
PIPE_GAP = 200

# Physics
GRAVITY = 0.25
JUMP_HEIGHT = -8

# User events
BIRD_FLAP = pygame.USEREVENT + 1
PIPE_SPAWN = pygame.USEREVENT

# Game speed
GAME_SPEED = 5
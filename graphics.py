import pygame
from constants import SCREEN_WIDTH, SCREEN_HEIGHT, BLOCK_SIZE, GRAY, DARK_GRAY, YELLOW, BLUE

def draw_grid(screen):
    for x in range(0, SCREEN_WIDTH, BLOCK_SIZE):
        pygame.draw.line(screen, GRAY, (x, 0), (x, SCREEN_HEIGHT))
    for y in range(0, SCREEN_HEIGHT, BLOCK_SIZE):
        pygame.draw.line(screen, GRAY, (0, y), (SCREEN_WIDTH, y))

def draw_block(screen, x, y, color):
    pygame.draw.rect(screen, color, (x * BLOCK_SIZE, y * BLOCK_SIZE, BLOCK_SIZE, BLOCK_SIZE))

def update_display():
    pygame.display.flip()

import pygame
from constants import *
from game import rotate_piece, check_collision, add_piece_to_board, clear_lines, TETRIS_SHAPES
from graphics import draw_grid, draw_block, update_display

import random

def main():
    pygame.init()
    screen = pygame.display.set_mode((SCREEN_WIDTH, SCREEN_HEIGHT))
    pygame.display.set_caption("Tetris")
    clock = pygame.time.Clock()

    board = [[0] * COLS for _ in range(ROWS)]
    piece = random.choice(TETRIS_SHAPES)
    x, y = COLS // 2 - len(piece[0]) // 2, 0
    game_over = False
    score = 0

    while not game_over:
        screen.fill(DARK_GRAY)
        draw_grid(screen)

        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                game_over = True
            if event.type == pygame.KEYDOWN:
                if event.key == pygame.K_LEFT and not check_collision(board, piece, x - 1, y):
                    x -= 1
                if event.key == pygame.K_RIGHT and not check_collision(board, piece, x + 1, y):
                    x += 1
                if event.key == pygame.K_DOWN and not check_collision(board, piece, x, y + 1):
                    y += 1
                if event.key == pygame.K_SPACE:  # Rotaciona a peça ao apertar espaço
                    new_piece = rotate_piece(piece)
                    if not check_collision(board, new_piece, x, y):
                        piece = new_piece

        if not check_collision(board, piece, x, y + 1):
            y += 1
        else:
            add_piece_to_board(board, piece, x, y)
            score += clear_lines(board)
            piece = random.choice(TETRIS_SHAPES)
            x, y = COLS // 2 - len(piece[0]) // 2, 0
            if check_collision(board, piece, x, y):
                game_over = True

        for i, row in enumerate(piece):
            for j, val in enumerate(row):
                if val:
                    draw_block(screen, x + j, y + i, YELLOW)

        for i, row in enumerate(board):
            for j, val in enumerate(row):
                if val:
                    draw_block(screen, j, i, BLUE)

        update_display()
        clock.tick(10)

    pygame.quit()

if __name__ == "__main__":
    main()
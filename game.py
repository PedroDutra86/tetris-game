import random
from constants import TETRIS_SHAPES, COLS, ROWS

def rotate_piece(piece):
    return [[piece[y][x] for y in range(len(piece))] for x in range(len(piece[0]) - 1, -1, -1)]

def check_collision(board, piece, x, y):
    for py, row in enumerate(piece):
        for px, cell in enumerate(row):
            if cell:
                if x + px < 0 or x + px >= COLS or y + py >= ROWS or board[y + py][x + px]:
                    return True
    return False

def add_piece_to_board(board, piece, x, y):
    for py, row in enumerate(piece):
        for px, cell in enumerate(row):
            if cell:
                board[y + py][x + px] = 1

def clear_lines(board):
    lines_to_clear = []
    for y, row in enumerate(board):
        if all(row):
            lines_to_clear.append(y)
    for y in lines_to_clear:
        del board[y]
        board.insert(0, [0] * COLS)
    return len(lines_to_clear)

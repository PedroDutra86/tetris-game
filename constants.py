SCREEN_WIDTH = 300
SCREEN_HEIGHT = 600
BLOCK_SIZE = 30
ROWS = SCREEN_HEIGHT // BLOCK_SIZE
COLS = SCREEN_WIDTH // BLOCK_SIZE

WHITE = (255, 255, 255)
GRAY = (169, 169, 169)
BLUE = (0, 0, 255)
GREEN = (0, 255, 0)
RED = (255, 0, 0)
YELLOW = (255, 255, 0)
DARK_GRAY = (40, 40, 40)

TETRIS_SHAPES = [
    [[1, 1, 1, 1]],  # I shape
    [[1, 1], [1, 1]],  # O shape
    [[0, 1, 0], [1, 1, 1]],  # T shape
    [[0, 1, 1], [1, 1, 0]],  # S shape
    [[1, 1, 0], [0, 1, 1]],  # Z shape
    [[1, 0, 0], [1, 1, 1]],  # J shape
    [[0, 0, 1], [1, 1, 1]],  # L shape
]

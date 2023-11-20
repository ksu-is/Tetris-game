import pygame 
import random 

# Initialize Pygame
pygame.init()

# Constants
WIDTH, HEIGHT = 300, 600
GRID_SIZE = 30
FPS = 10

# Colors
WHITE = (255, 255, 255)
BLACK = (0, 0, 0)
RED = (255, 0, 0)
CYAN = (0, 255, 255)
MAGENTA = (255, 0, 255)
YELLOW = (255, 255, 0)
GREEN = (0, 255, 0)
BLUE = (0, 0, 255)
ORANGE = (255, 165, 0)

# Shapes and their colors
SHAPES = [
    [[1, 1, 1, 1]],  # I
    [[1, 1, 1], [1]],  # L
    [[1, 1, 1], [0, 0, 1]],  # J
    [[1, 1], [1, 1]],  # O
    [[1, 1, 1], [0, 1]],  # S
    [[1, 1, 1], [1, 0]],  # T
    [[1, 1], [0, 1, 1]],  # Z
]

SHAPES_COLORS = [CYAN, ORANGE, BLUE, YELLOW, GREEN, MAGENTA, RED]

# Initialize game window
screen = pygame.display.set_mode((WIDTH, HEIGHT))
pygame.display.set_caption("Tetris")
clock = pygame.time.Clock()

# Function to draw the grid
def draw_grid():
    for x in range(0, WIDTH, GRID_SIZE):
        pygame.draw.line(screen, WHITE, (x, 0), (x, HEIGHT))
    for y in range(0, HEIGHT, GRID_SIZE):
        pygame.draw.line(screen, WHITE, (0, y), (WIDTH, y))

# Function to draw a shape on the grid
def draw_shape(shape, pos, color):
    for y, row in enumerate(shape):
        for x, value in enumerate(row):
            if value:
                pygame.draw.rect(screen, color, (pos[0] + x * GRID_SIZE, pos[1] + y * GRID_SIZE, GRID_SIZE, GRID_SIZE))
                pygame.draw.rect(screen, WHITE, (pos[0] + x * GRID_SIZE, pos[1] + y * GRID_SIZE, GRID_SIZE, GRID_SIZE), 1)

                def is_valid_position(shape, pos, grid):
    for y, row in enumerate(shape):
        for x, value in enumerate(row):
            if value:
                if (
                    pos[0] + x < 0
                    or pos[0] + x >= WIDTH / GRID_SIZE
                    or pos[1] + y >= HEIGHT / GRID_SIZE
                    or grid[pos[1] // GRID_SIZE + y][pos[0] // GRID_SIZE + x] is not None
                ):
                    return False
    return True

# Function to remove completed lines
def remove_line(grid, line):
    del grid[line]
    return [[None] * (WIDTH // GRID_SIZE)] + grid

    
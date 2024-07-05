import pygame as pg 
import sys, math, array, random, copy
from enum import Enum
from dataclasses import dataclass

vec2 = pg.math.Vector2
vec3 = pg.math.Vector3

false = False
true = True
inf = float('inf')
n_inf = float('-inf')
GRAVITY = 1

WIDTH = 600
HEIGHT = 600
HALF_WIDTH = WIDTH // 2 
HALF_HEIGHT = HEIGHT // 2
CENTER = vec2(WIDTH // 2, HEIGHT // 2)

CELL_SIZE = 32
ENTITY_SIZE = [CELL_SIZE, CELL_SIZE]
TILE_DIM = [CELL_SIZE, CELL_SIZE]
HALF_CELL_SIZE = CELL_SIZE // 2
ROWS = HEIGHT // CELL_SIZE
COLS = WIDTH // CELL_SIZE

# COLORS
BLACK = (0, 0, 0)
WHITE = (255, 255, 255)
LIGHT_GRAY = (160, 160, 160)
GRAY = (80, 80, 80)
RED = (255, 0, 0)
PINK = (250, 0, 250)
SKY_BLUE = (120, 170, 250)
MID_GRAY = (70, 70, 70)
DARK_GRAY = (30, 30, 30)
BROWN = (100, 50, 0)
GREEN = (40, 200, 0)
BLUE = (50, 100, 250)
ORANGE = (250, 40, 0)

FPS = 60

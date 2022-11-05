import pygame
import sys
import random
import math
import time
from pygame.locals import *
pygame.init()

SCREEN = pygame.display.set_mode((1280, 720), pygame.RESIZABLE)
FPS = 30
CLOCK = pygame.time.Clock()
pygame.display.set_caption("Agar.io")

cell_count = 2000
bot_count = 20
map_size = 2000
spawn_size = 25
bots_mins_size = 25
bots_max_size = 250
respawn_cells = True
respawn_bots = False
player_color = (255,0,0)
background_color = (0,0,0)
text_color = (255,255,255)

FONT = pygame.font.SysFont("comicsans", 32)
BIGFONT = pygame.font.SysFont("comicsans", 72)
WIDTH = 1280
HEIGHT = 720
cells = []
bots = []
game_over = False

counter = 0
frame_rate = 30
start_time = 0
frame_rate_delay = 0.5

class Cell():
    def __init__(self, x, y, color, radius, name):
        self.name = name
        self.radius = radius
        self.color = color
        self.status = random.randint(1,8)
        self.x_pos = x
        self.y_pos = y
        
    def wander(self):
        pass

    def collide_check(self, player):
        pass

    def draw(self, surface, x, y):
        pygame.draw.circle(surface, self.color, (x, y), int(self.radius))
        if self.name == "Bot" or self.name == "Player":
            text = FONT.render(str(round(self.radius)), False, text_color)

for i in range(cell_count):
    new_cell = Cell(random.randint(-map_size, map_size), random.randing(-map_size, map_size), (random.randint(0,255), random.randint(0,255), random.randint(0,255)), 5, "Cell")
    cells.append(new_cell)

player_cell = Cell(0,0,player_color, spawn_size, "Player")


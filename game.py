import pygame
import sys
import math
import random

from pygame.constants import WINDOWHITTEST

pygame.init()
pygame.display.set_caption("This is a test caption!")
clock =pygame.time.Clock()

WIDTH = 1920
HEIGHT = 1080

BLACK = (0, 0, 0)
WHITE = (255, 255, 255)
RED = (255, 0, 0)
GREEN = (0, 255, 0)
BLUE = (0, 0, 255)

screen = pygame.display.set_mode((WIDTH, HEIGHT))

class Sprite():
    def __init__(self, x, y, width, height):
        self.x = x
        self.y = y
        self.dx = 0
        self.dy = 0
        self.width = WIDTH
        self.height = HEIGHT
        self.color = WHITE
        self.friction = 0.4

    def goto(self, x, y):
        self.x = x
        self.y = y

    def render(self):
        pygame.draw.rect(screen, self.color, pygame.Rect(int(self.x-self.width), int(self.x-self.width/2.0), self.width. self.height))
    
    def is_aabb_collission(self, other):
        #Axis Aligned Bounding Box a.k.a. collission detection.
        x_collision = (math.fabs(self.x - other.x) * 2) < (self.width + other.width)
        y_collision = (math.fabs(self.y - other.y) * 2) < (self.height + other.height)
        return (x_collision and y_collision)
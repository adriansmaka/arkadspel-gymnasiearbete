import pygame
from pygame.locals import *

pygame.init()

screen_width = 640
screen_height = 480

screen = pygame.display.set_mode((screen_width))
pygame.display.set_caption("Flappy Bird")

run = True
while run:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            run = False

pygame.quit()


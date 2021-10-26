from typing import KeysView
import pygame
import os

pygame.init()
#width, height = 1280, 960
width, height = 1100, 740
window = pygame.display.set_mode((width, height))
fps = 60
char_velocity = 10
nme_v = 10
white = (255, 255, 255)
black = (0, 0, 0)
red = (255, 0, 0)
green = (0, 255, 0)
blue = (0, 0, 255)
nme_n = 1

char_border_h = int(height * 0.4)
# x-kord, y-kord, width, height
wall = pygame.Rect(0, char_border_h, width, height)

char_w, char_h = 64, 64
char_x, char_y = 0, 0
char_img = pygame.image.load(os.path.join('img', 'ship.png'))
char = pygame.transform.scale(char_img, (char_w, char_h))

nme_x, nme_y = 0, 0
nme_w, nme_h = 70, 30
nme_img = pygame.image.load(os.path.join('img', 'nme_rect.png'))
nme = pygame.transform.scale(nme_img, (nme_w, nme_h))
nme_border_h = char_border_h - nme_h - 30

def wall_create():
    numwall = int(height / nme_h)
    for x in range(numwall):
        wall = pygame.Rect(0, 0, width, nme_h)
    return wall

wall2 = pygame.Rect(0, 0, width, nme_h)
wall3 = pygame.Rect(0, 0, width, nme_h * 2)
wall4 = pygame.Rect(0, 0, width, nme_h * 3)
wall5 = pygame.Rect(0, 0, width, nme_h * 4)
wall6 = pygame.Rect(0, 0, width, nme_h * 5)
wall7 = pygame.Rect(0, 0, width, nme_h * 6)
wall8 = pygame.Rect(0, 0, width, nme_h * 7)
wall9 = pygame.Rect(0, 0, width, nme_h * 8)
wall10 = pygame.Rect(0, 0, width, nme_h * 9)
wall11 = pygame.Rect(0, 0, width, nme_h * 10)
wall12 = pygame.Rect(0, 0, width, nme_h * 11)

def display_window(char_game, nme_game):
    window.fill(white)
    pygame.draw.rect(window, red, wall12)
    pygame.draw.rect(window, green, wall11)
    pygame.draw.rect(window, blue, wall10)
    pygame.draw.rect(window, red, wall9)
    pygame.draw.rect(window, green, wall8)
    pygame.draw.rect(window, blue, wall7)
    pygame.draw.rect(window, red, wall6)
    pygame.draw.rect(window, green, wall5)
    pygame.draw.rect(window, blue, wall4)
    pygame.draw.rect(window, red, wall3)
    pygame.draw.rect(window, green, wall2)
    pygame.draw.rect(window, blue, wall)
    window.blit(char, (char_game.x, char_game.y))
    window.blit(nme, (nme_game.x, nme_game.y))
    pygame.display.update()

def char_movement(keys_pressed, char_game):
    #char movement
        if keys_pressed[pygame.K_a]:
            char_game.x -= char_velocity
        if keys_pressed[pygame.K_d]:
            char_game.x += char_velocity
        if keys_pressed[pygame.K_s]:
            char_game.y += char_velocity 
        if keys_pressed[pygame.K_w]:
            char_game.y -= char_velocity
    #char border
        if char_game.x < 0:
            char_game.x = 0
        if char_game.x > width-char_w:
            char_game.x = width-char_w
        if char_game.y > height-char_h:
            char_game.y = height-char_h
        if char_game.y < char_border_h:
            char_game.y = char_border_h



def nme_movement(nme_game):
    if nme_game.y < nme_border_h:
        clears = 0
        while clears < 6:
            n = 0
            clears = n

#----------- Height update -----------

            while n < 6:
                n = nme_game.y / nme_h
                print("n is", n)
                break

#----------- X axis movement -----------

            if nme_game.x >= 0 and nme_game.x <= width - nme_w and n % 2 <= 0:
                nme_game.x += nme_v

            elif nme_game.x >= 0 and nme_game.x <= width - nme_w and n % 2 == 1:
                nme_game.x -= nme_v

#----------- Y axis movement -----------

            if nme_game.x == width - nme_w and nme_game.y >= nme_h * n and nme_game.y <= nme_h * n + nme_h:
                nme_game.y += nme_v

            elif nme_game.x == 0 and nme_game.y >= nme_h * n and nme_game.y <= nme_h * n + nme_h:
                nme_game.y += nme_v

            break



def main():
    #starting position, (x, y), (w, h)
    char_game = pygame.Rect((char_x, char_y), (char_w, char_h))
    nme_game = pygame.Rect((nme_x, nme_y), (nme_w, nme_h))

#----------- Game run -----------
    clock = pygame.time.Clock()
    run = True
    while run:
        clock.tick(fps)
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                run = False
            

        keys_pressed = pygame.key.get_pressed()
        char_movement(keys_pressed, char_game)
        nme_movement(nme_game)

        display_window(char_game, nme_game)

pygame.QUIT

main()
from typing import KeysView
import pygame
import os

pygame.init()
#width, height = 1280, 960
width, height = 1100, 748
heightdiv = height / 2
border_y = height * 0.4
window = pygame.display.set_mode((width, height))
fps = 60
velocity = 10
white = (255, 255, 255)
black = (0, 0, 0)
green = (0, 255, 0)

# x-kord, Y-kord, tjocklek, höjd
wall = pygame.Rect(0, border_y, width, height)

char_img = pygame.image.load(os.path.join('img', 'ship.png'))
char_w, char_h = 50, 50

char = pygame.transform.scale(char_img, (char_w, char_h))
char_x, char_y = 0, 0

nme_img = pygame.image.load(os.path.join('img', 'enemy_1.png'))
nme_w = 87
nme_h = 50
nme = pygame.transform.scale(nme_img, (nme_w, nme_h))
nme_x, nme_y = 0, 10

def display_triangle():
    pygame.draw.polygon((window), (255, 255, 0), [(char_x, char_y+50), (char_x+25, char_y), (char_x+50, char_y+50)])

def display_window(char_game, nme_game):
    window.fill(white)
    pygame.draw.rect(window, green, wall)
    window.blit(char, (char_game.x, char_game.y))
    window.blit(nme, (nme_game.x, nme_game.y))
    display_triangle()
    pygame.display.update()

def char_movement(keys_pressed, char_game):
    #char movement
        if keys_pressed[pygame.K_a]:
            char_game.x -= velocity
        if keys_pressed[pygame.K_d]:
            char_game.x += velocity
        if keys_pressed[pygame.K_s]:
            char_game.y += velocity 
        if keys_pressed[pygame.K_w]:
            char_game.y -= velocity
    #char border
        if char_game.x < 0:
            char_game.x = 0
        if char_game.x > width-char_w:
            char_game.x = width-char_w
        if char_game.y > height-char_h:
            char_game.y = height-char_h
        if char_game.y < border_y:
            char_game.y = border_y


            #do not delete
            #-------------
            #if pygame.Rect.colliderect(char_game, wall):
                #print("Crash!")


def main():
    #starting position, (x, y), (w, h)
    char_game = pygame.Rect((char_x, char_y), (char_w, char_h))
    nme_game = pygame.Rect((nme_x, nme_y), (nme_w, nme_h))

    #game run
    clock = pygame.time.Clock()
    run = True
    while run:
        clock.tick(fps)
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                run = False
            
        

        #char movement
        keys_pressed = pygame.key.get_pressed()
        char_movement(keys_pressed, char_game)
        

        #nme movement
        nme_game.x += 1

        if char_game.x >= 0:
            char_game.x ==  0
        if char_game.x <= 1100:
            char_game.x ==  1100
        if char_game.y >= 0:
            char_game.y ==  0
        if char_game.y <= 748:
            char_game.y ==  748

        display_window(char_game, nme_game)

pygame.QUIT

#if __name__ == "__main__":

main()

""" https://www.pygame.org/docs/ref/rect.html """
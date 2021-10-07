from typing import KeysView
import pygame
import os

pygame.init()
#width, height = 1280, 960
width, height = 1100, 748
char_border_h = int(height * 0.4)
window = pygame.display.set_mode((width, height))
fps = 60
char_velocity = 10
nme_velocity = 10
white = (255, 255, 255)
black = (0, 0, 0)
red = (255, 0, 0)
green = (0, 255, 0)
blue = (0, 0, 255)

# x-kord, Y-kord, width, height
wall = pygame.Rect(0, char_border_h, width, height)


char_w, char_h = 64, 64
char_x, char_y = 0, 0
char_img = pygame.image.load(os.path.join('img', 'ship.png'))
char = pygame.transform.scale(char_img, (char_w, char_h))

nme_x, nme_y = 250, 0
nme_w, nme_h = 70, 30
nme_img = pygame.image.load(os.path.join('img', 'enemy_1.png'))
nme = pygame.transform.scale(nme_img, (nme_w, nme_h))
nme_border_h = char_border_h - nme_h - 10

wall2 = pygame.Rect(0, nme_border_h, width, height)


#def display_triangle():
#    pygame.draw.polygon((window), (255, 255, 0), [(char_x, char_y+50), (char_x+25, char_y), (char_x+50, char_y+50)])

def display_window(char_game, nme_game):
    window.fill(white)
    pygame.draw.rect(window, blue, wall2)
    pygame.draw.rect(window, green, wall)
    window.blit(char, (char_game.x, char_game.y))
    window.blit(nme, (nme_game.x, nme_game.y))
    #display_triangle()
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
        #nme movement
        if nme_game.y < nme_border_h:
            nme_game.x += nme_velocity
            if nme_game.x > width-nme_w:
                nme_game.x = width-nme_w
                nme_game.y += nme_velocity
            if nme_game.y == 0+nme_h:
                nme_game.x -= nme_velocity
                nme_game.x -= nme_velocity
            if nme_game.x == 0:
                nme_game.y += nme_velocity
                nme_game.x += nme_velocity
        else:
            
            """             nme_game.x, nme_game.y == nme_velocity
            if nme_game.x == 0:
                nme_game.x += nme_velocity
            if nme_game.x == width:
                nme_game.x -= nme_velocity """




            #do not delete
            #-------------
            #if pygame.Rect.colliderect(char_game, char_border_h):
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
        nme_movement(nme_game)
        #if nme_game.y < nme_border_h:
        #    nme_movement(nme_game)
        #else:
        #    print("Stop!")

        #nme_run = 0
        #while nme_run < :
        #    nme_movement(nme_game)
        #    nme_run = nme_run + 1

            #Dont delete, nme spawn?
            #if nme_game.x > width-char_w:
                #nme_game.x == width-char_w
                #nme_game.y += char_velocity
                #nme_game.x =- char_velocity

        display_window(char_game, nme_game)

pygame.QUIT

#if __name__ == "__main__":

main()

""" https://www.pygame.org/docs/ref/rect.html """
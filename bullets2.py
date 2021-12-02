from typing import KeysView
import pygame
import os
from pygame import font
import random
from pygame.constants import K_ESCAPE, KEYDOWN, USEREVENT, K_e

pygame.init()
#width, height = 1280, 960
width, height = 1100, 740
window = pygame.display.set_mode((width, height))
#useful assets
fps = 60
char_velocity = 10
bullet_velocity = 10
white = (255, 255, 255)
black = (0, 0, 0)
red = (255, 0, 0)
green = (0, 255, 0)
blue = (0, 0, 255)
nme_n = 1
lives = 3
bullet_delay = random.randrange(600, 2000)
nme_game_bullet = USEREVENT + 1
nme_amount = 20
nme_list = []

#score display
score = 0
font = pygame.font.Font('freesansbold.ttf', 32)

def score_display():
    score_game = font.render("Score: " + str(score), True, (255, 255, 255))
    window.blit(score_game, (950, 700))



def lives_display():
    lives_game = font.render("Lives: " + str(lives), True, (255,255,255))
    window.blit(lives_game, (20, 700))
    pygame.display.update()

char_border = int(height * 0.4)
# x-kord, y-kord, width, height
wall = pygame.Rect(0, char_border, width, height)

#char_lives = 3
#Char.w, Char.h = 64, 64
#char.x, char.y = width/2 - Char.w, 500
#char_img = pygame.image.load(os.path.join('img', 'ship.png'))
#char = pygame.transform.scale(char_img, (Char.w, Char.h))

#nme_x, nme_y = 0, 0
#nme_w, nme_h = 70, 30
#nme_img = pygame.image.load(os.path.join('img', 'nme_1.png'))
#nme = pygame.transform.scale(nme_img, (nme_w, nme_h))
#border = char_border - nme_h - 30

class Char:
    w, h = 64, 64
    x, y = width/2 - w, 500
    char_img = pygame.image.load(os.path.join('img', 'ship.png'))
    char = pygame.transform.scale(char_img, (w, h))

class Nme:
    x, y = 0, 0
    w, h = 70, 30
    img = pygame.image.load(os.path.join('img', 'enemy_1.png'))
    nme = pygame.transform.scale(img, (w, h))



nme_border = char_border - Char.h - 30

bullet_w, bullet_h = 10, 25
char_bullet_img = pygame.image.load(os.path.join('img', 'stor_bullet.png'))
char_bullet = pygame.transform.scale(char_bullet_img, (bullet_w, bullet_h))
nme_bullet_img = pygame.image.load(os.path.join('img', 'nmebullet.png'))
nme_bullet = pygame.transform.scale(nme_bullet_img, (bullet_w, bullet_h))



wall2 = pygame.Rect(0, 0, width, Nme.h)
wall3 = pygame.Rect(0, 0, width, Nme.h * 2)
wall4 = pygame.Rect(0, 0, width, Nme.h * 3)
wall5 = pygame.Rect(0, 0, width, Nme.h * 4)
wall6 = pygame.Rect(0, 0, width, Nme.h * 5)
wall7 = pygame.Rect(0, 0, width, Nme.h * 6)
wall8 = pygame.Rect(0, 0, width, Nme.h * 7)
wall9 = pygame.Rect(0, 0, width, Nme.h * 8)
wall10 = pygame.Rect(0, 0, width, Nme.h * 9)
wall11 = pygame.Rect(0, 0, width, Nme.h * 10)
wall12 = pygame.Rect(0, 0, width, Nme.h * 11)

def display_window(char_game, nme_game, char_game_bullet, nme_game_bullet):
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

    window.blit(Char.char, (char_game.x, char_game.y))
    window.blit(Nme.nme, (nme_game.x, nme_game.y))
    window.blit(Nme.nme, (nme_game.x, nme_game.y))
    
    #spawn = window.blit(nme, (nme_game.x, nme_game.y))
    #spawn = window.blit(nme, (nme_game.x, nme_game.y))
    #spawn_event = USEREVENT + 3
    #pygame.time.set_timer(spawn_event, 2000)
    #for i in range(nme_amount):
    #   if event.type == spawn_event:
        
    
        
    #display_triangle()

    for bullets in char_game_bullet:
        pygame.draw.rect(window, black, bullets)

    for bullets in nme_game_bullet:
        pygame.draw.rect(window, black, bullets)


def char_movement(keys_pressed, char_game, nme_game_bullet, nme_game):
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
        if char_game.x > width-Char.w:
            char_game.x = width-Char.w
        if char_game.y > height-Char.h:
            char_game.y = height-Char.h
        if char_game.y < char_border:
            char_game.y = char_border
        
def powerup(keys_pressed, char_game, char_game_bullet):     
    if keys_pressed[pygame.K_p]:
        bullet = pygame.Rect(char_game.x + char_game.width / 2.2 + 1, char_game.y, 5, 25)
        char_game_bullet.append(bullet)

nme_game_bullet_event = USEREVENT + 1
pygame.time.set_timer(nme_game_bullet_event, bullet_delay)


def nme_movement(nmes):
    nme_v = 10
    if nmes.y < nme_border:
        clears = 0
        while clears == 0:
            n = 0

#----------- Height update -----------

            while n < 6:
                n = nmes.y / Nme.h
                break

#----------- X axis movement -----------

            if nmes.x >= 0 and nmes.x <= width - Nme.w and n % 2 <= 0:
                nmes.x += nme_v

            elif nmes.x >= 0 and nmes.x <= width - Nme.w and n % 2 == 1:
                nmes.x -= nme_v

#----------- Y axis movement -----------

            if nmes.x == width - Nme.w and nmes.y >= Nme.h * n and nmes.y <= Nme.h * n + Nme.h:
                nmes.y += nme_v

            elif nmes.x == 0 and nmes.y >= Nme.h * n and nmes.y <= Nme.h * n + Nme.h:
                nmes.y += nme_v

            break

#    else:
#        if nme_game.x >= 0 and nme_game.x <= width - nme.w:
#            nme_game.x += nme_v
#        else:
#            nme_v = nme_v * -1


def bullet_physics(char_game_bullet, char_game, nme_game, nme_game_bullet):
    for bullet in char_game_bullet:
        bullet.y -= bullet_velocity
        if nme_game.colliderect(bullet):
            char_game_bullet.remove(bullet)
            nme_game.x = random.randrange(-1000, -100)
            nme_game.y = random.randrange(-1000, -100)
            global score
            score += 1
            print(score)
        elif bullet.y > height:
            char_game_bullet.remove(bullet)
    for bullet in nme_game_bullet:
        bullet.y += bullet_velocity
        if char_game.colliderect(bullet):
            nme_game_bullet.remove(bullet)
            global lives
            lives -= 1

def nme_spawner():
    nme_game = pygame.Rect((Nme.x, Nme.y), (Nme.w, Nme.h))
    return nme_game

def main():
    

    char_game = pygame.Rect((Char.x, Char.y), (Char.w, Char.h))
    nme_game = pygame.Rect((Nme.x, Nme.y), (Nme.w, Nme.h))
    if nme_game.x == 0:
        nme_list = []
        for i in range(10):
            nme_list.append(nme_game)
            #print(nme_list)

    char_game_bullet = []
    nme_game_bullet = []
    #game run
    clock = pygame.time.Clock()
    run = True
    while run:
        clock.tick(fps)
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                run = False
            
            if event.type == pygame.KEYDOWN:
                if event.key == pygame.K_SPACE:
                    bullet = pygame.Rect(char_game.x + char_game.width / 2.2 + 1, char_game.y, 5, 25)
                    char_game_bullet.append(bullet)
            
            if event.type == nme_game_bullet_event:
                bullet = pygame.Rect(nme_game.x + nme_game.width / 2.2 + 1, nme_game.y, 5, 25)
                nme_game_bullet.append(bullet)

                
                
            #WORK IN PROGRESS. NOT DONE, MAINMENU / SCORESCREEN!!!
            if lives < 0:
                run = False

        #char movement
        keys_pressed = pygame.key.get_pressed()
        nme_spawner()
        char_movement(keys_pressed, char_game, nme_game_bullet, nme_game)
        bullet_physics(char_game_bullet, char_game, nme_game, nme_game_bullet)
        score_display()
        lives_display()
        display_window(char_game, nme_game, char_game_bullet, nme_game_bullet)
        nme_movement(nme_game)
        #nme_spawn()
        #nme_shooting(nme_game, event)
        # #quit_game()

pygame.QUIT

#if __name__ == "__main__":

main()
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
nme_velocity = 10
bullet_velocity = 10
white = (255, 255, 255)
black = (0, 0, 0)
red = (255, 0, 0)
green = (0, 255, 0)
blue = (0, 0, 255)
nme_n = 1
lives = 3

#score display
score = 0
font = pygame.font.Font('freesansbold.ttf', 32)

def score_display():
    score_game = font.render("Score: " + str(score), True, (255, 255, 255))
    window.blit(score_game, (950, 700))

char_border_h = int(height * 0.4)

def lives_display():
    lives_game = font.render("Lives: " + str(lives), True, (255,255,255))
    window.blit(lives_game, (20, 700))
    pygame.display.update()



# x-kord, y-kord, width, height
wall = pygame.Rect(0, char_border_h, width, height)

#char_lives = 3
char_w, char_h = 64, 64
char_x, char_y = 0, 0
char_img = pygame.image.load(os.path.join('img', 'ship.png'))
char = pygame.transform.scale(char_img, (char_w, char_h))

nme_x, nme_y = width/2, 0
nme_w, nme_h = 70, 30
nme_img = pygame.image.load(os.path.join('img', 'enemy_1.png'))
nme = pygame.transform.scale(nme_img, (nme_w, nme_h))
nme_border_h = char_border_h - nme_h - 30

bullet_w, bullet_h = 10, 25
char_bullet_img = pygame.image.load(os.path.join('img', 'stor_bullet.png'))
char_bullet = pygame.transform.scale(char_bullet_img, (bullet_w, bullet_h))
nme_bullet_img = pygame.image.load(os.path.join('img', 'nmebullet.png'))
nme_bullet = pygame.transform.scale(nme_bullet_img, (bullet_w, bullet_h))

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
    window.blit(char, (char_game.x, char_game.y))
    window.blit(nme, (nme_game.x, nme_game.y))
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
        if char_game.x > width-char_w:
            char_game.x = width-char_w
        if char_game.y > height-char_h:
            char_game.y = height-char_h
        if char_game.y < char_border_h:
            char_game.y = char_border_h
        
def powerup(keys_pressed, char_game, char_game_bullet):     
    if keys_pressed[pygame.K_p]:
        bullet = pygame.Rect(char_game.x + char_game.width / 2.2 + 1, char_game.y, 5, 25)
        char_game_bullet.append(bullet)

#def nme_shooting(keys_pressed, nme_game, nme_game_bullet):
  #  if keys_pressed[pygame.K_p] == False:
   #     bullet = pygame.Rect(nme_game.x + nme_game.width / 2.2 + 1, nme_game.y, 5, 25)
   #     nme_game_bullet.append(bullet)
    #    nme_game_bullet = USEREVENT +1
    #    pygame.time.set_timer(nme_game_bullet, 500)

#nme_game_bullet = USEREVENT +1
#pygame.time.set_timer(nme_game_bullet, 500)

def bullet_physics(char_game_bullet, char_game, nme_game, nme_game_bullet):
    for bullet in char_game_bullet:
        bullet.y -= bullet_velocity
        if nme_game.colliderect(bullet):
            #pygame.event.post(pygame.event.Event(nme_hit))
            char_game_bullet.remove(bullet)
            nme_game.x = random.randrange(-1000, -100)
            nme_game.y = random.randrange(-1000, -100)
            global score
            score += 1
            #print(score)
        elif bullet.y > height:
            char_game_bullet.remove(bullet)
    for bullet in nme_game_bullet:
        bullet.y += bullet_velocity
        if char_game.colliderect(bullet):
            nme_game_bullet.remove(bullet)
            global lives
            lives -= 1

def nme_shooting(nme_game, nme_game_bullet, event_list):
    for event in event_list:
        if event.type == nme_game_bullet_event:
            bullet = pygame.Rect(nme_game.x + nme_game.width / 2.2 + 1, nme_game.y, 5, 25)
            nme_game_bullet.append(bullet)

nme_game_bullet_event = USEREVENT + 1
pygame.time.set_timer(nme_game_bullet_event, 500)

#def quit_game():
 #   if pygame.KEYDOWN == K_e:
  #      return pygame.QUIT

def main():
    #starting position, (x, y), (w, h)
    char_game = pygame.Rect((char_x, char_y), (char_w, char_h))
    nme_game = pygame.Rect((nme_x, nme_y), (nme_w, nme_h))

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
            
#----------- Char bullet -----------

        if event.type == pygame.KEYDOWN:
            if event.key == pygame.K_SPACE:
                bullet = pygame.Rect(char_game.x + char_game.width / 2.2 + 1, char_game.y, 5, 25)
                char_game_bullet.append(bullet)


                
            #WORK IN PROGRESS. NOT DONE!!!
            if lives < 0:
                run = False

            #nme shoot
            #nme_game_bullet = USEREVENT + 1
            #pygame.time.set_timer(nme_game_bullet, 450)
        
        #char movement
        keys_pressed = pygame.key.get_pressed()
        char_movement(keys_pressed, char_game, nme_game_bullet, nme_game)
        

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
            
        powerup(keys_pressed, char_game, char_game_bullet)
        bullet_physics(char_game_bullet, char_game, nme_game, nme_game_bullet)
        score_display()
        lives_display()
        display_window(char_game, nme_game, char_game_bullet, nme_game_bullet)
        nme_shooting(keys_pressed, nme_game, nme_game_bullet)
        nme_shooting(nme_game, nme_game_bullet, event_list)

        #quit_game()

pygame.QUIT

#if __name__ == "__main__":

main()

""" https://www.pygame.org/docs/ref/rect.html """
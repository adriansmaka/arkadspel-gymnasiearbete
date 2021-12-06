from typing import KeysView
import pygame
import os
from pygame import font
import random
from pygame import draw
from pygame import sprite
from pygame.constants import K_ESCAPE, KEYDOWN, USEREVENT, K_e
from pygame.sprite import Sprite, collide_mask

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
nme_spawner = USEREVENT + 0
nme_spawn_list = [5]
nme_amount = 20

nme_movement_ph = random.randint(1, 2)
#print(nme_movement_ph)


nme_movement_event = USEREVENT + 3
test = pygame.time.set_timer(nme_movement_event, 1)
#print(nme_movement_ph)


#def nmes_spawn(nme_game):
 #   nme_spawn_list.append(nme_game)

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

#movement switchers
#movement_switch1 = pygame.Rect(192, char_border_h, width, height)!!!!!!!!

#char_lives = 3
char_w, char_h = 64, 64
char_x, char_y = width/2 - char_w, 500
char_img = pygame.image.load(os.path.join('img', 'ship.png'))
char = pygame.transform.scale(char_img, (char_w, char_h))


nme_x, nme_y = 100, 100
nme_w, nme_h = 70, 30
nme_img = pygame.image.load(os.path.join('img', 'enemy_1.png'))
nme = pygame.transform.scale(nme_img, (nme_w, nme_h))
nmes_sprite = pygame.transform.scale(nme_img, (nme_w, nme_h))
nme_border_h = char_border_h - nme_h - 30

bullet_w, bullet_h = 10, 25
char_bullet_img = pygame.image.load(os.path.join('img', 'stor_bullet.png'))
char_bullet = pygame.transform.scale(char_bullet_img, (bullet_w, bullet_h))
nme_bullet_img = pygame.image.load(os.path.join('img', 'nmebullet.png'))
nme_bullet = pygame.transform.scale(nme_bullet_img, (bullet_w, bullet_h))



class enemy(pygame.sprite.Sprite):
    def __init__(self):
        super().__init__()
        self.x = random.randint(0, 1)
        self.y = 0
        self.w = 70
        self.h = 30
        self.moveX = 5
        self.moveY = 30

    def move(self):

        #print("D:",d1)
        #print("X:",self.x)
        #print("Y:",self.y)

        if self.x <= width - self.w:
            self.x += self.moveX
        wdiv = int(width - self.w/ 5)
        val = self.x % wdiv
        if val == 0 :
            d1 = random.randrange(0,2)
            print(d1)
            
                
                #self.y += self.moveY

    def draw(self):
        window.blit(nme, (self.x, self.y))
        self.hitbox = (self.x, self.y, 70, 30)
        pygame.draw.rect(window, (255, 0, 0), self.hitbox, 2)

#class enemy(Sprite):
    
enemies = pygame.sprite.Group()

enemy_list = []


for i in range(1):
    new_enemy = enemy()
    enemy_list.append(new_enemy)
 
def enemy_spawn():
    enemy.x = 0
    enemy.y = 0
    enemy_list.append(new_enemy)

enemies.add(new_enemy)

enemy_spawn_event = USEREVENT + 5
pygame.time.set_timer(enemy_spawn_event, 1000)

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

def display_window(char_game, nme_game, char_game_bullet, nme_game_bullet, nme_spawner):
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
    #window.blit(nmes, (nmes.x, nmes.y))
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

    #for place_holder_nme in nme_spawner:
        #pygame.draw.rect(window, black, place_holder_nme)

#def spawn(nme_game):
    #spawn = window.blit(nme, (nme_game.x, nme_game.y))
    #return spawn


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
        
        if nme_game.x == 768:
            nme_movement_ph == 1
        if nme_game.x == 0:
            nme_movement_ph == 2


def powerup(keys_pressed, char_game, char_game_bullet):     
    if keys_pressed[pygame.K_p]:
        bullet = pygame.Rect(char_game.x + char_game.width / 2.2 + 1, char_game.y, 5, 25)
        char_game_bullet.append(bullet)

nme_game_bullet_event = USEREVENT + 1
pygame.time.set_timer(nme_game_bullet_event, bullet_delay)

nme_direction_event = USEREVENT + 4
pygame.time.set_timer(nme_direction_event, 1)

#spawn_event = USEREVENT + 0
#pygame.time.set_timer(spawn_event, 1000)

#def nme_movement(nme_game):
 #   nme_v = 10
  #  if nme_game.y < nme_border_h:
   #     clears = 0
    #    while clears == 0:
     #       n = 0

#----------- Height update -----------

      #      while n < 6:
       #         n = nme_game.y / nme_h
        #        break

#----------- X axis movement -----------

         #   if nme_game.x >= 0 and nme_game.x <= width - nme_w and n % 2 <= 0:
          #      nme_game.x += nme_v

           # elif nme_game.x >= 0 and nme_game.x <= width - nme_w and n % 2 == 1:
            #    nme_game.x -= nme_v

#----------- Y axis movement -----------

            #if nme_game.x == width - nme_w and nme_game.y >= nme_h * n and nme_game.y <= nme_h * n + nme_h:
             #   nme_game.y += nme_v

            #elif nme_game.x == 0 and nme_game.y >= nme_h * n and nme_game.y <= nme_h * n + nme_h:
             #   nme_game.y += nme_v

            #break

    #else:
     #   if nme_game.x >= 0 and nme_game.x <= width - nme_w:
      #      nme_game.x += nme_v
       # else:
#            nme_v = nme_v * -1

#def nme_spawn():
   # for i in range(nme_amount):
     #   nme_img.append(pygame.image.load('enemy_1.png'))


def bullet_physics(char_game_bullet, char_game, nme_game, nme_game_bullet, nme_spawner):
    for bullet in char_game_bullet:
        bullet.y -= bullet_velocity
        if nme_game.colliderect(bullet):
            char_game_bullet.remove(bullet)
            #nme_game.x = random.randrange(0, 1)
            #nme_game.y = random.randrange(0, 1)
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
    #for nmes in nme_spawner:
        #nmes.x += char_velocity
    
    #if nmes.colliderect(bullet):
     #   char_game_bullet.remove(bullet)
    
#def nmes_physics(nmes, char_game_bullet):
    

def main():
    char_game = pygame.Rect((char_x, char_y), (char_w, char_h))
    nme_game = pygame.Rect((nme_x, nme_y), (nme_w, nme_h))
   # nmes = pygame.Rect(0, 0, 60, 30)

    char_game_bullet = []
    nme_game_bullet = []
    nme_spawner = []
    enemies.update()
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
                   
            #if event.type == enemy_spawn_event:
                #enemy_spawn()  #???????
                
           # if event.type == spawn_event:            
             #   nme_spawner.append(nmes)
         
            #if event.type == nme_direction_event:
             #   if nme_game.x == 0:
              #      nme_movement_ph = 2
               # elif nme_game.x == 769:
                #    nme_movement_ph = 1
                    
            if event.type == nme_movement_event:
                if nme_movement_ph == 1:
                    nme_game.x -= 1
                elif nme_movement_ph == 2:
                     nme_game.x += 1    

            #WORK IN PROGRESS. NOT DONE, MAINMENU / SCORESCREEN!!!
            if lives < 0:
                run = False
        
        for enemy in enemy_list:
            enemy.move()
        
        for enemy in enemy_list:
            enemy.draw()

        for bullet in char_game_bullet:
            if bullet.colliderect(enemy.hitbox):
                char_game_bullet.remove(bullet)
                

        #char movement
        keys_pressed = pygame.key.get_pressed()
       
        char_movement(keys_pressed, char_game, nme_game_bullet, nme_game)
        bullet_physics(char_game_bullet, char_game, nme_game, nme_game_bullet, nme_spawner)
        score_display()
        lives_display()
        display_window(char_game, nme_game, char_game_bullet, nme_game_bullet, nme_spawner)
        #nme_movement(nme_game)
       # nme_spawn()
        #nme_shooting(nme_game, event)
        # #quit_game()

pygame.QUIT

#if __name__ == "__main__":

main()

""" https://www.pygame.org/docs/ref/rect.html """
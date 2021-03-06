from typing import KeysView
import pygame
import os
from pygame import font
import random
from pygame import draw
from pygame import sprite
from pygame.constants import JOYAXISMOTION, K_ESCAPE, KEYDOWN, USEREVENT, K_e
from pygame.sprite import Sprite, collide_mask
from pygame import mixer

pygame.init()
#width, height = 1280, 960
width, height = 1200, 600
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
lives = 999
bullet_delay = 350
nme_game_bullet = USEREVENT + 1
nme_spawner = USEREVENT + 0
nme_spawn_list = [5]
nme_amount = 20
nme_random_movement_list = []
shuffled_list = []
jump_amount = 999
#for i in range(jump_amount):
    #nme_random_movement_list.append(random.randint(1,5))

print(nme_random_movement_list)

#Initialize controller
joysticks = []
for i in range(pygame.joystick.get_count()):
    joysticks.append(pygame.joystick.Joystick(i))
for joystick in joysticks:
    joystick.init()


#sounds (Mixkit.com)
mixer.music.load(os.path.join('sounds', 'diff_increase_sound.wav'))

GAMEOVER = "Game Over"
FONTNAME = 'freesansbold.ttf'
GAMEOVERTXTCOLOR = (150, 150, 150)
CENTERSCREENPOS = (width / 2 , height / 2)
center_score = (550, 400)


bg = pygame.image.load(os.path.join('img', 'resizedImage.png')).convert_alpha()
bg_scaled = pygame.transform.scale(bg, (width, height))

#score display
score = 0
font = pygame.font.Font('freesansbold.ttf', 32)

def score_display():
    score_game = font.render("Score: " + str(score), True, (0, 0, 0))
    window.blit(score_game, (950, 700))

char_border_h = int(height * 0.4)

def lives_display():
    lives_game = font.render("Lives: " + str(lives), True, (0,0,0))
    window.blit(lives_game, (20, 700))
    pygame.display.update()




# x-kord, y-kord, width, height
wall = pygame.Rect(0, char_border_h, width, height)

#char_lives = 3
char_w, char_h = 64, 64
char_x, char_y = width/2 - char_w, 500
char_img = pygame.image.load(os.path.join('img', 'ship.png'))
char = pygame.transform.scale(char_img, (char_w, char_h))


nme_x, nme_y = -100, 100
nme_w, nme_h = 80, 33
nme_img = pygame.image.load(os.path.join('img', 'enemy_1.png'))
nme = pygame.transform.scale(nme_img, (nme_w, nme_h))
nmes_sprite = pygame.transform.scale(nme_img, (nme_w, nme_h))
nme_border_h = char_border_h - nme_h - 30

bullet_w, bullet_h = 10, 25
char_bullet_img = pygame.image.load(os.path.join('img', 'stor_bullet.png'))
char_bullet = pygame.transform.scale(char_bullet_img, (bullet_w, bullet_h))
nme_bullet_img = pygame.image.load(os.path.join('img', 'nmebullet.png'))
nme_bullet = pygame.transform.scale(nme_bullet_img, (bullet_w, bullet_h))

#Everything enemy
class enemy(pygame.sprite.Sprite):
    def __init__(self):
        super().__init__()
        self.x = random.randint(0, 1)
        self.y = 150
        self.moveX = 5
        self.moveY = 0
        self.shoot = 350

    def move(self):
            self.x += self.moveX 
            if score == 15:
                self.moveX = 10
            if score == 30:
                self.moveX = 13
            if score == 45:
                self.moveX = 17
            if score == 60:
                self.moveX = 20
            if score == 75:
                self.moveX = 23
            if score == 100:
                self.moveX = 30

            if self.y >= 500:
                self.y = 500
                self.moveY = 0
                self.moveX = 0


            frac = width / 5
            if self.x <= 0:
                self.moveX = self.moveX * -1
                self.y += self.moveY
            elif self.x >= frac:
                nme_random_movement_list.append(random.randint(0, 1))
                print(nme_random_movement_list)
                if nme_random_movement_list[0] == 1:
                    self.moveX = self.moveX
                else:
                    self.moveX = self.moveX * -1
                nme_random_movement_list.pop(0)
            elif self.x >= frac * 2:
                nme_random_movement_list.append(random.randint(0, 1))
                print(nme_random_movement_list)
                if nme_random_movement_list[0] == 1:
                    self.moveX = self.moveX
                else:
                    self.moveX = self.moveX * -1
                nme_random_movement_list.pop(0)
            elif self.x >= frac * 3:
                nme_random_movement_list.append(random.randint(0, 1))
                print(nme_random_movement_list)
                if nme_random_movement_list[0] == 1:
                    self.moveX = self.moveX
                else:
                    self.moveX = self.moveX * -1
                nme_random_movement_list.pop(0)
            elif self.x >= frac * 4:
                nme_random_movement_list.append(random.randint(0, 1))
                print(nme_random_movement_list)
                if nme_random_movement_list[0] == 1:
                    self.moveX = self.moveX
                else:
                    self.moveX = self.moveX * -1
                nme_random_movement_list.pop(0)
            elif self.x >= width:
                nme_random_movement_list.append(random.randint(0, 1))
                print(nme_random_movement_list)
                if nme_random_movement_list[0] == 1:
                    self.moveX = self.moveX
                else:
                    self.moveX = self.moveX * -1
                nme_random_movement_list.pop(0)


    def draw(self):
        window.blit(nme, (self.x, self.y))
        self.hitbox = (self.x, self.y, 70, 30)

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
    window.blit(bg_scaled, (0,0))
    window.blit(char, (char_game.x, char_game.y))
    window.blit(nme, (nme_game.x, nme_game.y))

    for bullets in char_game_bullet:
        pygame.draw.rect(window, blue, bullets)

    for bullets in nme_game_bullet:
        pygame.draw.rect(window, red, bullets)


def char_movement(keys_pressed, char_game, nme_game_bullet, nme_game):
    #char movement
        if keys_pressed[pygame.K_a] or keys_pressed[pygame.K_LEFT]:
            char_game.x -= char_velocity
        if keys_pressed[pygame.K_d] or keys_pressed[pygame.K_RIGHT]:
            char_game.x += char_velocity
        if keys_pressed[pygame.K_s] or keys_pressed[pygame.K_DOWN]:
            char_game.y += char_velocity 
        if keys_pressed[pygame.K_w] or keys_pressed[pygame.K_UP]:
            char_game.y -= char_velocity
    #char screen border
        if char_game.x < 0:
            char_game.x = 0
        if char_game.x > width-char_w:
            char_game.x = width-char_w
        if char_game.y > height-char_h:
            char_game.y = height-char_h
        if char_game.y < char_border_h:
            char_game.y = char_border_h
        
        if keys_pressed[pygame.K_l]:
            pygame.draw.rect(window, (255, 0, 0), char_game, 2)
            

def powerup(keys_pressed, char_game, char_game_bullet):     
    if keys_pressed[pygame.K_p]:
        bullet = pygame.Rect(char_game.x + char_game.width / 2.2 + 1, char_game.y, 5, 25)
        char_game_bullet.append(bullet)

nme_game_bullet_event = USEREVENT + 1

#shot speed events
pygame.time.set_timer(nme_game_bullet_event, bullet_delay)

nme_game_bullet_event15 = USEREVENT + 6
bullet_delay15 = 300
pygame.time.set_timer(nme_game_bullet_event15, bullet_delay15)

nme_game_bullet_event30 = USEREVENT + 7
bullet_delay30 = 250
pygame.time.set_timer(nme_game_bullet_event30, bullet_delay30)

nme_game_bullet_event45 = USEREVENT + 8
bullet_delay45 = 200
pygame.time.set_timer(nme_game_bullet_event45, bullet_delay45)

nme_game_bullet_event60 = USEREVENT + 9
bullet_delay60 = 150
pygame.time.set_timer(nme_game_bullet_event60, bullet_delay60)

nme_game_bullet_event75 = USEREVENT + 10
bullet_delay75 = 100
pygame.time.set_timer(nme_game_bullet_event75, bullet_delay75)

nme_game_bullet_event100 = USEREVENT + 11
bullet_delay100 = 75
pygame.time.set_timer(nme_game_bullet_event100, bullet_delay100)

nme_game_bullet_event115 = USEREVENT + 12
bullet_delay115 = 50
pygame.time.set_timer(nme_game_bullet_event115, bullet_delay115)


def bullet_physics(char_game_bullet, char_game, nme_game, nme_game_bullet):
    #Bullet physics for main character.
    for bullet in char_game_bullet:
        bullet.y -= bullet_velocity
        if nme_game.colliderect(bullet):
            char_game_bullet.remove(bullet)
        elif bullet.y > height:
            char_game_bullet.remove(bullet)
    #Bullet physics for enemy.
    for bullet in nme_game_bullet:
        bullet.y += bullet_velocity
        if char_game.colliderect(bullet):
            nme_game_bullet.remove(bullet)
            global lives
            lives -= 1
    

def main():
    char_game = pygame.Rect((char_x, char_y), (char_w, char_h))
    nme_game = pygame.Rect((nme_x, nme_y), (nme_w, nme_h))
   # nmes = pygame.Rect(0, 0, 60, 30)

    char_game_bullet = []
    nme_game_bullet = []
    nme_spawner = []
    enemies.update()
    global score
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
            
            if event.type == pygame.JOYBUTTONDOWN:
                bullet = pygame.Rect(char_game.x + char_game.width / 2.2 + 1, char_game.y, 5, 25)
                char_game_bullet.append(bullet)

            #if event.type == JOYAXISMOTION:


            if event.type == nme_game_bullet_event and score < 15:
                bullet = pygame.Rect(enemy.x + nme_game.width / 2.2 + 1, enemy.y, 5, 25)
                nme_game_bullet.append(bullet)
            
            if score == 14:
                mixer.music.play()
            
            if event.type == nme_game_bullet_event15 and score >= 15 and score < 30:
                bullet = pygame.Rect(enemy.x + nme_game.width / 2.2 + 1, enemy.y, 5, 25)
                nme_game_bullet.append(bullet)

            if score == 29:
                mixer.music.play()

            if event.type == nme_game_bullet_event30 and score >= 30 and score < 45:
                bullet = pygame.Rect(enemy.x + nme_game.width / 2.2 + 1, enemy.y, 5, 25)
                nme_game_bullet.append(bullet)

            if score == 44:
                mixer.music.play()

            if event.type == nme_game_bullet_event45 and score >= 45 and score < 60:
                bullet = pygame.Rect(enemy.x + nme_game.width / 2.2 + 1, enemy.y, 5, 25)
                nme_game_bullet.append(bullet) 
            
            if score == 59:
                mixer.music.play()
            
            if event.type == nme_game_bullet_event60 and score >= 60 and score < 75:
                bullet = pygame.Rect(enemy.x + nme_game.width / 2.2 + 1, enemy.y, 5, 25)
                nme_game_bullet.append(bullet)

            if score == 74:
                mixer.music.play()

            if event.type == nme_game_bullet_event75 and score >= 75 and score < 100:
                bullet = pygame.Rect(enemy.x + nme_game.width / 2.2 + 1, enemy.y, 5, 25)
                nme_game_bullet.append(bullet)
            
            if score == 99:
                mixer.music.play()
            
            if event.type == nme_game_bullet_event100 and score >= 100 and score < 115:
                bullet = pygame.Rect(enemy.x + nme_game.width / 2.2 + 1, enemy.y, 5, 25)
                nme_game_bullet.append(bullet)

            if score == 114:
                mixer.music.play()

            if event.type == nme_game_bullet_event115 and score >= 115:
                bullet = pygame.Rect(enemy.x + nme_game.width / 2.2 + 1, enemy.y, 5, 25)
                nme_game_bullet.append(bullet)
                   
            #if lives < 0:
               #run = False

        for enemy in enemy_list:
            enemy.move()
        
        for enemy in enemy_list:
            enemy.draw()

        for bullet in char_game_bullet:
            if bullet.colliderect(enemy.hitbox):
                char_game_bullet.remove(bullet)
                
                score += 1
        
        if lives <= 0:
            #print("End")
            window.fill(black)
            font = pygame.font.Font(FONTNAME, 30)
            text_surface = font.render(GAMEOVER, True, GAMEOVERTXTCOLOR)
            text_rect = text_surface.get_rect()
            text_rect.center = CENTERSCREENPOS
            window.blit(text_surface, text_rect)
            pygame.display.update()
            pygame.time.wait(3000)
            run = False

        #char movement
        keys_pressed = pygame.key.get_pressed()
       
        char_movement(keys_pressed, char_game, nme_game_bullet, nme_game)
        bullet_physics(char_game_bullet, char_game, nme_game, nme_game_bullet)
        score_display()
        lives_display()
        display_window(char_game, nme_game, char_game_bullet, nme_game_bullet)
        powerup(keys_pressed, char_game, char_game_bullet)

        if keys_pressed[pygame.K_ESCAPE]:
            run = False

pygame.QUIT

#if __name__ == "__main__":

main()

""" https://www.pygame.org/docs/ref/rect.html """
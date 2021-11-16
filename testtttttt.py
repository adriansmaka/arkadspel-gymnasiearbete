import tkinter as tk
import pygame
import time
import random


def shutdown():
    root.destroy()
#Beginning of the game code for mainmenu link    
def Begin():

pygame.init()
#display size
display_width = 640
display_height = 750

gameDisplay = pygame.display.set_mode((display_width,display_height))

pygame.display.set_caption ("Spellmaster")
#Images for wizard sprite
wizard_right = [pygame.image.load('right_1.png'), pygame.image.load('right_3.png'), pygame.image.load('right_2.png'), pygame.image.load('right_4.png'), pygame.image.load('right_5.png')]
wizard_left = [pygame.image.load('left_1.png'), pygame.image.load('left_3.png'), pygame.image.load('left_2.png'), pygame.image.load('left_4.png'), pygame.image.load('left_5.png')]
still = pygame.image.load("wizardsprite.png")
background = pygame.image.load("background.png")
clock = pygame.time.Clock()

score = 0

class player(object):
    def __init__ (self,x,y,width,height):
        self.x = x
        self.y = y
        self.width = width
        self.height = height
        self.vel = 4
        self.steps= 0
        self.left = False
        self.right = False
        self.hitbox = (self.x + 20, self.y, 50, 60)

    #blit the character on screen
    def draw(self,gameDisplay):
        if self.steps + 1 >=27:
            self.steps = 0

        if self.left:
            gameDisplay.blit(wizard_left [self.steps//20], (self.x,self.y))
            self.steps +=1

        elif self.right:
            gameDisplay.blit(wizard_right [self.steps//20], (self.x,self.y))
            self.steps +=1

        else:
            gameDisplay.blit(still, (self.x,self.y))
            self.steps=0
        self.hitbox = (self.x + 20, self.y, 50, 60)
        #pygame.draw.rect(gameDisplay, (255,0,0),self.hitbox,2)

#FIRESPELL

class projectile(object):
    def __init__(self,x,y,radius,color,facing):
        self.x = x
        self.y = 662
        self.radius = radius
        self.color = color

        self.facing = 0
        self.vel = 10


    def draw(self,gameDisplay):
        pygame.draw.circle(gameDisplay, self.color, (self.x,self.y), self.radius)

#ENEMY CLASS
class enemy(object):
        redspider= [pygame.image.load('redspider_right.png'), pygame.image.load('redspider_left.png'), pygame.image.load('redspider_right.png'), pygame.image.load('redspider_left.png')]

        def __init__(self,x,y,width,height,end):
                self.x=x
                self.y=y
                self.width = width
                self.height = height
                self.end= end
                self.vel = 1.4
                self.walkCount = 0
                self.path = [self.y, self.end]
                self.hitbox = (self.x + 20, self.y, 70, 60)
                self.health = 0.2
                self.visible = True


        def draw(self,gameDisplay):
            self.move()
            if self.visible:
                if self.walkCount + 1 >= 27:
                    self.walkCount = 0
                else:
                    gameDisplay.blit(self.redspider[self.walkCount //2], (self.x, self.y))
                    self.walkCount += 0
                self.hitbox = (self.x + 2, self.y, 70, 60)
                #pygame.draw.rect(gameDisplay, (255,0,0), self.hitbox,2)


        def move(self):
            if self.vel > 0:
                if self.y + self.vel < self.path[1]:
                    self.y += self.vel


        def collision(self):
            if self.health > 0:
                self.health-= 1
            else:
                self.visible= False
            print("HIT")





def redraw():
    gameDisplay.blit(background, (0,0))
    text = font.render('SCORE: ' + str(score), 1,(255,0,0))
    gameDisplay.blit(text, (500,13))
    wizard.draw(gameDisplay)
    redspider.draw(gameDisplay)
    for bullet in bullets:
        bullet.draw(gameDisplay)


    pygame.display.update()


#MAIN LOOP

pygame.font.init()
font = pygame.font.SysFont('Engravers MT', 30)
wizard=player(300, 662, 80, 84)
redspider=enemy(360,80,80,84,650)
spides = []
shootControl = 0
bullets =[]
crashed = False
while not crashed:
    clock.tick(120)


    if shootControl >0:
        shootControl+=1
    if shootControl > 3:
        shootControl=0

    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            crashed = True


    for bullet in bullets:
        if bullet.y - bullet.radius < redspider.hitbox[1] + redspider.hitbox[3] and bullet.y + bullet.radius > redspider.hitbox[1]:
            if bullet.x + bullet.radius > redspider.hitbox[0] and bullet.x - bullet.radius < redspider.hitbox[0] + redspider.hitbox[2]:
                redspider.collision()
                score += 1
                bullets.pop(bullets.index(bullet))

        if bullet.x < 500 and bullet.x > 0:
            bullet.y -= bullet.vel
        else:
            bullets.pop(bullets.index(bullet))

    keys = pygame.key.get_pressed()

    if keys[pygame.K_a] and wizard.x > wizard.vel:
            #if event.key == pygame.K_a and wizard.x > wizard.vel:
                wizard.x -= wizard.vel
                wizard.left= True
                wizard.right= False

    elif keys [pygame.K_d] and wizard.x < 560:
                wizard.x += wizard.vel
                wizard.right= True
                wizard.left=False

    if keys [pygame.K_SPACE] and shootControl ==0:
            if wizard.left:
                facing = 0
            else:
                facing = 0

            if len(bullets) < 500:
               bullets.append(projectile(round(wizard.x + wizard.width //2), round(wizard.y + wizard.height//2), 5, (255,0,0), facing))

            shootControl=1



    if event.type == pygame.KEYUP:
            if event.key == pygame.K_a or event.key == pygame.K_d:
                wizard.left= False
                wizard.right=False




    redraw()

pygame.quit()
shutdown
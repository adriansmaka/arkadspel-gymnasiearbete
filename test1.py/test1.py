from typing import KeysView
import pygame
import os

pygame.init()
#width, height = 1280, 960
width, height = 1100, 748
window = pygame.display.set_mode((width, height))
fps = 60
velocity = 4
white = (255, 255, 255)

char_img = pygame.image.load(os.path.join('img', 'ship.png'))
char = pygame.transform.scale(char_img, (50, 50))

nme_img = pygame.image.load(os.path.join('img', 'enemy_1.png'))
nme = pygame.transform.scale(nme_img, (87, 50))

def display_window(char_game, nme_game):
    window.fill(white)
    window.blit(char, (char_game.x, char_game.y))
    window.blit(nme, (490, 200))
    pygame.display.update()

def char_movement(keys_pressed, char_game):
        if keys_pressed[pygame.K_a]:
            char_game.x -= velocity
        if keys_pressed[pygame.K_d]:
            char_game.x += velocity
        if keys_pressed[pygame.K_s]:
            char_game.y += velocity 
        if keys_pressed[pygame.K_w]:
            char_game.y -= velocity

def main():
    char_game = pygame.Rect((490, 500), (50, 50))
    nme_game = pygame.Rect((490, 200), (87, 50))

    clock = pygame.time.Clock()
    run = True
    while run:
        clock.tick(fps)
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                run = False
            
    
            
        keys_pressed = pygame.key.get_pressed()
        char_movement(keys_pressed, char_game)
        
        
        
        """ if keys_pressed[pygame.K_a]:
            char_game.x -= velocity
        if keys_pressed[pygame.K_d]:
            char_game.x += velocity
        if keys_pressed[pygame.K_s]:
            char_game.y += velocity 
        if keys_pressed[pygame.K_w]:
            char_game.y -= velocity"""

        
        if char_game.x >= 0:
            char_game.x ==  0
        if char_game.x <= 1100:
            char_game.x ==  1100
        if char_game.y >= 0:
            char_game.y ==  0
        if char_game.y <= 748:
            char_game.y ==  748

        color = (255,0,0)
        border = pygame.draw.rect(window, color, pygame.Rect(0, 0, 1100, 748), 1)
        pygame.display.flip()

        if char_game.colliderect(border):
            print("Kraschat!"+1)




        """ char.x = 490
        char.y = 500
        dx = 5
        dy = 7

        #events = pygame.key.get_pressed()
        #for event in events:
            #if event.type == pygame.KEYDOWN:
                #if event.key == pygame.K_LEFT:
                    #char.x -= dx
                #if event.key == pygame.K_RIGHT:
                    #char.x += dx """

        display_window(char_game, nme_game)

pygame.QUIT

#if __name__ == "__main__":

main()
from typing import KeysView
import pygame
import os

pygame.init()
#width, height = 1280, 960
width, height = 1100, 748
window = pygame.display.set_mode((width, height))
fps = 60
speed = 5 
white = (255, 255, 255)

char = pygame.image.load(os.path.join('img', 'ship.png'))
char = pygame.transform.scale(char, (85, 80))
nme = pygame.image.load(os.path.join('img', 'enemy_1.png'))
nme = pygame.transform.scale(nme, (87, 50))



def display_window(char_game):
    window.fill(white)
    window.blit(char, (490, 500))
    window.blit(nme, (490, 200))
    pygame.display.update()
    

def main():
    char_game = pygame.Rect((490, 500), (95, 70))
    nme_game = pygame.Rect((490, 200), (87,50))

    clock = pygame.time.Clock()
    run = True
    while run:
        clock.tick(fps)
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                run = False
            
        keys_pressed = pygame.key.get_pressed()

        if event.type == pygame.KEYDOWN:
            if event.key == ord('a'):
                print('left')
            if event.key == ord('d'):
                print('right')
            if event.key == pygame.K_UP or event.key == ord('w'):
                print('jump')

        if event.type == pygame.KEYUP:
            if event.key == ord('a'):
                print('left stop')
            if event.key == ord('d'):
                print('right stop')
            if event.key == ord('q'):
                pygame.quit()
        
        display_window(char_game)

pygame.QUIT

#if __name__ == "__main__":

main()
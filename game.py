from typing import KeysView
import pygame
import os

pygame.init()
#width, height = 1280, 960
width, height = 1100, 748
window = pygame.display.set_mode((width, height))
fps = 60
hastighet = 5 
vit = (255, 255, 255)

karaktär_img = pygame.image.load(os.path.join('img', 'ship.png'))
karaktär = pygame.transform.scale(karaktär_img, (50, 50))

fiende_img = pygame.image.load(os.path.join('img', 'enemy_1.png'))
fiende = pygame.transform.scale(fiende_img, (87, 50))

def display_fönster(karaktär_spel, fiende_spel):
    fönster.fill(vit)
    fönster.blit(karaktär, (490, 500))
    fönster.blit(fiende, (490, 200))
    pygame.display.update()
    

def main():
    karaktär_spel = pygame.Rect((490, 500), (95, 70))
    fiende_spel = pygame.Rect((490, 200), (87, 50))

    clock = pygame.time.Clock()
    run = True
    while run:
        clock.tick(fps)
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                run = False
            
        keys_pressed = pygame.key.get_pressed()
        if keys_pressed[pygame.K_a]:
            karaktär_spel.x -= hastighet
        
        display_fönster(karaktär_spel, fiende_spel)

pygame.QUIT

#if __name__ == "__main__":

main()
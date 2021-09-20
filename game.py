import pygame
import os

pygame.init()
#width, height = 1280, 960
width, height = 1100, 748
fönster = pygame.display.set_mode((width, height))
fps = 60
vit = (255, 255, 255)
karaktär = pygame.image.load(os.path.join('img', 'karaktär.png'))
karaktär = pygame.transform.scale(karaktär, (95, 70))
fiende = pygame.image.load(os.path.join('img', 'fiende_1.png'))

def display_fönster():
    fönster.fill(vit)
    fönster.blit(karaktär, (470, 500))
    pygame.display.update()
    

def main():
    clock = pygame.time.Clock()
    run = True
    while run:
        clock.tick(fps)
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                run = False
            
        display_fönster()

pygame.QUIT

#if __name__ == "__main__":

main()
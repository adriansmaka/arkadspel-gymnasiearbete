import pygame
import os

pygame.init()
#width, height = 1280, 960
width, height = 1100, 740
window = pygame.display.set_mode((width, height))
fps = 60
white = (255, 255, 255)
black = (0, 0, 0)
red = (255, 0, 0)
green = (0, 255, 0)
blue = (0, 0, 255)
nme_n = 1


nme_x, nme_y = 0, 0
nme_w, nme_h = 70, 30
nme_img = pygame.image.load(os.path.join('img', 'nme_rect.png'))
nme = pygame.transform.scale(nme_img, (nme_w, nme_h))


def display_window(nme_game):
    window.fill(white)
    window.blit(nme, (nme_game.x, nme_game.y))
    pygame.display.update()



def nme_movement(nme_game):
    nme_v = 10
    n = 0

#----------- Height update -----------

    n = nme_game.y / nme_h
    print(n)

#----------- X axis movement -----------

    if nme_game.x >= 0 and nme_game.x <= width - nme_w and n % 2 <= 0:
        nme_game.x += nme_v

    elif nme_game.x >= 0 and nme_game.x <= width - nme_w and n % 2 == 1:
        nme_game.x -= nme_v

#----------- Y axis movement -----------

    if nme_game.x == width - nme_w and nme_game.y >= nme_h * n and nme_game.y <= nme_h * n + nme_h:
        nme_game.y += nme_v

    elif nme_game.x == 0 and nme_game.y >= nme_h * n and nme_game.y <= nme_h * n + nme_h:
        nme_game.y += nme_v




def main():
    #starting position, (x, y), (w, h)
    nme_game = pygame.Rect((nme_x, 240), (nme_w, nme_h))

#----------- Game run -----------
    clock = pygame.time.Clock()
    run = True
    while run:
        clock.tick(fps)
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                run = False
            

        nme_movement(nme_game)

        display_window(nme_game)

pygame.QUIT

main()
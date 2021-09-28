import pygame

pygame.init()
width, height = 1100, 748
window = pygame.display.set_mode((width, height))

def main():
    run = True
    while run:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                run = False



keys_pressed = pygame.key.get_pressed()
if keys_pressed[pygame.K_a]:
    print("hello")

main()
import pygame
import os

pygame.init()
size = width, height = 800, 800

screen = pygame.display.set_mode(size)
FPS = 60
clock = pygame.time.Clock()
running = True
image = pygame.image.load('data/arrow.png').convert_alpha()
pygame.mouse.set_visible(False)
x, y = 0, 0
while running:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False
        if event.type == pygame.MOUSEMOTION:
            x, y = event.pos

    screen.fill((0, 0, 0))

    if pygame.mouse.get_focused():
        screen.blit(image, (x, y))

    clock.tick(FPS)
    pygame.display.flip()

pygame.quit()

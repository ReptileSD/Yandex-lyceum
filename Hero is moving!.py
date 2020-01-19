import pygame

pygame.init()
size = width, height = 300, 300

screen = pygame.display.set_mode(size)
FPS = 60
clock = pygame.time.Clock()
running = True
image = pygame.image.load('data/creature.png').convert_alpha()
pygame.mouse.set_visible(False)
x, y = 0, 0
while running:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False
    keys = pygame.key.get_pressed()
    if keys[pygame.K_LEFT]:
        x -= 10
    if keys[pygame.K_RIGHT]:
        x += 10
    if keys[pygame.K_UP]:
        y -= 10
    if keys[pygame.K_DOWN]:
        y += 10

    screen.fill((255, 255, 255))
    screen.blit(image, (x, y))

    clock.tick(FPS)
    pygame.display.flip()

pygame.quit()

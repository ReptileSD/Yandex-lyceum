import pygame
import random


class Bomb(pygame.sprite.Sprite):
    def __init__(self, *groops):
        super().__init__(groops)
        self.images = [load_image('data/bomb.png'), load_image('data/boom.png')]
        self.change_image(0)
        self.rect = self.image.get_rect()
        self.rect.x = random.randrange(width - self.image.get_width())
        self.rect.y = random.randrange(height - self.image.get_height())
        self.exploded = False

    def change_image(self, num):
        self.image = self.images[num]

    def update(self, *args):
        if args \
                and args[0].type == pygame.MOUSEBUTTONDOWN \
                and self.rect.collidepoint(args[0].pos) \
                and not self.exploded:
            self.rect.x += self.image.get_width() // 2
            self.rect.y += self.image.get_height() // 2
            self.change_image(1)
            self.exploded = True
            self.rect.x -= self.image.get_width() // 2
            self.rect.y -= self.image.get_height() // 2


def load_image(filename):
    return pygame.image.load(filename).convert_alpha()


pygame.init()
size = width, height = 500, 500

screen = pygame.display.set_mode(size)
FPS = 60
clock = pygame.time.Clock()
running = True
all_sprites = pygame.sprite.Group()

while len(all_sprites) != 10:
    sprite = Bomb()
    if pygame.sprite.spritecollideany(sprite, all_sprites):
        continue
    sprite.add(all_sprites)

while running:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False
        all_sprites.update(event)

    screen.fill((255, 255, 255))
    all_sprites.draw(screen)
    clock.tick(FPS)
    pygame.display.flip()

pygame.quit()

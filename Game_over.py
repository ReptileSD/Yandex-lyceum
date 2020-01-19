import pygame


class GameoverWindow(pygame.sprite.Sprite):
    def __init__(self, *groops):
        super().__init__(groops)
        self.image = load_image('data/gameover.png')
        self.rect = self.image.get_rect()
        self.rect.x = -width
        self.rect.y = 0
        self.v = 200

    def update(self, *args):
        self.rect.x += self.v / FPS
        if self.rect.x == 0:
            self.v = 0


def load_image(filename):
    return pygame.image.load(filename).convert_alpha()


pygame.init()
size = width, height = 600, 300

screen = pygame.display.set_mode(size)
FPS = 60
clock = pygame.time.Clock()
running = True
all_sprites = pygame.sprite.Group()

GameoverWindow(all_sprites)

while running:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False
    all_sprites.update()
    screen.fill((0, 0, 255))
    all_sprites.draw(screen)
    clock.tick(FPS)
    pygame.display.flip()

pygame.quit()

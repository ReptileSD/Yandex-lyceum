import pygame


class Platform(pygame.sprite.Sprite):
    def __init__(self, pos, *groops):
        super().__init__(groops)
        self.image = pygame.Surface((50, 10))
        self.image.fill((80, 80, 80))
        self.rect = self.image.get_rect()
        self.rect.x = pos[0]
        self.rect.y = pos[1]


class Wall(pygame.sprite.Sprite):
    def __init__(self, pos, *groops):
        super().__init__(groops)
        self.image = pygame.Surface((10, 50))
        self.image.fill((255, 0, 0))
        self.rect = self.image.get_rect()
        self.rect.x = pos[0]
        self.rect.y = pos[1]


class Hero(pygame.sprite.Sprite):
    def __init__(self, pos, *groops):
        super().__init__(groops)
        self.image = pygame.Surface((20, 20))
        self.image.fill((0, 0, 255))
        self.rect = self.image.get_rect()
        self.rect.x = pos[0]
        self.rect.y = pos[1]
        self.falling = True

    def update(self, *args):
        if args:
            if args[0].type == pygame.MOUSEBUTTONDOWN and args[0].button == 3:
                self.rect.x, self.rect.y = args[0].pos
                return
            sprites = pygame.sprite.spritecollide(self, all_walls, False)
            if sprites:
                self.falling = False
            if args[0].type == pygame.KEYDOWN:
                keys = pygame.key.get_pressed()
                if keys[pygame.K_DOWN] and sprites:
                    self.rect.y += 10
                    sprite = pygame.sprite.spritecollide(self, all_platforms, False)
                    if sprite:
                        self.rect.y = min([i.rect.y for i in sprite]) - sprite[0].image.get_height()
                if keys[pygame.K_UP] and sprites:
                    self.rect.y -= 10
                    sprite = pygame.sprite.spritecollide(self, all_platforms, False)
                    if sprite:
                        self.rect.y = max(i.rect.y for i in sprite) + sprite[0].image.get_height()
                if keys[pygame.K_LEFT]:
                    self.rect.x -= 10
                    sprites = pygame.sprite.spritecollide(self, all_platforms, False)
                    if sprites:
                        self.rect.x = min([i.rect.x for i in sprites]) + sprites[0].image.get_width()
                if keys[pygame.K_RIGHT]:
                    self.rect.x += 10
                    sprites = pygame.sprite.spritecollide(self, all_platforms, False)
                    if sprites:
                        self.rect.x = max([i.rect.x for i in sprites]) - self.image.get_width()

                return

    def fall(self, v=50):
        self.rect.y += v / FPS * int(self.falling)
        sprite = pygame.sprite.spritecollide(self, all_platforms, False)
        sprites = pygame.sprite.spritecollide(self, all_walls, False)
        if sprite:
            self.rect.y = sprite[0].rect.y - \
                          self.image.get_height()
            self.falling = False
        else:
            self.falling = not sprites

    def move(self, pos):
        self.rect.x, self.rect.y = pos


def load_image(filename):
    return pygame.image.load(filename).convert_alpha()


pygame.init()
size = width, height = 500, 500

screen = pygame.display.set_mode(size)
FPS = 30
clock = pygame.time.Clock()
running = True
all_sprites = pygame.sprite.Group()
all_platforms = pygame.sprite.Group()
all_walls = pygame.sprite.Group()
all_heroes = pygame.sprite.Group()

while running:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False
        if event.type == pygame.MOUSEBUTTONDOWN:
            if event.button == 1:
                if pygame.key.get_pressed()[pygame.K_LCTRL]:
                    sprite = Wall(event.pos, all_sprites, all_walls)
                    continue
                sprite = Platform(event.pos, all_sprites, all_platforms)
            if event.button == 3:
                if not all_heroes:
                    Hero(event.pos, all_sprites, all_heroes)
                all_heroes.sprites()[0].move(event.pos)

        all_sprites.update(event)
    if all_heroes:
        all_heroes.sprites()[0].fall()
    screen.fill((255, 255, 255))
    all_sprites.draw(screen)
    clock.tick(FPS)
    pygame.display.flip()

pygame.quit()

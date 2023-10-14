import pygame
import sys
import random

"""
Our goals
- Top down game
- We control the player
- we have enemies to avoid
- we can also collect coins
"""
# initialize internal variables
pygame.init()

# variables for screen size
screen_w = 640
screen_h = 480
size = (screen_w, screen_h)

# create the screen for the program
screen = pygame.display.set_mode(size)

# set up clock
clock = pygame.time.Clock()
fps = 60

# groups
enemy_group = pygame.sprite.Group()
coin_group = pygame.sprite.Group()

# game variables
enemy_count = 3
coin_count = 3
player_alive = True

# images
bg_image = pygame.image.load("sprites/background.png")
bg_image = pygame.transform.scale(bg_image, (screen_w, screen_h))


class Player:

    def __init__(self, x, y):
        self.rect = pygame.Rect((x, y), (100, 100))
        self.color = (100, 0, 100)
        self.image = pygame.image.load("sprites/player.png")
        # movement variables
        self.move_r = False
        self.move_l = False
        self.move_d = False
        self.move_u = False
        self.speed = 5

    def update(self):
        """
        update the position and draw the sprite
        :return:
        """
        screen.blit(self.image, (self.rect.x, self.rect.y))
        pygame.draw.rect(screen, self.color, self.rect)
        # update positions
        if self.move_r:
            self.rect.x += self.speed
        elif self.move_l:
            self.rect.x -= self.speed
        elif self.move_d:
            self.rect.y += self.speed
        elif self.move_u:
            self.rect.y -= self.speed


class Coin(pygame.sprite.Sprite):

    def __init__(self, x, y):
        pygame.sprite.Sprite.__init__(self)
        self.image = pygame.image.load("sprites/coin.png")
        self.image = pygame.transform.scale(self.image, (30, 40))
        self.color = (255, 255, 0)
        self.pos = (x, y)
        self.radius = 30
        self.rect = pygame.Rect(
            (self.pos[0] - self.radius, self.pos[1] - self.radius), (20, 40)
        )

    def update(self):
        pygame.draw.rect(screen, self.color, self.rect)
        screen.blit(self.image, (self.rect.x - 10, self.rect.y))


class Enemy(pygame.sprite.Sprite):

    def __init__(self, x, y):
        pygame.sprite.Sprite.__init__(self)
        self.image = pygame.image.load("sprites/enemy.png")
        self.rect = pygame.Rect((x, y), (100, 80))
        self.color = (255, 0, 0)

    def update(self):
        pygame.draw.rect(screen, self.color, self.rect)
        screen.blit(self.image, (self.rect.x - 10, self.rect.y - 50))


for _ in range(enemy_count):
    enemy = Enemy(random.randint(0, screen_w), random.randint(0, screen_h))
    enemy_group.add(enemy)

for _ in range(coin_count):
    coin = Coin(random.randint(0, screen_w), random.randint(0, screen_h))
    coin_group.add(coin)

player = Player(screen_w // 2, screen_h // 2)

while player_alive:
    # tick clock
    clock.tick(fps)
    screen.blit(bg_image, (0, 0))

    # check for collisions

    # check for enemy group collision
    for enemy in enemy_group:
        if player.rect.colliderect(enemy):
            print("colliding with enemy")

    # check for coin group collision
    for coin in coin_group:
        if player.rect.colliderect(coin):
            print("colliding with coin")

    # test for inputs
    for event in pygame.event.get():

        # handle quit events
        if event.type == pygame.QUIT:
            sys.exit()

        # Key down events
        elif event.type == pygame.KEYDOWN:
            if event.key == pygame.K_RIGHT:
                player.move_r = True
            elif event.key == pygame.K_LEFT:
                player.move_l = True
            elif event.key == pygame.K_DOWN:
                player.move_d = True
            elif event.key == pygame.K_UP:
                player.move_u = True

        # key up events
        elif event.type == pygame.KEYUP:
            if event.key == pygame.K_RIGHT:
                player.move_r = False
            elif event.key == pygame.K_LEFT:
                player.move_l = False
            elif event.key == pygame.K_DOWN:
                player.move_d = False
            elif event.key == pygame.K_UP:
                player.move_u = False

    enemy_group.update()
    coin_group.update()



    player.update()

    pygame.display.flip()

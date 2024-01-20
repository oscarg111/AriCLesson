import math

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
enemy_count = 1
coin_count = 3
player_alive = True
score = 0
player_health = 255
attack = False

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
        # pygame.draw.rect(screen, self.color, self.rect)
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
        # pygame.draw.rect(screen, self.color, self.rect)
        screen.blit(self.image, (self.rect.x - 10, self.rect.y))


class Enemy(pygame.sprite.Sprite):

    def __init__(self, x, y):
        pygame.sprite.Sprite.__init__(self)
        self.image = pygame.image.load("sprites/enemy.png")
        self.rect = pygame.Rect((x, y), (100, 80))
        self.color = (255, 0, 0)
        self.speed = 2
        self.health = 100

    def update(self):
        # pygame.draw.rect(screen, self.color, self.rect)

        # Calculate the direction and distance to the player
        dx = player.rect.x - self.rect.x
        dy = player.rect.y - self.rect.y
        distance = math.sqrt(dx ** 2 + dy ** 2)

        # Move towards player
        if distance != 0:
            dx /= distance
            dy /= distance
            self.rect.x += int(dx * self.speed)
            self.rect.y += int(dy * self.speed)
        if self.health >= 0:
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
        to_player_dist = math.sqrt((player.rect.x - enemy.rect.x)**2 + (player.rect.y - enemy.rect.y)**2)
        if to_player_dist <= 150 and attack:
            print(enemy.health)
            enemy.health -= 20

        if enemy.health <= 0:
            enemy_group.remove(enemy)

        if player.rect.colliderect(enemy):
            print("colliding with enemy")
            player_health -= 5

    # check for coin group collision
    for coin in coin_group:
        if player.rect.colliderect(coin):
            print("colliding with coin")
            score += 5
            coin_group.remove(coin)
            coin1 = Coin(random.randint(0, screen_w), random.randint(0, screen_h))
            coin_group.add(coin1)

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
            elif event.key == pygame.K_SPACE:
                attack = True


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
            elif event.key == pygame.K_SPACE:
                attack = False

    enemy_group.update()
    coin_group.update()
    player.update()

    # Display and update score
    font = pygame.font.Font(None, 36)
    score_text = font.render(f"Score: {score}", True, (31, 26, 26))
    screen.blit(score_text, (10, 10))

    # Player health
    health_text = font.render(f"Health: ", True, (31, 26, 26))
    screen.blit(health_text, (130, 20))
    health_rect = pygame.Rect((225, 20), (player_health, 30))
    pygame.draw.rect(screen, (255-player_health, player_health, 0), health_rect)

    if player_health <= 0:
        player_alive = False

    pygame.display.flip()

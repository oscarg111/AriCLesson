import pygame
import sys

# first thing in any pygame program
pygame.init()

# make the size of the screen
size = width, height = 640, 480

# make a screen for the program
screen = pygame.display.set_mode(size)

# make a clock/fps for the program
clock = pygame.time.Clock()
fps = 30

# define shape variables
shape_position = (width / 2, height / 2)
shape_size = (100, 100)
shape_rect = pygame.Rect(shape_position, shape_size)

# variables for circle
circle_pos = (50, 50)

# game colors
shape_color = (142, 58, 60)
line_color = (51, 116, 48)
circle_color = (36, 166, 171)

# game loop
while True:
    clock.tick(fps)

    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            sys.exit()
        if event.type == pygame.MOUSEBUTTONDOWN:
            if event.button == pygame.BUTTON_LEFT:
                # setting the square position to be that of a mouse left click
                shape_rect.center = event.pos
            if event.button == pygame.BUTTON_RIGHT:
                # set the circle pos to the right button click location
                circle_pos = event.pos
        if event.type == pygame.KEYDOWN:
            if event.key == pygame.K_SPACE:
                shape_color_original = shape_color
                shape_color = circle_color
                circle_color = line_color
                line_color = shape_color_original

    # fill screen with solid color
    screen.fill((209, 129, 25))

    # fill rect area with shape color
    screen.fill(shape_color, rect=shape_rect)

    # Draw circle on the screen
    pygame.draw.circle(screen, circle_color, circle_pos, 25)

    # Draw line between shapes
    pygame.draw.line(screen, line_color, circle_pos, shape_rect.center, 4)

    # updates the pygame screen
    pygame.display.flip()

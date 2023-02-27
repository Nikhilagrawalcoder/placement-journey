import pygame
import random

# initialize Pygame
pygame.init()

# set up the screen
screen_width = 800
screen_height = 600
screen = pygame.display.set_mode((screen_width, screen_height))

# load the images
player_image = pygame.image.load("player.png")
obstacle_image = pygame.image.load("obstacle.png")

# define the player's position and speed
player_x = screen_width // 2
player_y = screen_height - 100
player_speed = 5

# define the obstacles
obstacles = []
for i in range(5):
    x = random.randint(0, screen_width - obstacle_image.get_width())
    y = random.randint(-500, -obstacle_image.get_height())
    obstacles.append((x, y))

# define the game loop
running = True
while running:
    # handle events
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False

    # handle player input
    keys = pygame.key.get_pressed()
    if keys[pygame.K_LEFT]:
        player_x -= player_speed
    if keys[pygame.K_RIGHT]:
        player_x += player_speed

    # update the obstacles
    for i in range(len(obstacles)):
        x, y = obstacles[i]
        y += 5
        if y > screen_height:
            y = random.randint(-500, -obstacle_image.get_height())
            x = random.randint(0, screen_width - obstacle_image.get_width())
        obstacles[i] = (x, y)

    # check for collisions
    for obstacle in obstacles:
        if pygame.Rect(obstacle[0], obstacle[1], obstacle_image.get_width(), obstacle_image.get_height()).colliderect(pygame.Rect(player_x, player_y, player_image.get_width(), player_image.get_height())):
            running = False

    # clear the screen
    screen.fill((0, 0, 0))

    # draw the player
    screen.blit(player_image, (player_x, player_y))

    # draw the obstacles
    for obstacle in obstacles:
        screen.blit(obstacle_image, obstacle)

    # update the screen
    pygame.display.flip()

# clean up
pygame.quit()

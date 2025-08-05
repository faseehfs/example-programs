import pygame
import math

pygame.init()
screen = pygame.display.set_mode((1280, 720))
clock = pygame.time.Clock()
running = True

width, height = screen.get_size()
origin_y = height // 2
scale_x = 40
scale_y = 100

x = 0
points = []

while running:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False
        if event.type == pygame.MOUSEBUTTONUP:
            points.clear()
            x = 0

    screen.fill("black")

    if x < width:
        y = math.sin(x / scale_x) * scale_y
        points.append((x, origin_y - int(y)))
        x += 1

    if len(points) > 1:
        pygame.draw.lines(screen, "white", False, points, 2)

    pygame.display.flip()
    clock.tick(60)

pygame.quit()

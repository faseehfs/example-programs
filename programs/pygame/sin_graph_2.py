import pygame
import math


def lower_color(color, intensity):
    return tuple(max(0, component - intensity) for component in color)


# In Python, `(expr for item in iterable)` is always a generator expression, not a tuple, whereas `[expr for item in iterable]` is a list.


pygame.init()
screen = pygame.display.set_mode((1280, 720))
clock = pygame.time.Clock()
running = True

width, height = screen.get_size()
origin_y = height // 2
scale_x = 20
scale_y = 50

x = 0
points = []

while running:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False

    screen.fill("black")

    y = math.sin(x / scale_x) * scale_y
    points.append((x, origin_y - int(y)))
    x += 1

    color = (255, 255, 255)
    last_point_drawn = (0, 0)
    for i in range(len(points) - 1, 0, -1):
        pygame.draw.line(screen, color, points[i], points[i - 1], 2)
        color = lower_color(color, 2)
        if color == (0, 0, 0):
            last_point_drawn = points[i]
            break

    if last_point_drawn[0] > width:
        x = 0
        points.clear()

    pygame.display.flip()
    clock.tick(60)

pygame.quit()

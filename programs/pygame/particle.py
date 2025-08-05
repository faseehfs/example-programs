import pygame
from pygame.math import Vector2

class Drop():
    def __init__(self, position: Vector2, speed: float=100, length: float=4, width: float=2):
        self.position = position
        self.speed = speed
        self.length = length
        self.width = width
    
        self.velocity = None

    def refresh(self, surface: pygame.Surface):
        self.velocity = (Vector2(pygame.mouse.get_pos()) - self.position).normalize() * self.speed
        self.position += self.velocity * dt
        pygame.draw.line(
            surface, (255, 255, 255),
            self.position,
            self.position - self.velocity.normalize() * self.length,
            self.width
        )

pygame.init()
screen = pygame.display.set_mode((1280, 720))
clock = pygame.time.Clock()
dt = 0
running = True

drop = Drop(Vector2(0, 0))

while running:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False

    screen.fill("black")

    drop.refresh(screen)

    pygame.display.flip()
    dt = clock.tick(30) / 1000

pygame.quit()

import pygame
from pygame.math import Vector2

class Drop():
    def __init__(self, position: Vector2, velocity: Vector2, length: float):
        self.position = position
        self.velocity = velocity
        self.length = length
    
    def refresh(self, surface: pygame.Surface):
        self.position += self.velocity * dt
        pygame.draw.line(
            surface, (255, 255, 255),
            self.position,
            self.position - self.velocity.normalize() * self.length
        )

pygame.init()
screen = pygame.display.set_mode((1280, 720))
clock = pygame.time.Clock()
dt = 0
running = True

drop = Drop(Vector2(0, 0), Vector2(10, 10), 5)

while running:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False

    screen.fill("black")

    drop.refresh(screen)

    pygame.display.flip()
    dt = clock.tick(30) / 1000
pygame.quit()

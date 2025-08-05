import pygame
from pygame.math import Vector2

class Drop():
    def __init__(self, position: Vector2, length: float, speed: float):
        self.position = position
        self.length = length
        self.speed = speed
    
        self.velocity = None

    def refresh(self, surface: pygame.Surface):
        self.velocity = (Vector2(pygame.mouse.get_pos()) - self.position).normalize() * self.speed
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

drop = Drop(Vector2(0, 0), 5, 100)

while running:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False

    screen.fill("black")

    drop.refresh(screen)

    pygame.display.flip()
    dt = clock.tick(30) / 1000

pygame.quit()

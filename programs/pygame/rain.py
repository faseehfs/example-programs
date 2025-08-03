import pygame
import random


class Raindrops:
    # drops = [] # shared across all instances of the class.
    # Modifying drops from any instance will affect all other instances,
    # unless you explicitly shadow it with an instance variable.
    # That is not what we want. So, use `self` in the constructor.
    # if drops = [] is present here and also in the constructor,
    # it will be ignored by instances.

    def __init__(
        self,
        area,
        drops_per_frame=1,
        length=10,
        width=2,
        color=(255, 255, 255),
        tail=True,
    ):
        self.area = area
        self.drops_per_frame = drops_per_frame
        self.length = length
        self.width = width
        self.color = color
        self.color_step = max(color) // length
        self.drops = []
        self.tail = tail

    def move(self):
        for i in range(len(self.drops)):
            self.drops[i] = (self.drops[i][0], self.drops[i][1] + 1)

    def add(self):
        for i in range(self.drops_per_frame):
            self.drops.append((random.randrange(self.area[0]), 0))

    def draw(self, surface: pygame.Surface):
        if self.tail:
            for i, drop in enumerate(self.drops):
                start_pos = drop
                color = self.color
                while color != (0, 0, 0):
                    end_pos = (start_pos[0], start_pos[1] - 1)
                    pygame.draw.line(surface, color, start_pos, end_pos, self.width)
                    start_pos = end_pos
                    color = tuple([max(0, component - 10) for component in color])
                if start_pos[1] > self.area[1]:
                    print(self.drops.pop(i))
        else:
            for drop in self.drops:
                pygame.draw.circle(surface, self.color, drop, self.width / 2)


pygame.init()
screen = pygame.display.set_mode((1280, 720))
clock = pygame.time.Clock()
running = True

screen_size = screen.get_size()
raindrops = Raindrops(screen_size, 1)

while running:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False

    screen.fill("black")
    raindrops.move()
    raindrops.add()
    raindrops.draw(screen)

    pygame.display.flip()
    clock.tick(60)

pygame.quit()

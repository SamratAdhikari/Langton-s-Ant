import math
import pygame
from collections import deque
from random import choice,  randrange


class Ant:
    def __init__(self, app, pos, color):
        self.app = app
        self.color = color
        self.x, self.y = pos
        self.increments = deque([(1, 0), (0, 1), (-1, 0), (0, -1)])

    def run(self):
        value = self.app.grid[self.y][self.x]
        self.app.grid[self.y][self.x] = not value


        size = self.app.cell_size
        center = self.x*size, self.y*size

        if value:
            pygame.draw.circle(self.app.screen, self.color, center, size)

        self.increments.rotate(1) if value else self.increments.rotate(-1)
        dx, dy = self.increments[0]
        self.x = (self.x + dx) % self.app.cols
        self.y = (self.y + dy) % self.app.rows



class App:
    def __init__(self, CELL_SIZE=6):
        pygame.init()
        self.screen = pygame.display.set_mode((0, 0), pygame.FULLSCREEN)
        self.clock = pygame.time.Clock()

        self.cell_size = CELL_SIZE
        WIDTH, HEIGHT = pygame.display.get_surface().get_size()
        self.rows, self.cols = HEIGHT // CELL_SIZE, WIDTH // CELL_SIZE
        self.grid = [[0 for col in range(self.cols)] for row in range(self.rows)]


        colors1 = [(50, _, 100) for _ in range(256)]
        colors2 = [(_, 0, 50) for _ in range(256)]



        ants1 = [Ant(self, [self.cols // 3, self.rows // 2],
                     choice(colors1)) for i in range(400)]
        ants2 = [Ant(self, [self.cols - self.cols // 3, self.rows // 2],
                     choice(colors2)) for i in range(400)]
        self.ants = ants1 + ants2

    @staticmethod
    def get_color():
        channel = lambda: randrange(10, 200)
        return channel(), channel(), channel()

    def run(self):
        while True:
            [ant.run() for ant in self.ants]

            [exit() for _ in pygame.event.get() if _.type == pygame.KEYDOWN and _.key == pygame.K_ESCAPE]
            pygame.display.flip()
            self.clock.tick()


if __name__ == '__main__':
    app = App()
    app.run()


import pygame
from collections import deque
from random import choice, randrange

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
        rect = self.x*size, self.y*size, size-1, size-1

        if value:
            pygame.draw.rect(self.app.screen, pygame.Color('white'), rect)
        else:
            pygame.draw.rect(self.app.screen, self.color, rect)

        self.increments.rotate(1) if value else self.increments.rotate(-1)
        dx, dy = self.increments[0]
        self.x = (self.x - dx) % self.app.cols
        self.y = (self.y - dy) % self.app.rows

class App:
    def __init__(self, CELL_SIZE=8):
        pygame.init()
        self.screen = pygame.display.set_mode((0, 0), pygame.FULLSCREEN)
        self.clock = pygame.time.Clock()

        self.cell_size = CELL_SIZE
        WIDTH, HEIGHT = pygame.display.get_surface().get_size()
        self.rows, self.cols = HEIGHT//CELL_SIZE, WIDTH//CELL_SIZE
        self.grid = [[0 for col in range(self.cols)] for row in range(self.rows)]

        self.ants = [Ant(self, [randrange(self.cols), randrange(self.rows)], self.get_color()) for _ in range(15)]


    @staticmethod
    def get_color():
        channel = lambda: randrange(30 ,220)
        return channel(), channel(), channel()

    def run(self):
        running = True

        while running:
            [ant.run() for ant in self.ants]

            [exit() for _ in pygame.event.get() if _.type == pygame.KEYDOWN and _.key == pygame.K_ESCAPE]
            pygame.display.flip()
            self.clock.tick()


if __name__ == '__main__':
    app = App()
    app.run()
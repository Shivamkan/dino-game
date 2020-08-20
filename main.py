import dino
import pygame
import sys


class main:
    def __init__(self, width, height):
        self.width = width
        self.height = height
        self.dino = dino.player()
        self.size = self.width, self.height
        self.screen = pygame.display.set_mode(self.size)

    def handleInput(self):
        self.event = pygame.event.get()
        self.dino.handleInput(self.event)
        for event in self.event:
            if event.type == pygame.QUIT:
                sys.exit()

    def draw(self):
        self.screen.fill((000, 000, 000))
        self.dino.drawplayer(self.screen)
        pygame.display.flip()

    def run(self):
        self.handleInput()
        self.draw()


run = main(500, 500)
while True:
    run.run()

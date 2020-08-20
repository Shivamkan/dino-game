import dino
import pygame
import sys
import map

clock = pygame.time.Clock()

class main:
    def __init__(self, width, height):
        self.width = width
        self.height = height
        self.map = map.map(height,width)
        self.dino = dino.player(height)
        self.size = self.width, self.height
        self.screen = pygame.display.set_mode(self.size)

    def handleInput(self):
        self.event = pygame.event.get()
        self.dino.handleInput(self.event)
        for event in self.event:
            if event.type == pygame.QUIT:
                sys.exit()

    def handlecollition(self):
        pass

    def draw(self):
        self.screen.fill((000, 000, 000))
        pygame.draw.rect(self.screen,(0,255,0),(0,500-10,600,600))
        self.dino.drawplayer(self.screen)
        pygame.display.flip()

    def run(self):
        self.handleInput()
        self.dino.move()
        self.draw()


run = main(500, 500)
while True:
    clock.tick(60)
    run.run()

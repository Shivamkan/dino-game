import pygame
from util import *


class player:
    def __init__(self):
        self.monvingspeed = 0
        self.dino = pygame.Rect(50, 100, 50, 50)

    def jump(self):
        if self.dino.y >= 60:
            self.dino.y += 5
            self.monvingspeed = 5

    def handleInput(self, input):
        for event in input:
            if event.type == pygame.KEYDOWN:
                if event.key == pygame.K_SPACE:
                    self.jump()

    def drawplayer(self,screen):
        pygame.draw.rect(screen,(RGB("#424242"),self.dino))
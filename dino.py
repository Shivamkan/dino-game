import pygame
from util import *
import map


class player:
    def __init__(self,height):
        self.height = height
        self.monvingspeed = 0
        self.dino = pygame.Rect(50, 100, 50, 50)

    def jump(self):
        if self.dino.y >= self.height - 62:
            self.dino.y -= 5
            self.monvingspeed = -5

    def move(self):
        self.dino.y += int(self.monvingspeed)
        self.monvingspeed += 0.1
        if self.dino.y >= self.height - 12 - self.dino.height:
            self.monvingspeed = 0

    def handleInput(self, input):
        for event in input:
            if event.type == pygame.KEYDOWN:
                if event.key == pygame.K_SPACE:
                    self.jump()

    def drawplayer(self,screen):
        pygame.draw.rect(screen,(RGB("#424242")),self.dino)
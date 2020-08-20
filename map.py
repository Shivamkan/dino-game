import pygame
from random import randint

class map:
    def __init__(self,height,width):
        self.width = width
        self.height = height

    def spawncac(self):
        x = randint(320, 400)
        pygame.Rect(self.width,x,self.width + 30, self.height+10)

    def draw(self):
        pygame.draw.rect()
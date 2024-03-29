import sys 
import pygame
from settings import *
from PACPY import *
pygame.init()
VV = pygame.math.Vector2
class App:
    def __init__(self):
        self.screen = pygame.display.set_mode((WIDTH, HEIGHT))
        self.clock = pygame.time.Clock()
        self.running = True
        self.state = 'intro'
    def run(self):
        while self.running:
            if self.state == "intro":
                self.intro_events()
                self.intro_update()
                self.intro_draw()
            self.clock.tick(FPS)
        pygame.quit()
        sys.exit()
    def intro_events(self):
        for event in pygame.event.get():
            if event.type == pygame.quit:
                self.running = False
    def intro_update(self):
        pass
    def intro_draw(self):
        pygame.display.update()


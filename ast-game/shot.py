import circleshape
from constants import *
import pygame

class Shot(circleshape.CircleShape):
    def __init__(self, x, y):
        super().__init__(x, y, SHOT_RADIUS)

    def draw(self, screen):
        pygame.draw.circle(surface=screen, center=self.position, color="white", radius=self.radius, width=2)

    def update(self, dt):
        self.position += self.velocity * dt


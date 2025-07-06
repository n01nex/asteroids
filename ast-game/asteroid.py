import circleshape
from constants import *
import pygame
import random

class Asteroid(circleshape.CircleShape):
    def __init__(self, x, y, radius):
        super().__init__(x, y, radius)

    def draw(self, screen):
        pygame.draw.circle(surface=screen, center=self.position, color="yellow", radius=self.radius, width=2)

    def update(self, dt):
        self.position += self.velocity * dt

    def split(self):
        self.kill()
        if self.radius <= ASTEROID_MIN_RADIUS:
            return
        else:
            ex_angle = random.uniform(20, 50)
            ex1 = self.velocity.rotate(ex_angle)
            ex2 = self.velocity.rotate(-ex_angle)
            new_radius = self.radius - ASTEROID_MIN_RADIUS
            na1 = Asteroid(self.position.x, self.position.y, new_radius)
            na2 = Asteroid(self.position.x, self.position.y, new_radius)
            na1.velocity = ex1
            na2.velocity = ex2



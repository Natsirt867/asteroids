import pygame
import random
from circleshape import CircleShape
from constants import *


class Asteroid(CircleShape):
    def __init__(self, x, y, radius):
        super().__init__(x, y, radius)


    def update(self, dt):
        self.position += (self.velocity * dt) 

    def draw(self, screen):
        asteroid = pygame.draw.circle(screen, "white", self.position, self.radius, 2)

    def split(self):
        self.kill()
        if self.radius <= ASTEROID_MIN_RADIUS:
            return
        else:
            rand_angle = random.uniform(20, 50)
            velocity_rotated = self.velocity.rotate(rand_angle)
            velocity_rotated2 = self.velocity.rotate(-rand_angle)
            new_radius = self.radius - ASTEROID_MIN_RADIUS
            asteroid = Asteroid(self.position.x, self.position.y, new_radius)
            asteroid.velocity = velocity_rotated * 1.2 
            asteroid = Asteroid(self.position.x, self.position.y, new_radius)
            asteroid.velocity = velocity_rotated2 * 1.2

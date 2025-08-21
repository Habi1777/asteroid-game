import pygame
import random
from circleshape import CircleShape
from constants import ASTEROID_MIN_RADIUS

class Asteroid(CircleShape):
    def __init__(self, x, y, radius):
        super().__init__(x, y, radius)

    def draw(self, screen):
        pygame.draw.circle(screen, (255,255,255), self.position, self.radius, 2)

    def update(self, dt):
        self.position += (self.velocity * dt)

    def split(self):
        # getting rid of original asteroid if shot and checking it should be split into 2 new asteroids or if it was already too small
        self.kill()
        if self.radius <= ASTEROID_MIN_RADIUS:
            return
        
        ran_degree = random.uniform(20, 50)
        random_angled_velocity = self.velocity.rotate(ran_degree)
        neg_random_angled_velocity = self.velocity.rotate(-ran_degree)
        new_radius = self.radius - ASTEROID_MIN_RADIUS
        rock1 = Asteroid(self.position.x, self.position.y, new_radius)
        rock2 = Asteroid(self.position.x, self.position.y, new_radius)
        rock1.velocity = random_angled_velocity * 1.2
        rock2.velocity = neg_random_angled_velocity * 1.2
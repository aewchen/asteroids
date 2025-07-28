from circleshape import CircleShape
import pygame
from constants import *
import random

class Asteroid(CircleShape):
  def __init__(self, x, y, radius):
    super().__init__(x, y, radius)
  
  def draw(self, screen):
    pygame.draw.circle(surface=screen, color="white", center=self.position, radius=self.radius, width=2)
  
  def update(self, dt):
    self.position += self.velocity*dt
  
  def split(self):
    self.kill()
    if self.radius <= ASTEROID_MIN_RADIUS:
        return
    angle = random.uniform(20, 50)
    meteor_1_vector = self.velocity.rotate(angle)
    meteor_2_vector = self.velocity.rotate(-angle)
    new_radius = self.radius - ASTEROID_MIN_RADIUS
    asteroid1 = Asteroid(self.position.x, self.position.y, new_radius)
    asteroid1.velocity = meteor_1_vector * 1.2
    asteroid2 = Asteroid(self.position.x, self.position.y, new_radius) 
    asteroid2.velocity = meteor_2_vector * 1.2

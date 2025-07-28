from circleshape import CircleShape
from bullet import Shot
import pygame
from constants import *

class Player(CircleShape):
  def __init__(self, x, y):
      super().__init__(x,y, PLAYER_RADIUS)
      self.rotation = 0
      self.rate = 0
  
  # in the player class
  def triangle(self):
      forward = pygame.Vector2(0, 1).rotate(self.rotation)
      right = pygame.Vector2(0, 1).rotate(self.rotation + 90) * self.radius / 1.5
      a = self.position + forward * self.radius
      b = self.position - forward * self.radius - right
      c = self.position - forward * self.radius + right
      return [a, b, c]

  def draw(self, screen):
      pygame.draw.polygon(surface=screen, color="white", points=self.triangle(), width=2)
  
  def rotate(self, dt):
      self.rotation += PLAYER_TURN_SPEED * dt

  def update(self, dt):
      keys = pygame.key.get_pressed()
      self.rate -= dt

      if keys[pygame.K_a]:
          self.rotate(-dt)
      if keys[pygame.K_d]:
          self.rotate(dt)
      if keys[pygame.K_w]:
          self.move(dt)
      if keys[pygame.K_s]:
          self.move(-dt)
      if keys[pygame.K_SPACE]:
          self.shoot()


  def move(self, dt):
      forward = pygame.Vector2(0, 1).rotate(self.rotation)
      self.position += forward * PLAYER_SPEED * dt
  
  def shoot(self):
      if self.rate <= 0:
          self.rate = PLAYER_SHOOT_COOLDOWN 
          bullet = Shot(self.position.x, self.position.y)
          bullet.velocity = pygame.Vector2(0,1).rotate(self.rotation) * PLAYER_SHOT_SPEED

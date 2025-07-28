import pygame
from player import Player
from asteroid import Asteroid
from asteroidfield import AsteroidField
from constants import *
from bullet import Shot
import sys


def main():
    print("Starting Asteroids!")
    print(f"Screen width: {SCREEN_WIDTH}")
    print(f"Screen height: {SCREEN_HEIGHT}")
    pygame.init()
    updateable = pygame.sprite.Group()
    drawable = pygame.sprite.Group()
    asteroids = pygame.sprite.Group()
    bullets = pygame.sprite.Group()

    Player.containers = (updateable, drawable)
    Asteroid.containers = (asteroids, updateable, drawable)
    AsteroidField.containers = (updateable)
    Shot.containers = (updateable, drawable, bullets)

    asteroidfield = AsteroidField()
    player = Player(SCREEN_WIDTH/2, SCREEN_HEIGHT/2)
    screen = pygame.display.set_mode((SCREEN_WIDTH, SCREEN_HEIGHT))
    timer = pygame.time.Clock()
    dt = 0
    
    while True:
      for event in pygame.event.get():
        if event.type == pygame.QUIT:
          return
      screen.fill((0,0,0))
      for drawing in drawable: 
        drawing.draw(screen)
      pygame.display.flip()
      dt = timer.tick(60) / 1000
      updateable.update(dt)
      for asteroid in asteroids:
        if asteroid.collision(player):
          sys.exit("Game Over!")
        for bullet in bullets:
            if asteroid.collision(bullet):
                bullet.kill()
                asteroid.split()

if __name__ == "__main__":
    main()

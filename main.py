import pygame
import sys
from constants import *
from player import *
from asteroid import Asteroid
from asteroidfield import AsteroidField

def main():
    pygame.init()
    game_clock = pygame.time.Clock()
    dt = 0
    #created groups for objects to be able to update/draw/loop through easier
    updatable = pygame.sprite.Group()
    drawables = pygame.sprite.Group()
    asteroids_group = pygame.sprite.Group()
    bullets_group = pygame.sprite.Group()
    #use .containers to assign object classes to groups
    Player.containers = (updatable, drawables)
    Asteroid.containers = (asteroids_group, updatable, drawables)
    AsteroidField.containers = (updatable)
    Shot.containers = (bullets_group, updatable, drawables)
    print("Starting Asteroids!")
    print(f"Screen width: {SCREEN_WIDTH}\nScreen height: {SCREEN_HEIGHT}")
    screen = pygame.display.set_mode((SCREEN_WIDTH, SCREEN_HEIGHT))
    field_1 = AsteroidField()
    player_1 = Player(SCREEN_WIDTH/2, SCREEN_HEIGHT/2)
    while True:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                return
        updatable.update(dt)
        for asteroid in asteroids_group:
            if player_1.collision_check(asteroid):
                sys.exit("Game over!")
            #adding for loop to check for bullet and asteroid collisions
            for bullet in bullets_group:
                if bullet.collision_check(asteroid):
                    bullet.kill()
                    asteroid.split()
        screen.fill((0 , 0, 0))
        for item in drawables:
            item.draw(screen)
        pygame.display.flip()
        dt = game_clock.tick(60) / 1000


if __name__ == "__main__":
    main()

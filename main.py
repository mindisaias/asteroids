# this allows us to use code from
# the open-source pygame library
# throughout this file
import sys
import pygame
import asteroidfield
from constants import SCREEN_HEIGHT, SCREEN_WIDTH
from player import *
from asteroid import *
from asteroidfield import *
from shot import *
def main():
    print("Starting Asteroids!")
    print(f"Screen width: {SCREEN_WIDTH}")
    print(f"Screen height: {SCREEN_HEIGHT}")
    pygame.init()
    screen = pygame.display.set_mode((SCREEN_WIDTH, SCREEN_HEIGHT))
    clock = pygame.time.Clock()
    dt = 0
    updatable = pygame.sprite.Group()
    drawable = pygame.sprite.Group()  
    asteroids = pygame.sprite.Group()
    shots = pygame.sprite.Group()
    Shot.containers = (shots, updatable, drawable)
    Player.containers = (updatable, drawable)
    Asteroid.containers = (asteroids, updatable, drawable)
    AsteroidField.containers = updatable
    player = Player(SCREEN_WIDTH / 2, SCREEN_HEIGHT / 2)
    asteroid_field = AsteroidField()
    while True:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                return

        updatable.update(dt)
        for asteroid in asteroids:
            if player.collisionChecker(asteroid):
                print("Game over!")
                sys.exit()

            for shot in shots:
                if asteroid.collisionChecker(shot):
                    asteroid.split()
                    shot.kill()

        screen.fill("black")

        for entity in drawable:
            entity.draw(screen)

        pygame.display.flip()

        dt = clock.tick(60)
        dt = dt / 1000
if __name__ == "__main__":
    main()

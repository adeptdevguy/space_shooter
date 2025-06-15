import pygame
from constants import *
from player import Player
from asteroid import Asteroid
from asteroidfield import *
from circleshape import CircleShape
from shot import Shot
import sys



def main():

    # initialize pygame 
    pygame.init()

    # Create a display window for our game(height and width are already defined)
    screen = pygame.display.set_mode((SCREEN_WIDTH, SCREEN_HEIGHT))
    clock = pygame.time.Clock()

    updatable = pygame.sprite.Group()
    drawable = pygame.sprite.Group()
    asteroid = pygame.sprite.Group()
    shot = pygame.sprite.Group()


    Asteroid.containers = (asteroid, updatable, drawable)
    Shot.containers = (shot, updatable, drawable)
    AsteroidField.containers = updatable
    asteroid_field = AsteroidField()

    
    Player.containers = (updatable, drawable)

    player = Player(SCREEN_WIDTH / 2, SCREEN_HEIGHT / 2)

    dt = 0
    
    # Creating the game loop
    while True:

        # Close the game window if press on X 
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                return
        
        # Movement of player and drawing on the game window
        updatable.update(dt)

        screen.fill("black")
        
        for obj in drawable:
            obj.draw(screen)

        for obj in asteroid:
            if obj.collision_check(player):
                print("Game Over!")
                sys.exit()

        pygame.display.flip()

        # limit the framerates to 60 FPS
        dt = clock.tick(60) / 1000
        


if __name__ == "__main__":
    main()
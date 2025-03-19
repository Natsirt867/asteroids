from os import environ
environ["PYGAME_HIDE_SUPPORT_PROMPT"] = "hide"
import pygame
import sys
from constants import SCREEN_WIDTH, SCREEN_HEIGHT
from player import Player
from asteroid import Asteroid
from asteroidfield import AsteroidField
from shot import Shot

def main():
    print("Starting Asteroids!")
    print(f"Screen width: {SCREEN_WIDTH}")
    print(f"Screen height: {SCREEN_HEIGHT}")

    pygame.init()
  
    screen = pygame.display.set_mode((SCREEN_WIDTH, SCREEN_HEIGHT))
    
    # game ticks
    clock = pygame.time.Clock()    
    
    # delta time
    dt = 0

    # sets all shot objects inot a group
    shots = pygame.sprite.Group()  
 
    # sets all asteroid objects into a group
    asteroids = pygame.sprite.Group()

    # sets all updatable objects into a group
    updatable = pygame.sprite.Group()

    # sets all drawable objects into a group
    drawable = pygame.sprite.Group()

    # creates a container for updatable and drawable groups for the Shot class
    Shot.containers = (shots, updatable, drawable)

    # creates a container for updatable and drawable groups for the Player class
    Player.containers = (updatable, drawable)
    
    # creates a container for updatable groups for the AsteroidField class
    AsteroidField.containers = (updatable)

    # creates a container for asteroids, updatable and drawable groups for the Asteroids class 
    Asteroid.containers = (asteroids, updatable, drawable)

    # creates a Player object and sets it to player variable
    player = Player(SCREEN_WIDTH / 2, SCREEN_HEIGHT / 2, shots)  

    # creates an asteroid_field object and sets it to the asteroid_field variable
    asteroid_field = AsteroidField()

    # infinite game loop
    while True:
        #checks if pygame quit event was called (allows 'X' button on window to work)
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                return

        # fills the screen with a color "black" in this case 'RGB'
        screen.fill((0, 0, 0))
        
        # for loop to sort through our drawable entties in the group
        for entity in drawable:
            entity.draw(screen) 

        updatable.update(dt) 

        # needs to be called at the end of our game loop to make sure its updated properly
        pygame.display.update()
        dt = clock.tick(60) / 1000
        
        for asteroid in asteroids:
            
            if player.collision(asteroid):
                print("Game over!")
                sys.exit()
            for bullet in shots:
                if asteroid.collision(bullet):
                    asteroid.split()
                    bullet.kill()

if __name__ == "__main__":
    main()

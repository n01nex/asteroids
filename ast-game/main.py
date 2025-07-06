import pygame
import sys
from player import *
from constants import *
from asteroid import *
from asteroidfield import *
from shot import *

def main():

    print("Starting Asteroids!")
    print(f"Screen width: {SCREEN_WIDTH}")
    print(f"Screen height: {SCREEN_HEIGHT}")

    game_running = True
    pygame.init()

    # group creation for screen update management
    updatable = pygame.sprite.Group()
    drawable = pygame.sprite.Group()
    asteroids_gp = pygame.sprite.Group()
    shots = pygame.sprite.Group()

    # FPS
    clock = pygame.time.Clock()
    dt = 0

    # Initializing screen display with set sizes
    screen = pygame.display.set_mode((SCREEN_WIDTH, SCREEN_HEIGHT))

    # Initializing the player object and setting group containers
    Player.containers = (updatable, drawable)
    p1 = Player(int(SCREEN_WIDTH/2), int(SCREEN_HEIGHT/2))

    # Initializing asteroids
    Asteroid.containers = (asteroids_gp, updatable, drawable)
    AsteroidField.containers = (updatable)
    af = AsteroidField()

    # Initializing shots
    Shot.containers = (shots, updatable, drawable)

    while game_running:

        # Registering the closure of the window and exiting the game loop
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                return
        
        # fill the screen with black
        screen.fill("black")
        # draws the items of the group drawable
        for drw in drawable:
            drw.draw(screen)
        # update the items after status change like key pressed
        updatable.update(dt)

        for ast in asteroids_gp:
            if ast.collisions(p1):
                print("Game over!")
                game_running = False
                sys.exit()
            
            for sh in shots:
                if ast.collisions(sh):
                    sh.kill()
                    ast.split()  

        # flip refreshes the screen
        pygame.display.flip()
        # pauses the loop for 1/60th of a second and stores the value since it was called in milliseconds in dt
        dt = int(clock.tick(60))/1000


if __name__ == "__main__":
    main()

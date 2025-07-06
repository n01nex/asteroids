import pygame
from player import *
from constants import *

def main():

    print("Starting Asteroids!")
    print(f"Screen width: {SCREEN_WIDTH}")
    print(f"Screen height: {SCREEN_HEIGHT}")

    game_running = True
    pygame.init()

    # group creation for screen update management
    updatable = pygame.sprite.Group()
    drawable = pygame.sprite.Group()

    # FPS
    clock = pygame.time.Clock()
    dt = 0

    # Initializing screen display with set sizes
    screen = pygame.display.set_mode((SCREEN_WIDTH, SCREEN_HEIGHT))

    # Initializing the player object and setting group containers
    Player.containers = (updatable, drawable)
    p1 = Player(int(SCREEN_WIDTH/2), int(SCREEN_HEIGHT/2))

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
        # flip refreshes the screen
        pygame.display.flip()
        # pauses the loop for 1/60th of a second and stores the value since it was called in milliseconds in dt
        dt = int(clock.tick(60))/1000



if __name__ == "__main__":
    main()

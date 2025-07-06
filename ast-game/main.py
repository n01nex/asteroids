import pygame
from player import *
from constants import *

def main():

    print("Starting Asteroids!")
    print(f"Screen width: {SCREEN_WIDTH}")
    print(f"Screen height: {SCREEN_HEIGHT}")

    game_running = True
    pygame.init()

    # FPS
    clock = pygame.time.Clock()
    dt = 0

    # Initializing screen display with set sizes
    screen = pygame.display.set_mode((SCREEN_WIDTH, SCREEN_HEIGHT))

    # Initializing the player object
    p1 = Player(x=SCREEN_WIDTH/2, y=SCREEN_HEIGHT/2)


    while game_running:

        # Registering the closure of the window and exiting the game loop
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                return
        
        # fill the screen with black
        screen.fill("black")
        # draws the player
        p1.draw(screen)
        # flip refreshes the screen
        pygame.display.flip()
        # pauses the loop for 1/60th of a second and stores the value since it was called in milliseconds in dt
        dt = int(clock.tick(60))/1000







if __name__ == "__main__":
    main()

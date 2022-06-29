import pygame
import os
import gameStates
import graphics

#set the movement speed and FPS of the game
FPS = 60
RUNNING = True

# Set the colo image
COLO_CUP = pygame.image.load(os.path.join('assets', 'colo_cup_1.png'))
COLO_CUP = pygame.transform.scale(COLO_CUP, (25, 75))

# should draw the different bits of trash
def draw_trash(inventory):
    
    pass

def main():
    I = 0
    global RUNNING
    clock = pygame.time.Clock()
    game_state = gameStates.GameState
    while RUNNING:
        clock.tick(FPS)
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                RUNNING = False

        game_state.state_manager(game_state)

    pygame.quit()

if __name__ == "__main__":
    main()

import pygame
import gameStates
pygame.init()
################################################################
# The main loop of the game. Though most of it's contents are
# in gamestates so we can easily switch level states.
# However, before the game is even started the user will be
# asked to put their name in the terminal so we can record their
# high score.
################################################################
name = input("Please enter your name to start the game >  ") 
print(f"Welcome {name}!")

scores = open("scores.txt", "a")
scores.write(name)
scores.close()

FPS = 60
clock = pygame.time.Clock()
game_state = gameStates.GameState()
pygame.display.set_caption("BinBoy")

def main():
  
    while True:
        clock.tick(FPS)
        game_state.state_manager()
if __name__ == "__main__":
    main()

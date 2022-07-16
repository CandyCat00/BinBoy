import graphics
import movement
from platforms import Platforms
from trash import Trash
import pygame
import sys
import menu
import maps
from inventory import Inventory
from music import Music

######################################################################
# This file is where all the different screens of the game are stored.
# Basically, the game state is just full of different game loops that
# get called when the screen changes.
######################################################################

screen = pygame.display.set_mode((graphics.Window.WIDTH,graphics.Window.HEIGHT))

class GameState():
    HIT_GOAL = False
    CREATE = 0
    GOAL = 1230 #graphics.Window.WIDTH - (graphics.Window.WIDTH/30) * 2
    END_OF_LEVEL = 0
    LEVEL_START = 0
    LEVEL_2_DONE = False
    FINAL_SCORE =  0
    FILE = open("scores.txt","a") # ADDED THIS LINE TO OPEN THE FILE

    def __init__(self):
        self.state = "main_menu"

    # Run the main Menu
    def main_menu(self):
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                pygame.quit()
                sys.exit()

        if GameState.CREATE == 0:
            Music.play_music(-1)
            GameState.CREATE = 1
                
        screen.blit(menu.background,(0,0))
        if menu.start_button.draw(screen):
            print("START")
            self.state = "first_message"
        if menu.exit_button.draw(screen):
            print("EXIT")
            pygame.quit()
            sys.exit()
        
        pygame.display.update()
    
    # Run the first Message
    def first_message(self):
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                pygame.quit()
                sys.exit()
                
        screen.blit(menu.first_message,(0,0))
        if menu.continue_button.draw(screen):
            print("Continue")
            GameState.CREATE = 0
            self.state = "second_message"
        
        pygame.display.update()
    
    # Run the seccond Message
    def second_message(self):
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                pygame.quit()
                sys.exit()
        
        screen.blit(menu.second_message,(0,0))
        if menu.continue_button.draw(screen):
            print("Continue")
            self.state = "third_message"
     
        pygame.display.update()
    
    # Run the third Message
    def third_message(self):
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                pygame.quit()
                sys.exit()
        
        screen.blit(menu.third_message,(0,0))
        if menu.letsgo_button.draw(screen):
            Music.stop()
            GameState.CREATE = 0
            self.state = "level_1"
            
     
        pygame.display.update()

    def fourth_message(self):
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                pygame.quit()
                sys.exit()
        
        if GameState.CREATE == 0:
            Music.play_music(-1)
            GameState.CREATE = 1
        
        screen.blit(menu.fourth_message,(0,0))
        if menu.tips_button.draw(screen):
            print("4th")
            Music.stop()
            GameState.CREATE = 0
            self.state = "level_2"
            
     
        pygame.display.update()

    def thanks_message(self):
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                pygame.quit()
                sys.exit()

        screen.blit(menu.thanks_message,(0,0))
        if menu.final_button.draw(screen):
            print("EXIT")
            pygame.quit()
            sys.exit()

        pygame.display.update()
    
    
    # Run level 1
    def level_1(self):
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                pygame.quit()
                sys.exit()

        GameState.END_OF_LEVEL = graphics.Window.WIDTH
        # We create everything for level 1
        if (GameState.CREATE == 0):
            Music.play_music(1)
            Platforms.createPlatforme()
            Trash.createBanana()
            Trash.createBottle()
            Trash.createNewspaper()
            Trash.createPlastic()
            Trash.createGoal()
            GameState.CREATE = 1
      
        graphics.Window.draw_level_1(graphics.Window, movement.Screen.SCROLL_INDEX)
        movement.Chara.movement(movement.Chara, graphics.Binboy.BINBOY_POS)
        movement.Screen.scroll(movement.Screen, graphics.Binboy.BINBOY_POS)
        
        # If we get to the goal we clear everything and give binboy a start position for mext
        if (GameState.HIT_GOAL == True):
            Music.stop()
            Platforms.PLATFORMS.clear()
            Trash.BANANAS.clear()
            Trash.BOTTLES.clear()
            Trash.NEWSPAPERS.clear()
            Trash.PLASTICS.clear()
            Trash.GOAL.clear()
            GameState.CREATE = 0
            GameState.BONUS = True
            graphics.Binboy.BINBOY_POS.x = 0
            graphics.Binboy.BINBOY_POS.y = 650
            movement.Screen.SCROLL_INDEX = 0
            #graphics.Window.SCORE = 0
            self.state = "bonus_level"
            GameState.HIT_GOAL = False

        pygame.display.update()

    
    
    # Run level 2
    def level_2(self):

        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                pygame.quit()
                sys.exit()

        GameState.END_OF_LEVEL = graphics.Window.WIDTH
        maps.Maps.LEVEL_1 = maps.Maps.LEVEL_2

        if (GameState.CREATE == 0):
            Music.play_music(2)
            Platforms.createPlatforme()
            Trash.createBanana()
            Trash.createBottle()
            Trash.createNewspaper()
            Trash.createPlastic()
            Trash.createGoal()
            GameState.CREATE = 1
      
        graphics.Window.draw_level_2(graphics.Window, movement.Screen.SCROLL_INDEX)
        movement.Chara.movement(movement.Chara, graphics.Binboy.BINBOY_POS)
        movement.Screen.scroll(movement.Screen, graphics.Binboy.BINBOY_POS)

        if (GameState.HIT_GOAL == True):
            GameState.LEVEL_2_DONE = True
            Platforms.PLATFORMS.clear()
            Trash.BANANAS.clear()
            Trash.BOTTLES.clear()
            Trash.NEWSPAPERS.clear()
            Trash.PLASTICS.clear()
            Trash.GOAL.clear()
            GameState.CREATE = 0
            movement.Screen.SCROLL_INDEX = 0
            self.state = "bonus_level"

        pygame.display.update()

      
     # Run bonus level   
    def bonus_level(self):
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                pygame.quit()
                sys.exit()
            elif event.type == pygame.MOUSEBUTTONDOWN:
                movement.Selection.make_selection()

        if GameState.CREATE == 0:
            Music.play_music(0)
            GameState.CREATE = 1

        if Inventory.is_empty():
            GameState.FINAL_SCORE = graphics.Window.SCORE
            Music.stop()
            GameState.CREATE = 0
            if GameState.LEVEL_2_DONE == False:
                self.state = "fourth_message" 
            elif GameState.LEVEL_2_DONE == True:
                print(f"Your score is {GameState.FINAL_SCORE}\n") # print the score on the terminal                    ADDED
                GameState.FILE.write(f" {GameState.FINAL_SCORE}\n") # save the score next to the name in the file       ADDED
                GameState.FILE = open("scores.txt","r") # We read the file now                                          ADDED   
                print("SCORE LIST:\n")                                                                                  #ADDED
                for x in GameState.FILE:                                                                                #ADDED
                    print(x)                                                                                            #ADDED
                self.state = "thanks_message"
        else:
            graphics.Window.draw_bonus_level(graphics.Window)
            movement.Selection.hover()

    
    # Manage what is happening when is the different states are called
    def state_manager(self):
        if self.state == "main_menu":
            self.main_menu()
        if self.state == "level_1":
            self.level_1()
        if self.state == "level_2":
            self.level_2()
        if self.state == "bonus_level":
            self.bonus_level()
        if self.state == "first_message":
            self.first_message()
        if self.state == "second_message":
            self.second_message()
        if self.state == "third_message":
            self.third_message()
        if self.state == "fourth_message":
            self.fourth_message()
        if self.state == "thanks_message":
            self.thanks_message()

import pygame
import os
from maps import Maps

BANANA = pygame.image.load(os.path.join('assets', 'banana.png'))
BANANA = pygame.transform.scale(BANANA, (40, 40))
PLASTIC = pygame.image.load(os.path.join('assets', 'plastic.png'))
PLASTIC = pygame.transform.scale(PLASTIC, (40, 40))
BOTTLE = pygame.image.load(os.path.join('assets', 'bottle.png'))
BOTTLE = pygame.transform.scale(BOTTLE, (30, 40))
NEWSPAPER = pygame.image.load(os.path.join('assets', 'newspaper.png'))
NEWSPAPER = pygame.transform.scale(NEWSPAPER, (40, 40))
TRASH_GOAL = pygame.image.load(os.path.join('assets', 'GOAL.png'))
TRASH_GOAL =  pygame.transform.scale(TRASH_GOAL, (160, 80))

    
    
class Trash:
    BANANAS = []
    NEWSPAPERS = []
    PLASTICS = []
    BOTTLES = []
    GOAL = []
    TRASH_SIZE = 40

    def createBanana():
        for row_index,row in enumerate(Maps.LEVEL_1):
            for col_index, col in enumerate(row):
                x = col_index * Trash.TRASH_SIZE
                y = row_index * Trash.TRASH_SIZE
                if col == "B":
                    trash = pygame.Rect((x,y,40,40)) # save the coordinates of "B" and the size of the rectangle that it will draw it
                    Trash.BANANAS.append(trash)   # save all the "B" into the array TRASH
    
    def createNewspaper():
        for row_index,row in enumerate(Maps.LEVEL_1):
            for col_index, col in enumerate(row):
                x = col_index * Trash.TRASH_SIZE
                y = row_index * Trash.TRASH_SIZE
                if col == "N":
                    trash = pygame.Rect((x,y,40,40)) # save the coordinates of "N" and the size of the rectangle that it will draw it
                    Trash.NEWSPAPERS.append(trash)  # save all the "N" into the array TRASH
    
    def createPlastic():
        for row_index,row in enumerate(Maps.LEVEL_1):
            for col_index, col in enumerate(row):
                x = col_index * Trash.TRASH_SIZE
                y = row_index * Trash.TRASH_SIZE
                if col == "C":
                    trash = pygame.Rect((x,y,40,40)) # save the coordinates of "C" and the size of the rectangle that it will draw it
                    Trash.PLASTICS.append(trash)  # save all the "C" into the array TRASH

    def createBottle():
        for row_index,row in enumerate(Maps.LEVEL_1):
            for col_index, col in enumerate(row):
                x = col_index * Trash.TRASH_SIZE
                y = row_index * Trash.TRASH_SIZE
                if col == "L":
                    trash = pygame.Rect((x,y,40,40)) # save the coordinates of "L" and the size of the rectangle that it will draw it
                    Trash.BOTTLES.append(trash)  # save all the "L" into the array TRASH
    
    def createGoal():
        for row_index,row in enumerate(Maps.LEVEL_1):
            for col_index, col in enumerate(row):
                x = col_index * Trash.TRASH_SIZE
                y = row_index * Trash.TRASH_SIZE
                if col == "F":
                    trash = pygame.Rect((x,y,40,40)) # save the coordinates of "L" and the size of the rectangle that it will draw it
                    Trash.GOAL.append(trash) 
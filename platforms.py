import pygame
from maps import Maps

class Platforms:
    PLATFORMS = []
    PLAT_SIZE = 50

    def createPlatforme():
        for row_index,row in enumerate(Maps.LEVEL_1):
            for col_index, col in enumerate(row):
                x = col_index * Platforms.PLAT_SIZE
                y = row_index * Platforms.PLAT_SIZE
                print(f"x {x}  y{y}")
                if col == "X":
                    platform = pygame.Rect((x,y,50,50))
                    Platforms.PLATFORMS.append(platform)


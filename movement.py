import pygame
import gameStates
import graphics
import main

class Chara:
    VEL_X = 5
    VEL_Y = 20
    JUMP = False
    MOVE_L = False
    MOVE_R = False

    def movement(self, binboy):
        keys_pressed = pygame.key.get_pressed()
        if keys_pressed[pygame.K_a] and binboy.x - Chara.VEL_X > 0: #LEFT
            binboy.x -= Chara.VEL_X
            Chara.MOVE_L = True
            Chara.MOVE_R = False
        elif keys_pressed[pygame.K_d] and binboy.x + Chara.VEL_X < graphics.Window.WIDTH - 100: #RIGHT
            binboy.x += Chara.VEL_X
            Chara.MOVE_R = True
            Chara.MOVE_L = False
        else:
            Chara.MOVE_L = False
            Chara.MOVE_R = False

        if Chara.JUMP is False and keys_pressed[pygame.K_SPACE]:
            Chara.JUMP = True

        if Chara.JUMP:
            binboy.y -= Chara.VEL_Y
            Chara.VEL_Y -= 1
            if Chara.VEL_Y < -20:
                Chara.JUMP = False
                Chara.VEL_Y = 20

class Screen:
    SCROLL_INDEX = 0
    VEL_X = 5
    Vel_Y = 15

    def scroll(self, binboy):
        if Chara.MOVE_R and binboy.x - Chara.VEL_X > graphics.Window.WIDTH - 500 and Screen.SCROLL_INDEX != gameStates.GameState.END_OF_LEVEL:
            Screen.SCROLL_INDEX += Screen.VEL_X
            binboy.x -= Chara.VEL_X
        if Chara.MOVE_L and binboy.x - Chara.VEL_X < 300 and Screen.SCROLL_INDEX != gameStates.GameState.LEVEL_START:
            Screen.SCROLL_INDEX -= Screen.VEL_X
            binboy.x += Chara.VEL_X

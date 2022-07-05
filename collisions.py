import pygame
import movement
import graphics
from platforms import Platforms

class Collision:
    X_COLLI = False
    Y_COLLI = False
    ON_GROUND = True

    def checkXcolli():
        binboy = graphics.Binboy.BINBOY_POS
        for sprite in Platforms.PLATFORMS:
            if sprite.colliderect(binboy):
                if movement.Chara.MOVE_L:
                    binboy.left = sprite.right
                elif movement.Chara.MOVE_R:
                    binboy.right = sprite.left

    def checkYcolli():
        binboy = graphics.Binboy.BINBOY_POS
        for sprite in Platforms.PLATFORMS:
            if sprite.colliderect(binboy):
                if movement.Chara.VEL_Y > 0: #moving up
                    binboy.top = sprite.bottom
                    movement.Chara.VEL_Y = -11
                elif movement.Chara.VEL_Y < 0: #moving down
                    binboy.bottom = sprite.top
                    movement.Chara.VEL_Y = -11
            if (binboy.bottom != sprite.top):
                binboy.y += movement.Chara.VEL_Y

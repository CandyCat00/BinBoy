from turtle import width
import pygame
import gameStates
import graphics
from collisions import Collision
from platforms import Platforms
from trash import Trash
from inventory import Inventory

class Chara:
    VEL_X = 4
    VEL_Y = 8
    JUMP = False
    MOVE_L = False
    MOVE_R = False
    ACCELERATION = 0.25

    def movement(self, binboy):
    
        Chara.new_player_x = binboy.x
        Chara.new_player_y = binboy.y

        Chara.VEL_Y += Chara.ACCELERATION
        Chara.new_player_y += Chara.VEL_Y

        keys_pressed = pygame.key.get_pressed()
        if keys_pressed[pygame.K_a] and binboy.x - Chara.VEL_X > 0 and binboy.x > 0:  #LEFT
            Chara.new_player_x -= Chara.VEL_X
            Chara.MOVE_L = True
            Chara.MOVE_R = False
        elif keys_pressed[pygame.K_d] and binboy.x + Chara.VEL_X < graphics.Window.WIDTH-40: #RIGHT
            Chara.new_player_x += Chara.VEL_X
            Chara.MOVE_R = True
            Chara.MOVE_L = False
        else:
            Chara.MOVE_L = False
            Chara.MOVE_R = False
        
        Collision.checkXcolli(Chara.new_player_x, binboy)
        Collision.checkYcolli(Chara.new_player_y, binboy)
        Collision.checkTrashColli(binboy)

        if  keys_pressed[pygame.K_SPACE] and Collision.player_on_ground:
            Chara.VEL_Y = -7    

class Screen:
    SCROLL_INDEX = 0
    VEL_X = 5
    Vel_Y = 15

    def scroll(self, binboy):
        if Chara.MOVE_R and binboy.x - Chara.VEL_X > graphics.Window.WIDTH - 500 and Screen.SCROLL_INDEX != gameStates.GameState.END_OF_LEVEL:
            Screen.SCROLL_INDEX += Screen.VEL_X
            binboy.x -= Chara.VEL_X
            for plat in Platforms.PLATFORMS:
                plat.x -= Chara.VEL_X
            for trash in Trash.BANANAS:
                trash.x -= Chara.VEL_X
            for trash in Trash.BOTTLES:
                trash.x -= Chara.VEL_X 
            for trash in Trash.NEWSPAPERS:
                trash.x -= Chara.VEL_X
            for trash in Trash.PLASTICS:
                trash.x -= Chara.VEL_X 
            for trash in Trash.GOAL:
                trash.x -= Chara.VEL_X 

        if Chara.MOVE_L and binboy.x - Chara.VEL_X < 300 and Screen.SCROLL_INDEX != gameStates.GameState.LEVEL_START:
            Screen.SCROLL_INDEX -= Screen.VEL_X
            binboy.x += Chara.VEL_X
            for plat in Platforms.PLATFORMS:
                plat.x += Chara.VEL_X
            for trash in Trash.BANANAS:
                trash.x += Chara.VEL_X
            for trash in Trash.BOTTLES:
                trash.x += Chara.VEL_X
            for trash in Trash.NEWSPAPERS:
                trash.x += Chara.VEL_X
            for trash in Trash.PLASTICS:
                trash.x += Chara.VEL_X
            for trash in Trash.GOAL:
                trash.x += Chara.VEL_X

class Selection:
    PLASTIC_BIN = False
    PAPER_BIN = False
    GLASS_BIN = False
    TRASH_CAN = False

    def hover():
        cursor = pygame.mouse.get_pos()
        if (cursor[0] in range(graphics.Cans.CAN1.left, graphics.Cans.CAN1.right) and
            cursor[1] in range(graphics.Cans.CAN1.top, graphics.Cans.CAN1.bottom)):
            Selection.TRASH_CAN = True
        else:
            Selection.TRASH_CAN = False

        if (cursor[0] in range(graphics.Cans.CAN2.left, graphics.Cans.CAN2.right) and
            cursor[1] in range(graphics.Cans.CAN2.top, graphics.Cans.CAN2.bottom)):
            Selection.PLASTIC_BIN = True
        else:
            Selection.PLASTIC_BIN = False

        if (cursor[0] in range(graphics.Cans.CAN3.left, graphics.Cans.CAN3.right) and
            cursor[1] in range(graphics.Cans.CAN3.top, graphics.Cans.CAN3.bottom)):
            Selection.PAPER_BIN = True
        else:
            Selection.PAPER_BIN = False

        if (cursor[0] in range(graphics.Cans.CAN4.left, graphics.Cans.CAN4.right) and
            cursor[1] in range(graphics.Cans.CAN4.top, graphics.Cans.CAN4.bottom)):
            Selection.GLASS_BIN = True
        else:
            Selection.GLASS_BIN = False

    def make_selection():
        if not Selection.TRASH_CAN and not Selection.GLASS_BIN and not Selection.PAPER_BIN and not Selection.PLASTIC_BIN:
            return

        #take the first item from the inventory and check if it belongs in that bin
        item = Inventory.inventory[0]
        if (item == 'T'):
            if Selection.TRASH_CAN:
                graphics.Window.SCORE += 1 #add points if it does
            else:
                graphics.Window.SCORE -= 1 #lose points if it doesnt
        if (item == 'L'):
            if Selection.PLASTIC_BIN:
                graphics.Window.SCORE += 1 #add points if it does
            else:
                graphics.Window.SCORE -= 1 #lose points if it doesnt
        if (item == 'N'):
            if Selection.PAPER_BIN:
                graphics.Window.SCORE += 1 #add points if it does
            else:
                graphics.Window.SCORE -= 1 #lose points if it doesnt
        if (item == 'B'):
            if Selection.GLASS_BIN:
                graphics.Window.SCORE += 1 #add points if it does
            else:
                graphics.Window.SCORE -= 1 #lose points if it doesnt
        #delete the item from the inventory and get the next one
        Inventory.delete_trash()
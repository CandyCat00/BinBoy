from platform import platform
import pygame
import os
import movement
import platforms
import trash
from inventory import Inventory

pygame.init()

class Binboy:
    binboy_height = 65
    binboy_width = 40 
    posX = platforms.Platforms.setPlayerPosition()
    posY = platforms.Platforms.setPlayerPositionY()
    BINBOY_POS = pygame.Rect(posX,posY, binboy_width, binboy_height)
    RUN_FRAME = 0

    #Set the movement.Chara character image
    BINBOY_IDOL = pygame.image.load(os.path.join('assets', 'binboyTEST1.png'))
    BINBOY_IDOL = pygame.transform.scale(BINBOY_IDOL, (binboy_width, binboy_height))

    #The character images when moving right
    BINBOY_RIGHT = [None]*10
    for rightIndex in range(1, 11):
        BINBOY_RIGHT[rightIndex - 1] = pygame.image.load(os.path.join('assets', 'binboy_right_' + str(rightIndex) + '.png'))
        rightIndex += 1
    for rightIndex in range(1, 11):
        BINBOY_RIGHT[rightIndex - 1] = pygame.transform.scale(BINBOY_RIGHT[rightIndex - 1], (binboy_width, binboy_height))
        rightIndex += 1

    #The character images when moving left
    BINBOY_LEFT = [None]*10
    for leftIndex in range(1, 11):
        BINBOY_LEFT[leftIndex - 1] = pygame.image.load(os.path.join('assets', 'binboy_left_' + str(leftIndex) + '.png'))
        leftIndex += 1
    for leftIndex in range(1, 11):
        BINBOY_LEFT[leftIndex - 1] = pygame.transform.scale(BINBOY_LEFT[leftIndex - 1], (binboy_width, binboy_height))
        leftIndex += 1

    def draw_binboy(self):
        if Binboy.RUN_FRAME > 54: 
            Binboy.RUN_FRAME = 0
        if movement.Chara.JUMP:
            if movement.Chara.MOVE_R:
                Window.WIN.blit(Binboy.BINBOY_RIGHT[4], (Binboy.BINBOY_POS.x, Binboy.BINBOY_POS.y))
            if movement.Chara.MOVE_L:
                Window.WIN.blit(Binboy.BINBOY_LEFT[4], (Binboy.BINBOY_POS.x, Binboy.BINBOY_POS.y))
            else:
                Window.WIN.blit(Binboy.BINBOY_RIGHT[4], (Binboy.BINBOY_POS.x, Binboy.BINBOY_POS.y))
        elif movement.Chara.MOVE_R:
            Window.WIN.blit(Binboy.BINBOY_RIGHT[Binboy.RUN_FRAME//6], (Binboy.BINBOY_POS.x, Binboy.BINBOY_POS.y))
            Binboy.RUN_FRAME += 1
        elif movement.Chara.MOVE_L:
            Window.WIN.blit(Binboy.BINBOY_LEFT[Binboy.RUN_FRAME//6], (Binboy.BINBOY_POS.x, Binboy.BINBOY_POS.y))
            Binboy.RUN_FRAME += 1
        else:
            Window.WIN.blit(Binboy.BINBOY_IDOL, (Binboy.BINBOY_POS.x, Binboy.BINBOY_POS.y))
            Binboy.RUN_FRAME = 0

class Window:
    pygame.display.set_caption("Binboy")
    WIDTH, HEIGHT = 1280,700
    WIN = pygame.display.set_mode((WIDTH, HEIGHT))
    BEACH = pygame.image.load(os.path.join('assets', 'beachfinal.png')).convert_alpha()
    PARK = pygame.image.load(os.path.join('assets', 'park1.png')).convert_alpha()
    GRASS = (100, 200, 100)
    SKY = (180, 180, 255)
    SAND = (248,200,129)
    GROUND = pygame.Rect(0, HEIGHT - HEIGHT/8, WIDTH, HEIGHT/3)
    BACKGROUND = (245, 66, 152)
    white = (255, 255, 255)
    font = pygame.font.Font('freesansbold.ttf', 32)
    SCORE = 0
  
    def draw_level_1(self, SCROLL_INDEX):
        
        # Draw the scrolling background  
        Window.WIN.blit(Window.BEACH,(0 - SCROLL_INDEX,0))
        # Draw the score on the window
        score = str(Window.SCORE)
        text = Window.font.render(f'Score {score}', True,  Window.white)
        textRect = text.get_rect()
        textRect.center = (65, 20)
        Window.WIN.blit(text, textRect)
       
       # Draw Binboy on the screen
        Binboy.draw_binboy(Binboy)
        
        # Draw the platforms on the screen
        for plat in platforms.Platforms.PLATFORMS:
            pygame.draw.rect(Window.WIN, Window.SAND, plat)
        
        # Draw the trash on the screen
        for t in trash.Trash.BANANAS:
                Window.WIN.blit(trash.BANANA, (t.x, t.y))
        for t in trash.Trash.NEWSPAPERS:
                Window.WIN.blit(trash.NEWSPAPER, (t.x, t.y))
        for t in trash.Trash.BOTTLES:
                Window.WIN.blit(trash.BOTTLE, (t.x, t.y))
        for t in trash.Trash.PLASTICS:
                Window.WIN.blit(trash.PLASTIC, (t.x, t.y))
        for t in trash.Trash.GOAL:
                Window.WIN.blit(trash.TRASH_GOAL, (t.x, t.y))
       
        pygame.display.update()

    def draw_level_2(self, SCROLL_INDEX):
        
     
        # Draw the scrolling background  
        Window.WIN.blit(Window.PARK,(0 - SCROLL_INDEX,0))

        # Draw the score on the window
        score = str(Window.SCORE)
        text = Window.font.render(f'Score {score}', True,  Window.white)
        textRect = text.get_rect()
        textRect.center = (65, 20)
        Window.WIN.blit(text, textRect)
       
       # Draw Binboy on the screen
        Binboy.draw_binboy(Binboy)
        
        # Draw the platforms on the screen
        for plat in platforms.Platforms.PLATFORMS:
            pygame.draw.rect(Window.WIN, Window.GRASS, plat)
        
        # Draw the trash on the screen
        for t in trash.Trash.BANANAS:
                Window.WIN.blit(trash.BANANA, (t.x, t.y))
        for t in trash.Trash.NEWSPAPERS:
                Window.WIN.blit(trash.NEWSPAPER, (t.x, t.y))
        for t in trash.Trash.BOTTLES:
                Window.WIN.blit(trash.BOTTLE, (t.x, t.y))
        for t in trash.Trash.PLASTICS:
                Window.WIN.blit(trash.PLASTIC, (t.x, t.y))
        for t in trash.Trash.GOAL:
                Window.WIN.blit(trash.TRASH_GOAL, (t.x, t.y))

        pygame.display.update()

    
    def draw_bonus_level(self):
        ground = Window.GROUND
        ground.y = Window.HEIGHT - Window.HEIGHT/3
        Window.WIN.fill(Window.SKY)
        pygame.draw.rect(Window.WIN, Window.GRASS, ground)
        Cans.draw_cans()
        Items.drawItems()

        pygame.display.update()

class Cans:
    TRASH_CAN_OPEN = pygame.image.load(os.path.join('assets', 'trash_can_open.png'))
    TRASH_CAN_OPEN = pygame.transform.scale(TRASH_CAN_OPEN, (200, 250))

    PLASTIC_CAN_OPEN = pygame.image.load(os.path.join('assets', 'plastic_bin_open.png'))
    PLASTIC_CAN_OPEN = pygame.transform.scale(PLASTIC_CAN_OPEN, (200, 250))

    PAPER_CAN_OPEN = pygame.image.load(os.path.join('assets', 'paper_bin_open.png'))
    PAPER_CAN_OPEN = pygame.transform.scale(PAPER_CAN_OPEN, (200, 250))

    GLASS_CAN_OPEN = pygame.image.load(os.path.join('assets', 'glass_bin_open.png'))
    GLASS_CAN_OPEN = pygame.transform.scale(GLASS_CAN_OPEN, (200, 250))

    TRASH_CAN_CLOSED = pygame.image.load(os.path.join('assets', 'trash_can_closed.png'))
    TRASH_CAN_CLOSED = pygame.transform.scale(TRASH_CAN_CLOSED, (200, 250))

    PLASTIC_CAN_CLOSED = pygame.image.load(os.path.join('assets', 'plastic_bin_closed.png'))
    PLASTIC_CAN_CLOSED = pygame.transform.scale(PLASTIC_CAN_CLOSED, (200, 250))

    PAPER_CAN_CLOSED = pygame.image.load(os.path.join('assets', 'paper_bin_closed.png'))
    PAPER_CAN_CLOSED = pygame.transform.scale(PAPER_CAN_CLOSED, (200, 250))

    GLASS_CAN_CLOSED = pygame.image.load(os.path.join('assets', 'glass_bin_closed.png'))
    GLASS_CAN_CLOSED = pygame.transform.scale(GLASS_CAN_CLOSED, (200, 250))


    CAN1 = pygame.Rect(Window.WIDTH/5 - 100, Window.HEIGHT/2 - 100, 200, 250)
    CAN2 = pygame.Rect((Window.WIDTH/5)*2 - 100, Window.HEIGHT/2 - 100, 200, 250)
    CAN3 = pygame.Rect((Window.WIDTH/5)*3 - 100, Window.HEIGHT/2 - 100, 200, 250)
    CAN4 = pygame.Rect((Window.WIDTH/5)*4 - 100, Window.HEIGHT/2 - 100, 200, 250)

    def draw_cans():
        if (movement.Selection.TRASH_CAN):
            Window.WIN.blit(Cans.TRASH_CAN_OPEN, (Cans.CAN1.x, Cans.CAN1.y))
        else:
            Window.WIN.blit(Cans.TRASH_CAN_CLOSED, (Cans.CAN1.x, Cans.CAN1.y))

        if (movement.Selection.PLASTIC_BIN):
            Window.WIN.blit(Cans.PLASTIC_CAN_OPEN, (Cans.CAN2.x, Cans.CAN2.y))
        else:
            Window.WIN.blit(Cans.PLASTIC_CAN_CLOSED, (Cans.CAN2.x, Cans.CAN2.y))

        if (movement.Selection.PAPER_BIN):
            Window.WIN.blit(Cans.PAPER_CAN_OPEN, (Cans.CAN3.x, Cans.CAN3.y))
        else:
            Window.WIN.blit(Cans.PAPER_CAN_CLOSED, (Cans.CAN3.x, Cans.CAN3.y))

        if (movement.Selection.GLASS_BIN):
            Window.WIN.blit(Cans.GLASS_CAN_OPEN, (Cans.CAN4.x, Cans.CAN4.y))
        else:
            Window.WIN.blit(Cans.GLASS_CAN_CLOSED, (Cans.CAN4.x, Cans.CAN4.y))

class Items:
    NEWSPAPER = pygame.image.load(os.path.join('assets', 'newspaper.png'))
    BOTTLE = pygame.image.load(os.path.join('assets', 'bottle.png'))
    PLASTIC = pygame.image.load(os.path.join('assets', 'plastic.png'))
    BANANA = pygame.image.load(os.path.join('assets', 'banana.png'))

    FIRST_ITEM = pygame.Rect(Window.WIDTH/2 - 50, (Window.HEIGHT/4)*3 + 50, 100, 100)
    NEXT_ITEM = pygame.Rect(Window.WIDTH/2 + 100, (Window.HEIGHT/4)*3 + 75, 50, 50)

    def drawItems():
        first, next = Inventory.display_inventory()
        if first in 'B':
            Items.BANANA = pygame.transform.scale(Items.BANANA, (100, 100))
            Window.WIN.blit(Items.BANANA, Items.FIRST_ITEM)
        if first in 'N':
            Items.NEWSPAPER = pygame.transform.scale(Items.NEWSPAPER, (100, 100))
            Window.WIN.blit(Items.NEWSPAPER, Items.FIRST_ITEM)
        if first in 'C':
            Items.PLASTIC = pygame.transform.scale(Items.PLASTIC, (100, 100))
            Window.WIN.blit(Items.PLASTIC, (Items.FIRST_ITEM.x, Items.FIRST_ITEM.y))
        if first in 'L':
            Items.BOTTLE = pygame.transform.scale(Items.BOTTLE, (100, 100))
            Window.WIN.blit(Items.BOTTLE, Items.FIRST_ITEM)

        if next == 'B':
            Items.BANANA = pygame.transform.scale(Items.BANANA, (50, 50))
            Window.WIN.blit(Items.BANANA, Items.NEXT_ITEM)
        if next == 'N':
            Items.NEWSPAPER = pygame.transform.scale(Items.NEWSPAPER, (50, 50))
            Window.WIN.blit(Items.NEWSPAPER, Items.NEXT_ITEM)
        if next == 'C':
            Items.PLASTIC = pygame.transform.scale(Items.PLASTIC, (50, 50))
            Window.WIN.blit(Items.PLASTIC, Items.NEXT_ITEM)
        if next == 'L':
            Items.BOTTLE = pygame.transform.scale(Items.BOTTLE, (50, 50))
            Window.WIN.blit(Items.BOTTLE, Items.NEXT_ITEM)
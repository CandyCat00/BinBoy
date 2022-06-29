from tokenize import PseudoToken
import pygame
import os
import movement

class Binboy:
    BINBOY_POS = pygame.Rect(100, 438 - 140, 100, 150)
    RUN_FRAME = 0

    #Set the movement.Chara character image
    BINBOY_IDOL = pygame.image.load(os.path.join('assets', 'binboyTEST.png'))
    BINBOY_IDOL = pygame.transform.scale(BINBOY_IDOL, (100, 150))

    #The character images when moving right
    BINBOY_RIGHT = [None]*10
    for rightIndex in range(1, 11):
        BINBOY_RIGHT[rightIndex - 1] = pygame.image.load(os.path.join('assets', 'binboy_right_' + str(rightIndex) + '.png'))
        rightIndex += 1
    for rightIndex in range(1, 11):
        BINBOY_RIGHT[rightIndex - 1] = pygame.transform.scale(BINBOY_RIGHT[rightIndex - 1], (120, 150))
        rightIndex += 1

    #The character images when moving left
    BINBOY_LEFT = [None]*10
    for leftIndex in range(1, 11):
        BINBOY_LEFT[leftIndex - 1] = pygame.image.load(os.path.join('assets', 'binboy_left_' + str(leftIndex) + '.png'))
        leftIndex += 1
    for leftIndex in range(1, 11):
        BINBOY_LEFT[leftIndex - 1] = pygame.transform.scale(BINBOY_LEFT[leftIndex - 1], (120, 150))
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
    WIDTH, HEIGHT = 900, 500
    WIN = pygame.display.set_mode((WIDTH, HEIGHT))
    SKY = (180, 180, 255)
    GRASS = (100, 200, 100)
    GROUND = pygame.Rect(0, HEIGHT - HEIGHT/8, WIDTH, 200)
    BACKGROUND = (245, 66, 152)

    def draw_level_1(self, SCROLL_INDEX):
        Window.WIN.fill(Window.SKY)
        pygame.draw.rect(Window.WIN, Window.BACKGROUND, pygame.Rect(Window.WIDTH - SCROLL_INDEX, 0, Window.WIDTH, Window.HEIGHT))
        pygame.draw.rect(Window.WIN, Window.GRASS, Window.GROUND)
        Binboy.draw_binboy(Binboy)
        
        pygame.display.update()
    
    def draw_bonus_level(self):
        ground = Window.GROUND
        ground.y = Window.HEIGHT - Window.HEIGHT/3
        Window.WIN.fill(Window.SKY)
        pygame.draw.rect(Window.WIN, Window.GRASS, ground)
        Cans.draw_cans()

        pygame.display.update()

class Cans:
    TRASH_CAN_OPEN = pygame.image.load(os.path.join('assets', 'trash_can.png'))
    TRASH_CAN_OPEN = pygame.transform.scale(TRASH_CAN_OPEN, (200, 250))

    CAN1 = pygame.Rect(Window.WIDTH/5 - 100, Window.HEIGHT/2 - 100, 200, 250)
    CAN2 = pygame.Rect((Window.WIDTH/5)*2 - 100, Window.HEIGHT/2 - 100, 200, 250)
    CAN3 = pygame.Rect((Window.WIDTH/5)*3 - 100, Window.HEIGHT/2 - 100, 200, 250)
    CAN4 = pygame.Rect((Window.WIDTH/5)*4 - 100, Window.HEIGHT/2 - 100, 200, 250)

    def draw_cans():
        Window.WIN.blit(Cans.TRASH_CAN_OPEN, (Cans.CAN1.x, Cans.CAN1.y))
        Window.WIN.blit(Cans.TRASH_CAN_OPEN, (Cans.CAN2.x, Cans.CAN2.y))
        Window.WIN.blit(Cans.TRASH_CAN_OPEN, (Cans.CAN3.x, Cans.CAN3.y))
        Window.WIN.blit(Cans.TRASH_CAN_OPEN, (Cans.CAN4.x, Cans.CAN4.y))
import pygame
import os

#Window display settings
pygame.display.set_caption("Binboy")
WIDTH, HEIGHT = 900, 500
WIN = pygame.display.set_mode((WIDTH, HEIGHT))
SKY = (180, 180, 255)
GRASS = (100, 200, 100)
GROUND = pygame.Rect(0, HEIGHT - HEIGHT/8, WIDTH, 100)
BACKGROUND = (245, 66, 152)

#set the movement speed and FPS of the game
FPS = 60
VEL_X = 5
VEL_Y = 20
JUMP = False
MOVE_L = False
MOVE_R = False
RUN_FRAME = 0

#Level Assets
I = 0
LEVEL_START = 0
END_OF_LEVEL = WIDTH * 2

#Set the main character image
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

#Draws the character and animates him
def draw_character(binboy):
    global RUN_FRAME
    if RUN_FRAME > 54: 
        RUN_FRAME = 0

    if JUMP:
        if MOVE_R:
            WIN.blit(BINBOY_RIGHT[4], (binboy.x, binboy.y))
        if MOVE_L:
            WIN.blit(BINBOY_LEFT[4], (binboy.x, binboy.y))
        else:
            WIN.blit(BINBOY_RIGHT[4], (binboy.x, binboy.y))
    elif MOVE_R:
        WIN.blit(BINBOY_RIGHT[RUN_FRAME//6], (binboy.x, binboy.y))
        RUN_FRAME += 1
    elif MOVE_L:
        WIN.blit(BINBOY_LEFT[RUN_FRAME//6], (binboy.x, binboy.y))
        RUN_FRAME += 1
    else:
        WIN.blit(BINBOY_IDOL, (binboy.x, binboy.y))
        RUN_FRAME = 0

#Draws everything to the screen
def draw_window(binboy, I):
    WIN.fill(SKY)
    pygame.draw.rect(WIN, BACKGROUND, pygame.Rect(WIDTH - I, 0, WIDTH, HEIGHT))
    pygame.draw.rect(WIN, GRASS, GROUND)
    draw_character(binboy)
    
    pygame.display.update()

#tells the rest of the code what the user wants binboy to do and moves him
def movement(binboy):
    global JUMP
    global MOVE_L
    global MOVE_R
    keys_pressed = pygame.key.get_pressed()
    if keys_pressed[pygame.K_a] and binboy.x - VEL_X > 0: #LEFT
        binboy.x -= VEL_X
        MOVE_L = True
        MOVE_R = False
    elif keys_pressed[pygame.K_d] and binboy.x + VEL_X < WIDTH - 100: #RIGHT
        binboy.x += VEL_X
        MOVE_R = True
        MOVE_L = False
    else:
        MOVE_L = False
        MOVE_R = False

    if JUMP is False and keys_pressed[pygame.K_SPACE]: #JUMP
        JUMP = True
    global VEL_Y
    if JUMP:
        binboy.y -= VEL_Y
        VEL_Y -= 1
        if VEL_Y < -20:
            JUMP = False
            VEL_Y = 20


def main():
    I = 0
    binboy = pygame.Rect(100, GROUND.y - 140, 100, 150)
    clock = pygame.time.Clock()
    run = True
    while run:
        clock.tick(FPS)
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                run = False


        if  MOVE_R and binboy.x - VEL_X > WIDTH - 500 and I != END_OF_LEVEL:
            I += VEL_X
            binboy.x -= VEL_X
        if MOVE_L and binboy.x - VEL_X < 300 and I != LEVEL_START:
            I -=VEL_X
            binboy.x += VEL_X

        draw_window(binboy, I)
        movement(binboy)
    
    pygame.quit()

if __name__ == "__main__":
    main()

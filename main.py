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
VEL_Y = 15
JUMP = False

I = 0

#Set the main character image
BINBOY_IMAGE = pygame.image.load(os.path.join('assets', 'binboyTEST.png'))
BINBOY_IMAGE = pygame.transform.scale(BINBOY_IMAGE, (100, 150))

def draw_window(binboy, I):
    WIN.fill(SKY)
    pygame.draw.rect(WIN, BACKGROUND, pygame.Rect(WIDTH - I,0,WIDTH,HEIGHT))
    pygame.draw.rect(WIN, GRASS, GROUND)
    WIN.blit(BINBOY_IMAGE, (binboy.x, binboy.y))
    
    pygame.display.update()

MOVE_L = False
MOVE_R = False
def movement(binboy):
    global JUMP
    global MOVE_L
    global MOVE_R
    keys_pressed = pygame.key.get_pressed()
    if keys_pressed[pygame.K_a] and binboy.x - VEL_X > 0: #LEFT
        binboy.x -= VEL_X
        MOVE_L = True
        MOVE_R = False
    elif keys_pressed[pygame.K_d] and binboy.x < 800: #RIGHT
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
        if VEL_Y < -15:
            JUMP = False
            VEL_Y = 15


def main():
    I = 0
    keys_pressed = pygame.key.get_pressed()
    binboy = pygame.Rect(400, GROUND.y - 140, 100, 150)
    clock = pygame.time.Clock()
    run = True
    while run:
        clock.tick(FPS)
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                run = False


        if  MOVE_R == True:
            I += VEL_X
        if MOVE_L == True:
            I -=VEL_X
        if  binboy.x - VEL_X > WIDTH - 400:
            binboy.x -= VEL_X
        if binboy.x - VEL_X < 400:
            binboy.x += VEL_X

        draw_window(binboy, I)
        movement(binboy)
    
    pygame.quit()

if __name__ == "__main__":
    main()
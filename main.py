import pygame
import os

#Window display settings
pygame.display.set_caption("Binboy")
WIDTH, HEIGHT = 900, 500
WIN = pygame.display.set_mode((WIDTH, HEIGHT))
SKY = (180, 180, 255)
GRASS = (100, 200, 100)
GROUND = pygame.Rect(0, HEIGHT - HEIGHT/8, WIDTH, 100)

#set the movement speed and FPS of the game
FPS = 60
VEL_X = 5
VEL_Y = 15
JUMP = False

#Set the main character image
BINBOY_IMAGE = pygame.image.load(os.path.join('assets', 'binboyTEST.png'))
BINBOY_IMAGE = pygame.transform.scale(BINBOY_IMAGE, (100, 150))

def draw_window(binboy):
    WIN.fill(SKY)
    pygame.draw.rect(WIN, GRASS, GROUND)
    WIN.blit(BINBOY_IMAGE, (binboy.x, binboy.y))
    pygame.display.update()

def movement(binboy):
    global JUMP
    keys_pressed = pygame.key.get_pressed()
    if keys_pressed[pygame.K_a] and binboy.x - VEL_X > 0: #LEFT
        binboy.x -= VEL_X
    if keys_pressed[pygame.K_d]: #RIGHT
        binboy.x += VEL_X
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
    binboy = pygame.Rect(100, GROUND.y - 140, 100, 150)
    clock = pygame.time.Clock()
    run = True
    while run:
        clock.tick(FPS)
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                run = False
        
        draw_window(binboy)

        movement(binboy)
    
    pygame.quit()

if __name__ == "__main__":
    main()
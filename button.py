import pygame

class Button():
    def __init__(self,x,y, image, scale):
        width = image.get_width()
        height = image.get_height()
        self.image = pygame.transform.scale(image, (int(width*scale), int(height*scale)))
        self.rect = self.image.get_rect()
        self.rect.topleft = (x,y)
        self.clicked = False
        self.scale = scale

    def draw(self, surface):
        action = False
        # get mouse position
        pos = pygame.mouse.get_pos()
        
        # check mouse and clicked conditions
        if self.rect.collidepoint(pos):
            if pygame.mouse.get_pressed()[0] == True and self.clicked == False:
                self.clicked = True
                action = True
        if pygame.mouse.get_pressed()[0] == False:
            self.clicked = False

        surface.blit(self.image, (self.rect.x, self.rect.y))   
        
        return action
import graphics
import movement
import platforms

class GameState:
    def __init__(self):
        self.state = "state_manager"

    #Variables that change the scene
    LEVEL = 1     #What level are they on?
    BONUS = False #Are they in the bonus stage?
    MENU = False  #is there a menu open?

    #Variables that don't are used in levels, but don't change
    LEVEL_START = 0
    GOAL = graphics.Window.WIDTH - (graphics.Window.WIDTH/8) * 3

    #this variable tells us how far the level will scroll and can be changed.
    #Zero means it will now scroll
    END_OF_LEVEL = 0
    
    def level_1(self):
        GameState.END_OF_LEVEL = graphics.Window.WIDTH * 2
        graphics.Window.draw_level_1(graphics.Window, movement.Screen.SCROLL_INDEX)
        movement.Chara.movement(movement.Chara, graphics.Binboy.BINBOY_POS)
        movement.Screen.scroll(movement.Screen, graphics.Binboy.BINBOY_POS)

        if (graphics.Binboy.BINBOY_POS.x >= GameState.GOAL):
            GameState.LEVEL += 1
            GameState.BONUS = True
        
    def bonus_level(self):
        graphics.Window.draw_bonus_level(graphics.Window)

    def state_manager(self):
        if (GameState.BONUS):
            self.bonus_level(GameState)
        else:
            match GameState.LEVEL:
                case 1:
                    self.level_1(GameState)
                #case 2:
                    #self.bonus_level(GameState)


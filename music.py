import pygame

class Music:
    def play_music(level):
        if level == -1:
            pygame.mixer.music.load('Happy-Alley.wav')
            pygame.mixer.music.play(-1)
        elif level == 0:
            pygame.mixer.music.load('Wallpaper.wav')
            pygame.mixer.music.play(-1)
        elif level == 1:
            pygame.mixer.music.load('happy_bee_surf.wav')
            pygame.mixer.music.play(-1)
        elif level == 2:
            pygame.mixer.music.load('Carpe-Diem.wav')
            pygame.mixer.music.play(-1)

    def stop():
        pygame.mixer.music.stop()



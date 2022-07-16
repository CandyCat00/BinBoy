import pygame

######################################################################
# This class is called when we want music to be played or stopped.
# All music however will work better if you convert the MP3s to WAV 
# files, but WAV is too big for GitHub
######################################################################
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



import pygame
import os
import button

background = pygame.image.load("background.png").convert_alpha()
first_message= pygame.image.load(os.path.join('assets', 'firstMessage.png')).convert_alpha()
second_message= pygame.image.load(os.path.join('assets', 'secondMessage.png')).convert_alpha()
third_message= pygame.image.load(os.path.join('assets', 'thirdMessage.png')).convert_alpha()
fourth_message = pygame.image.load(os.path.join('assets', 'fourth_message.png')).convert_alpha()

start_img = pygame.image.load(os.path.join('assets', 'start_btn.png')).convert_alpha()
exit_img = pygame.image.load(os.path.join('assets', 'exit_btn.png')).convert_alpha()
cont_img = pygame.image.load(os.path.join('assets', 'continue.png')).convert_alpha()
go_img = pygame.image.load(os.path.join('assets', 'letsgo.png')).convert_alpha()

start_button = button.Button(400,400,start_img,1)
exit_button = button.Button(700,400,exit_img,1)
continue_button = button.Button(900,500,cont_img,1)
letsgo_button = button.Button(700,500,go_img,1)
tips_button = button.Button(1100,50,cont_img,0.5)
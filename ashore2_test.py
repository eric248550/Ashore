import pygame
from time import sleep

file = "./music.mp3"
pygame.mixer.init()
pygame.mixer.music.load(file)
m = pygame.mixer.music
m.set_volume(0.5 + vol/12)
m.play()

